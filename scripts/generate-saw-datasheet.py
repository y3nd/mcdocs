"""Create the French, two-page A4 product datasheet from the product page.

Install dependencies: python -m pip install reportlab Pillow
Run from any directory: python scripts/generate-saw-datasheet.py
Output: public/datasheets/filtre-saw-868-f4nlv.pdf
"""

from __future__ import annotations

import re
from datetime import date
from io import BytesIO
from pathlib import Path
from xml.sax.saxutils import escape

from PIL import Image
from reportlab import rl_config
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfdoc import PDFString
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "filtres/saw-868-f4nlv.md"
OUTPUT = ROOT / "public/datasheets/filtre-saw-868-f4nlv.pdf"
URL = "https://meshcore.f4nlv.fr/filtres/saw-868-f4nlv.html"
PAGE_W, PAGE_H = A4
MARGIN = 42
WIDTH = PAGE_W - 2 * MARGIN
INK = colors.HexColor("#152E37")
TEAL = colors.HexColor("#00788C")
ORANGE = colors.HexColor("#F58B03")
MUTED = colors.HexColor("#526974")
PALE = colors.HexColor("#EEF6F7")
RULE = colors.HexColor("#D7E4E7")


def register_fonts():
    pdfmetrics.registerFont(TTFont("Logo", str(ROOT / "assets/fonts/Orbitron-Black.ttf")))
    pdfmetrics.registerFont(TTFont("Body", str(ROOT / "assets/fonts/Inter-Regular.ttf")))
    pdfmetrics.registerFont(TTFont("Strong", str(ROOT / "assets/fonts/Inter-Bold.ttf")))


class Datasheet:
    def __init__(self):
        self.generation_date = date.today().strftime("%Y/%m/%d")
        OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        self.pdf = canvas.Canvas(str(OUTPUT), pagesize=A4, pageCompression=1, initialFontName="Body")
        self.pdf.setTitle("Filtre SAW 868 MHz F4NLV — Fiche technique")
        self.pdf.setAuthor("F4NLV")
        self.pdf.setSubject("Filtre SAW pour MeshCore : caractéristiques, réponse en fréquence et montage")
        self.pdf.setKeywords("F4NLV, MeshCore, SAW, 868 MHz, 869 MHz, u.FL, fiche technique")
        self.pdf.setCreator("F4NLV product datasheet generator")
        self.pdf.setViewerPreference("DisplayDocTitle", "true")
        self.pdf.setCatalogEntry("Lang", PDFString("fr-FR"))

    def rect(self, x, top, width, height, fill, radius=0):
        self.pdf.setFillColor(fill)
        if radius:
            self.pdf.roundRect(x, PAGE_H - top - height, width, height, radius, stroke=0, fill=1)
        else:
            self.pdf.rect(x, PAGE_H - top - height, width, height, stroke=0, fill=1)

    def line(self, top, x=MARGIN, width=WIDTH):
        self.pdf.setStrokeColor(RULE)
        self.pdf.setLineWidth(0.6)
        self.pdf.line(x, PAGE_H - top, x + width, PAGE_H - top)

    def text(self, text, x, top, size=10, bold=False, color=INK):
        self.pdf.setFillColor(color)
        self.pdf.setFont("Strong" if bold else "Body", size)
        self.pdf.drawString(x, PAGE_H - top - size, text)

    def paragraph(self, text, x, top, width, size=10, color=INK, bold=False, leading=None):
        style = ParagraphStyle(
            "body", fontName="Strong" if bold else "Body", fontSize=size,
            leading=leading or size * 1.45, textColor=color, spaceAfter=0,
        )
        para = Paragraph(text, style)
        _, height = para.wrap(width, PAGE_H)
        para.drawOn(self.pdf, x, PAGE_H - top - height)
        return height

    def picture(self, path, x, top, width, height, *, lossless=False):
        with Image.open(path) as image:
            image = image.convert("RGB")
            if lossless:
                reader = ImageReader(image)
            else:
                # Keep full resolution and color detail; embed JPEG bytes directly.
                encoded = BytesIO()
                image.save(encoded, format="JPEG", quality=95, subsampling=0, optimize=True)
                encoded.seek(0)
                reader = ImageReader(encoded)
            self.pdf.drawImage(reader, x, PAGE_H - top - height,
                               width=width, height=height, preserveAspectRatio=True,
                               anchor="c", mask="auto")

    def furniture(self, number, label):
        self.rect(0, 0, PAGE_W, 5, TEAL)
        self.pdf.setFillColor(INK)
        self.pdf.setFont("Logo", 20)
        self.pdf.drawString(MARGIN, PAGE_H - 48, "F4NLV")
        self.text("MESHCORE · FILTRAGE RF", PAGE_W - MARGIN - 164, 36, 9, True, TEAL)
        self.line(65)
        self.line(785)
        self.text("meshcore.f4nlv.fr", MARGIN, 796, 8.5, color=TEAL)
        self.pdf.linkURL(URL, (MARGIN, PAGE_H - 808, MARGIN + 130, PAGE_H - 794), relative=0)
        self.text(label, 224, 796, 8, color=MUTED)
        self.text(self.generation_date, PAGE_W - MARGIN - 115, 796, 8, color=MUTED)
        self.text(f"{number} / 2", PAGE_W - MARGIN - 25, 796, 8.5, color=MUTED)


