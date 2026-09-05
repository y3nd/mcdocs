# MC Raw for Seeed Studio Wio Tracker L1

Minimal PlatformIO firmware for the Seeed Studio Wio Tracker L1. It does only
the following:

- exposes one line-oriented text API over USB serial and Bluetooth LE NUS;
- optionally receives LoRa packets and prints their raw payload as hexadecimal;
- reports RSSI, SNR, and frequency error for every successfully received packet;
- transmits the fixed `minitrig` and `minitrig-region` payload prefixes with a
  fresh two-byte hardware-random nonce appended;
- reports firmware version, battery voltage, help, and radio status.

GPS, display, buttons, buzzer, storage, mesh decoding, and message forwarding
are not initialized or implemented.

## Build and upload

Install [PlatformIO](https://platformio.org/), connect the Wio Tracker L1 over
USB, then run:

```sh
pio run
pio run --target upload
pio device monitor
```

The monitor baud rate is 115200. The serial interface is USB CDC, so the baud
rate is conventional rather than electrically significant.

The project includes the Wio Tracker L1 board and variant definitions. It
expects the factory-compatible UF2 bootloader and Nordic S140 v7 SoftDevice
memory layout used by the upstream board support.

Always connect a suitable 868 MHz antenna before enabling reception or
transmitting.

## Transports

Both transports accept and produce the exact same ASCII line protocol:

- USB serial: 115200 baud
- BLE: Nordic UART Service (NUS), advertised as `MC Raw L1`

Commands are case-insensitive and end with LF (`\n`), CR (`\r`), or CRLF
(`\r\n`) on both transports. Every output record ends with CRLF.

Some BLE terminals, including the default Nordic nRF Toolbox UART send action,
do not append an end-of-line byte. Optional idle-time framing can make each
such write execute after 30 ms without another received byte. It is disabled
by default. Enable it by uncommenting this build flag in `platformio.ini`:

```ini
-D ENABLE_BLE_IDLE_COMMAND_FRAMING=1
```

Responses and asynchronous events are broadcast to USB serial and, when a
client is connected, BLE NUS. There is no authentication.

## Commands

| Command | Result |
|---|---|
| `HELP` or `?` | Lists the complete command set and framing. |
| `VERSION` | Returns `VERSION 1.3.0`. |
| `BATTERY` | Returns the current battery voltage, millivolts, and raw 12-bit ADC value. |
| `STATUS` | Returns radio configuration/state, counters (including BLE output drops), battery, BLE state, uptime, and last packet metrics when available. |
| `RX ON` | Starts continuous raw LoRa reception. Reception defaults to off after every boot. |
| `RX OFF` | Stops reception and puts the SX1262 in standby. |
| `MINITRIG` | Transmits `19 00 00 00 00 00` followed by a fresh two-byte random nonce, then resumes reception if it was on. |
| `MINITRIG-REGION [region]` | Transmits the region-scoped packet with a calculated MeshCore transport code and fresh two-byte nonce. The region defaults to `fr`. |

No command changes the RF parameters and no arbitrary transmit command is
provided.

### MeshCore region transport code

`MINITRIG-REGION` uses the public MeshCore region `fr` by default:

```text
MINITRIG-REGION
MINITRIG-REGION de
MINITRIG-REGION #Europe
```

Region names are case-sensitive, matching MeshCore. A leading `#` is optional.
Public region names may contain letters, digits, `-`, and `_`; private `$`
regions are rejected because their secret transport key cannot be derived from
the name.

The packet is assembled as:

```text
18 [transport-code:2] 00 00 00 46 34 4E 4C 56 [nonce:2]
```

The transport code follows MeshCore's `TransportKey` calculation:

1. The public scope key is the first 16 bytes of `SHA-256("#" + region)`.
2. The HMAC input is payload type `06` followed by the final application
   payload `46 34 4E 4C 56 [nonce:2]`.
3. The transport code is the first two HMAC-SHA256 bytes. MeshCore's reserved
   values `0000` and `FFFF` are adjusted to `0100` and `FEFF`.
4. The second transport code remains reserved as `0000`.

## Output records

Successful packet reception produces one line:

```text
RX len=6 hex=190000000000 rssi_dbm=-81.5 snr_db=7.25 frequency_error_hz=-122.1
```

The `hex` field is uppercase, contains two characters per byte, and has no
separators. RSSI and SNR are measured for that same packet.

Other records use these prefixes:

```text
READY version=1.3.0 radio=ready radio_code=0 rx=off
OK rx=on
TX name=minitrig len=8 hex=190000000000A17C nonce=A17C result=ok airtime_ms=124
BATTERY millivolts=3978 voltage=3.978 raw_adc=2263
VERSION 1.3.0
STATUS ...
ERR operation=... radio_code=...
```

`radio_code=0` means success. Negative radio codes are RadioLib status codes.

## Fixed LoRa PHY

The requested frequency, bandwidth, and spreading factor identify the
MeshCore EU/UK Narrow PHY. The remaining parameters required for interoperable
LoRa packets are fixed to the corresponding Narrow values:

| Parameter | Value |
|---|---:|
| Frequency | 869.618 MHz |
| Bandwidth | 62.5 kHz |
| Spreading factor | 8 |
| Coding rate | 4/8 |
| Sync word | `0x12` |
| Header | Explicit |
| CRC | Enabled, 2 bytes |
| Preamble | 8 symbols |
| IQ | Normal |
| TX power | 22 dBm |
| TCXO voltage | 1.8 V |

“Raw” means that the complete LoRa PHY payload is shown unchanged. The
firmware does not parse, decrypt, validate, repeat, or otherwise participate in
MeshCore.

## Example session

```text
READY version=1.3.0 radio=ready radio_code=0 rx=off
STATUS
STATUS version=1.3.0 radio=ready radio_code=0 rx=off freq_mhz=869.618 bw_khz=62.5 sf=8 cr=4/8 sync_word=0x12 header=explicit crc=on preamble=8 tx_power_dbm=22 battery_mv=3978 ble=disconnected uptime_ms=6341 rx_packets=0 rx_errors=0 tx_packets=0 ble_output_drops=0
RX ON
OK rx=on
RX len=23 hex=1100AABBCCDDEEFF00112233445566778899AABBCCDDEE rssi_dbm=-93.0 snr_db=4.50 frequency_error_hz=61.0
MINITRIG
TX name=minitrig len=8 hex=190000000000A17C nonce=A17C result=ok airtime_ms=124
MINITRIG-REGION de
TX name=minitrig-region len=13 hex=18684A00000046344E4C5692D4 nonce=92D4 region=de transport_code=684A result=ok airtime_ms=165
RX OFF
OK rx=off
```