def main():
    # PDF supports binary streams, so ASCII85 adds unnecessary size.
    rl_config.useA85 = False
    register_fonts()
    source = SOURCE.read_text(encoding="utf-8")
    rows = []
    for line in source.splitlines():
        if line.startswith("|"):
            cells = [cell.strip() for cell in line.strip("|").split("|")]
            if len(cells) == 2 and cells[0] != "Caractéristique" and not cells[0].startswith("---"):
                rows.append(cells)
    specs = dict(rows)
    description = re.search(r'description="([^"]+)"', source).group(1)
    product_image = ROOT / re.search(r'image="/([^"]+)"', source).group(1)
    page_images = re.findall(
        r'!\[[^\]]*\]\(/([^\)]+)\)|<img\b[^>]*\bsrc="/([^"]+)"', source
    )
    response_image, assembly_image = [ROOT / (markdown or html) for markdown, html in page_images]
    contents_block = source.split("## Contenu de l'emballage", 1)[1].split("##", 1)[0]
    contents = [line[2:].strip() for line in contents_block.splitlines() if line.startswith("- ")]
    warnings_block = source.split(":::warning", 1)[1].split(":::", 1)[0]
    warnings = [line[2:].strip() for line in warnings_block.splitlines() if line.startswith("- ")]
    if len(rows) != 9 or len(contents) != 2 or len(warnings) != 2:
        raise ValueError("The source structure changed; review the datasheet layout before generating.")

    d = Datasheet()
    d.furniture(1, "FICHE TECHNIQUE")
    d.pdf.bookmarkPage("specifications")
    d.pdf.addOutlineEntry("Caractéristiques techniques", "specifications", level=0)
    d.text("FICHE PRODUIT", MARGIN, 85, 9, True, TEAL)
    d.text("Filtre SAW 868 MHz", MARGIN, 107, 32, True)
    d.text("Pour les nœuds MeshCore · Fabrication dans le Var, France", MARGIN, 153, 10.5, color=MUTED)
    # The source description is the single authority for the introductory copy.
    d.paragraph(escape(description), MARGIN, 181, WIDTH, 10, MUTED, leading=14)

    d.picture(product_image, MARGIN, 257, 274, 205.5)
    d.rect(336, 257, PAGE_W - MARGIN - 336, 205.5, PALE, 9)
    highlights = [
        (specs["Fréquence centrale"], "FRÉQUENCE CENTRALE", "Bande : " + specs["Bande passante"]),
        (specs["Perte d'insertion"].replace("1.5-1.8", "1,5–1,8"), "PERTE D'INSERTION", None),
        (specs["Puissance maximale"], "PUISSANCE MAXIMALE", None),
    ]
    for i, (value, label, detail) in enumerate(highlights):
        top = 271 + i * 64
        d.text(label, 350, top, 7.2, True, MUTED)
        d.text(value, 350, top + 14, 21, True, TEAL)
        if detail:
            d.text(detail, 350, top + 40, 8, color=MUTED)
    d.text("Le filtre et son câble u.FL fournis.", MARGIN, 468, 8, color=MUTED)

    d.text("Caractéristiques techniques", MARGIN, 502, 16, True)
    table_top = 537
    for i, (label, value) in enumerate(rows):
        top = table_top + i * 20.5
        if i % 2 == 0:
            d.rect(MARGIN, top, WIDTH, 20.5, PALE)
        d.text(label, MARGIN + 10, top + 3.5, 9)
        value = value.replace("1.5-1.8", "1,5–1,8").replace("30-40", "30–40")
        d.text(value, MARGIN + 230, top + 3.5, 9, True)
    d.line(table_top + len(rows) * 20.5)

    d.text("CONTACT", MARGIN, 747, 8, True, TEAL)
    d.text("filtres@f4nlv.fr", MARGIN + 75, 743, 12, True)
    d.pdf.linkURL("mailto:filtres@f4nlv.fr?subject=Filtre%20SAW%20868%20MHz",
                  (MARGIN + 75, PAGE_H - 763, MARGIN + 230, PAGE_H - 740), relative=0)
    d.text("Documentation et prise de contact en ligne", MARGIN + 266, 747, 8, color=MUTED)
    d.pdf.showPage()

    d.furniture(2, "MESURE & MONTAGE")
    d.pdf.bookmarkPage("response-and-assembly")
    d.pdf.addOutlineEntry("Réponse en fréquence et montage", "response-and-assembly", level=0)
    d.text("MESURE & MONTAGE", MARGIN, 85, 9, True, TEAL)
    d.text("Réponse & intégration", MARGIN, 108, 28, True)
    d.paragraph("Une réponse typique centrée sur 869 MHz, avec une atténuation des signaux "
                "indésirables en dehors de la bande passante.", MARGIN, 154, WIDTH, 10, MUTED)

    d.picture(response_image, MARGIN, 202, 324, 216, lossless=True)
    x = 386
    d.text("RÉPONSE EN FRÉQUENCE", x, 208, 7.3, True, TEAL)
    d.text(specs["Atténuation hors bande"].replace("30-40", "30–40"), x, 235, 24, True)
    d.paragraph("Atténuation hors bande", x, 271, PAGE_W - MARGIN - x, 10, MUTED)
    d.line(309, x, PAGE_W - MARGIN - x)
    d.paragraph("Courbe typique de réponse en fréquence.", x, 327, PAGE_W - MARGIN - x, 10, MUTED)
    d.paragraph("Chaque exemplaire possède des caractéristiques légèrement différentes.",
                x, 373, PAGE_W - MARGIN - x, 9, INK, True)
    d.text("Capture de mesure fournie dans la documentation du produit.", MARGIN, 428, 8, color=MUTED)
    d.line(457)

    d.text("Exemple de montage", MARGIN, 476, 16, True)
    d.picture(assembly_image, MARGIN, 511, 161, 248.65)
    x = 226
    column = PAGE_W - MARGIN - x
    d.text("Seeedstudio Sensecap Solar P1(-Pro)", x, 510, 12, True)
    d.paragraph("Exemple d'intégration du filtre avec ses connexions u.FL.",
                x, 539, column, 10, MUTED)

    d.rect(x, 584, column, 90, colors.HexColor("#FFF5E7"), 7)
    d.rect(x, 591, 3, 76, ORANGE)
    d.text("PRÉCAUTIONS DE MONTAGE", x + 14, 595, 8, True, colors.HexColor("#98600D"))
    # Put the battery-removal prerequisite first, without adding unsupported steps.
    top = 614
    for warning in reversed(warnings):
        height = d.paragraph("• " + escape(warning), x + 14, top, column - 28,
                             9, INK, leading=13)
        top += height + 6

    d.text("CONTENU DE L'EMBALLAGE", x, 695, 8, True, TEAL)
    top = 713
    for item in contents:
        item = item.replace("<->", "↔")
        height = d.paragraph("• " + escape(item), x, top, column, 9, leading=13)
        top += height + 7
    d.pdf.save()
    print(OUTPUT)


if __name__ == "__main__":
    main()
