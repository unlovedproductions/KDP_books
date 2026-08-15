#!/usr/bin/env python3
"""Typeset Book 2 interior to KDP 6x9 B&W no-bleed PDF."""

from __future__ import annotations

import re
from pathlib import Path

from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import inch
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch as IN
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    FrameBreak,
    HRFlowable,
    KeepTogether,
    ListFlowable,
    ListItem,
    NextPageTemplate,
    PageBreak,
    PageTemplate,
    Paragraph,
    Preformatted,
    Spacer,
    Table,
    TableStyle,
    Flowable,
)

ROOT = Path(__file__).resolve().parents[1]
MS_PATH = ROOT / "BOOK 2 — STOIC SHADOW WORK JOURNAL — MANUSCRIPT.md"
OUT_DIR = Path(__file__).resolve().parent / "output"
FONT_DIR = Path(__file__).resolve().parent / "fonts"

PAGE_W, PAGE_H = 6 * IN, 9 * IN
# Professional workbook margins (above KDP mins for <=150 pp)
GUTTER = 0.75 * IN
OUTER = 0.60 * IN
TOP = 0.60 * IN
BOTTOM = 0.65 * IN  # room for footer


class WriteLines(Flowable):
    def __init__(self, count=5, gap=16):
        super().__init__()
        self.count = count
        self.gap = gap
        self.width = 0
        self.height = count * gap

    def wrap(self, availWidth, availHeight):
        self.width = availWidth
        return availWidth, self.height

    def draw(self):
        self.canv.setStrokeColorRGB(0.35, 0.35, 0.35)
        self.canv.setLineWidth(0.4)
        y = self.height - 2
        for _ in range(self.count):
            self.canv.line(0, y, self.width, y)
            y -= self.gap


class CheckLine(Flowable):
    def __init__(self, labels: list[str]):
        super().__init__()
        self.labels = labels
        self.height = 18

    def wrap(self, availWidth, availHeight):
        self.width = availWidth
        return availWidth, self.height

    def draw(self):
        x = 0
        self.canv.setStrokeColorRGB(0, 0, 0)
        self.canv.setFillColorRGB(0, 0, 0)
        self.canv.setFont("LibSans", 9)
        for lab in self.labels:
            self.canv.rect(x, 4, 9, 9, stroke=1, fill=0)
            self.canv.drawString(x + 14, 5, lab)
            x += 14 + self.canv.stringWidth(lab, "LibSans", 9) + 18


def register_fonts():
    pdfmetrics.registerFont(TTFont("LibSerif", str(FONT_DIR / "LiberationSerif-Regular.ttf")))
    pdfmetrics.registerFont(TTFont("LibSerif-Bold", str(FONT_DIR / "LiberationSerif-Bold.ttf")))
    pdfmetrics.registerFont(TTFont("LibSerif-Italic", str(FONT_DIR / "LiberationSerif-Italic.ttf")))
    pdfmetrics.registerFont(TTFont("LibSerif-BoldItalic", str(FONT_DIR / "LiberationSerif-BoldItalic.ttf")))
    pdfmetrics.registerFont(TTFont("LibSans", str(FONT_DIR / "LiberationSans-Regular.ttf")))
    pdfmetrics.registerFont(TTFont("LibSans-Bold", str(FONT_DIR / "LiberationSans-Bold.ttf")))
    # Replace reportlab Standard 14 stubs so Helvetica is never unembedded
    pdfmetrics.registerFont(TTFont("Helvetica", str(FONT_DIR / "LiberationSans-Regular.ttf")))
    pdfmetrics.registerFont(TTFont("Helvetica-Bold", str(FONT_DIR / "LiberationSans-Bold.ttf")))
    pdfmetrics.registerFontFamily(
        "LibSerif",
        normal="LibSerif",
        bold="LibSerif-Bold",
        italic="LibSerif-Italic",
        boldItalic="LibSerif-BoldItalic",
    )


def styles():
    s = getSampleStyleSheet()
    s.add(ParagraphStyle(name="Body", fontName="LibSerif", fontSize=11, leading=15, alignment=TA_JUSTIFY, spaceAfter=9))
    s.add(ParagraphStyle(name="BodyCenter", fontName="LibSerif", fontSize=11, leading=15, alignment=TA_CENTER, spaceAfter=8))
    s.add(ParagraphStyle(name="H1", fontName="LibSerif-Bold", fontSize=18, leading=22, alignment=TA_CENTER, spaceBefore=12, spaceAfter=14))
    s.add(ParagraphStyle(name="H2", fontName="LibSans-Bold", fontSize=12, leading=15, spaceBefore=10, spaceAfter=6))
    s.add(ParagraphStyle(name="H3", fontName="LibSans-Bold", fontSize=11, leading=13, spaceBefore=8, spaceAfter=4))
    s.add(ParagraphStyle(name="Label", fontName="LibSans-Bold", fontSize=9, leading=11, spaceBefore=8, spaceAfter=4))
    s.add(ParagraphStyle(name="Quote", fontName="LibSerif-Italic", fontSize=10.5, leading=14, leftIndent=12, rightIndent=12, spaceBefore=8, spaceAfter=4))
    s.add(ParagraphStyle(name="Attr", fontName="LibSans", fontSize=8, leading=10, alignment=TA_RIGHT, rightIndent=12, spaceAfter=10))
    s.add(ParagraphStyle(name="Small", fontName="LibSerif", fontSize=9, leading=11.5, alignment=TA_JUSTIFY, spaceAfter=4))
    s.add(ParagraphStyle(name="BodyBullet", fontName="LibSerif", fontSize=10.5, leading=14, leftIndent=14, spaceAfter=4))
    s.add(ParagraphStyle(name="Orient", fontName="LibSerif-Italic", fontSize=10.5, leading=14, spaceAfter=10))
    s.add(ParagraphStyle(name="Footer", fontName="LibSans", fontSize=8, leading=10))
    s.add(ParagraphStyle(name="HalfTitle", fontName="LibSerif-Bold", fontSize=22, leading=28, alignment=TA_CENTER))
    s.add(ParagraphStyle(name="TitleMain", fontName="LibSerif-Bold", fontSize=20, leading=24, alignment=TA_CENTER, spaceAfter=10))
    s.add(ParagraphStyle(name="SubTitle", fontName="LibSerif-Italic", fontSize=11, leading=14, alignment=TA_CENTER, spaceAfter=18))
    return s


def esc(t: str) -> str:
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    # Flatten markdown emphasis — nested */** breaks reportlab's tag stack
    t = re.sub(r"\*{1,3}([^*]+)\*{1,3}", r"<b>\1</b>", t)
    t = t.replace("*", "")
    t = re.sub(r"`([^`]+)`", r"<font face='LibSans' size='9'>\1</font>", t)
    return t


def odd_frame():
    # odd pages: gutter on left
    return Frame(GUTTER, BOTTOM, PAGE_W - GUTTER - OUTER, PAGE_H - TOP - BOTTOM, id="odd")


def even_frame():
    # even pages: gutter on right
    return Frame(OUTER, BOTTOM, PAGE_W - GUTTER - OUTER, PAGE_H - TOP - BOTTOM, id="even")


class BookDoc(BaseDocTemplate):
    def __init__(self, path: str):
        super().__init__(
            path,
            pagesize=(PAGE_W, PAGE_H),
            title="Stoic Shadow Work Journal",
            author="UnlovedProductions",
        )
        self.front_mode = True
        self.body_started = False
        odd = PageTemplate(id="Odd", frames=[odd_frame()], onPage=self._on_odd)
        even = PageTemplate(id="Even", frames=[even_frame()], onPage=self._on_even)
        self.addPageTemplates([odd, even])

    def _footer(self, canv, doc, page_label: str):
        canv.saveState()
        canv.setFont("LibSans", 8)
        canv.setFillColorRGB(0.2, 0.2, 0.2)
        y = 0.38 * IN
        if doc.page % 2 == 1:
            canv.drawRightString(PAGE_W - OUTER, y, page_label)
            canv.drawString(GUTTER, y, "The Stoic Collection")
        else:
            canv.drawString(OUTER, y, page_label)
            canv.drawRightString(PAGE_W - GUTTER, y, "Stoic Shadow Work Journal")
        canv.restoreState()

    def _on_odd(self, canv, doc):
        if doc.page <= 8 and self.front_mode:
            # roman later via counter — front matter pages 1-8 show roman if we track
            label = self._roman_or_arabic(doc)
        else:
            label = self._roman_or_arabic(doc)
        if not getattr(doc, "suppress_footer", False):
            self._footer(canv, doc, label)

    def _on_even(self, canv, doc):
        if not getattr(doc, "suppress_footer", False):
            self._footer(canv, doc, self._roman_or_arabic(doc))

    def _roman_or_arabic(self, doc):
        # Pages 1-8 of PDF = front matter roman; then arabic from 1
        if doc.page <= 8:
            romans = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii"]
            return romans[doc.page - 1]
        return str(doc.page - 8)


def next_spread():
    """Ensure we alternate templates; BaseDocTemplate handles odd/even via page number if we switch."""
    return []


def parse_manuscript(text: str) -> list[tuple[str, str]]:
    """Return list of (page_title, body) for ## Page sections."""
    # Strip YAML-ish header before first # FRONT or ## Page i
    parts = re.split(r"\n(?=## Page )", text)
    pages = []
    for part in parts:
        if not part.strip().startswith("## Page "):
            continue
        lines = part.strip().splitlines()
        title = lines[0].replace("## ", "").strip()
        body = "\n".join(lines[1:]).strip()
        # Drop production-only end notes section pages after End leaf content still OK
        pages.append((title, body))
    return pages


def md_table_to_flowables(block: str, sty) -> list:
    rows = []
    for line in block.strip().splitlines():
        if re.match(r"^\|?\s*-+", line):
            continue
        if "|" not in line:
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        rows.append([Paragraph(esc(c), sty["Small"]) for c in cells])
    if not rows:
        return []
    col_n = max(len(r) for r in rows)
    for r in rows:
        while len(r) < col_n:
            r.append(Paragraph("", sty["Small"]))
    tw = PAGE_W - GUTTER - OUTER - 4
    col_w = tw / col_n
    t = Table(rows, colWidths=[col_w] * col_n)
    t.setStyle(
        TableStyle(
            [
                ("GRID", (0, 0), (-1, -1), 0.4, (0.4, 0.4, 0.4)),
                ("BACKGROUND", (0, 0), (-1, 0), (0.92, 0.92, 0.92)),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ]
        )
    )
    return [Spacer(1, 6), t, Spacer(1, 8)]


def body_to_flowables(body: str, sty) -> list:
    flow = []
    lines = body.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        raw = line.rstrip()
        if not raw:
            i += 1
            continue
        if raw.startswith("```") or raw.startswith("---"):
            i += 1
            continue
        if raw.startswith("# "):
            flow.append(Paragraph(esc(raw[2:].strip()), sty["H1"]))
            i += 1
            continue
        if raw.startswith("### "):
            flow.append(Paragraph(esc(raw[4:].strip()), sty["H3"]))
            i += 1
            continue
        if raw.startswith("## "):
            flow.append(Paragraph(esc(raw[3:].strip()), sty["H2"]))
            i += 1
            continue
        if raw.startswith("> "):
            quote_lines = []
            while i < len(lines) and lines[i].startswith(">"):
                q = lines[i].lstrip("> ").strip()
                if q:
                    quote_lines.append(q)
                i += 1
            # last line often attribution
            if quote_lines and quote_lines[-1].startswith("—"):
                attr = quote_lines.pop()
                flow.append(Paragraph(esc(" ".join(quote_lines)), sty["Quote"]))
                flow.append(Paragraph(esc(attr), sty["Attr"]))
            else:
                flow.append(Paragraph(esc(" ".join(quote_lines)), sty["Quote"]))
            continue
        if raw.startswith("|"):
            block = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                block.append(lines[i])
                i += 1
            flow.extend(md_table_to_flowables("\n".join(block), sty))
            continue
        if re.match(r"^[-*] ", raw) or re.match(r"^\d+\. ", raw):
            text = re.sub(r"^[-*]\s+", "", raw)
            text = re.sub(r"^\d+\.\s+", "", text)
            flow.append(Paragraph("• " + esc(text), sty["BodyBullet"]))
            i += 1
            continue
        # handwriting underscore blocks
        if set(raw) <= {"_", " "} and len(raw) > 10:
            n = 1
            i += 1
            while i < len(lines) and set(lines[i].strip() or "x") <= {"_"}:
                n += 1
                i += 1
            # Workbook: expand write-in for hand use (MDS usability)
            n = max(n + 2, min(n * 2, 14))
            flow.append(WriteLines(n, gap=18))
            flow.append(Spacer(1, 6))
            continue
        if raw.startswith("**After this chapter"):
            flow.append(Paragraph(esc(raw), sty["Orient"]))
            i += 1
            continue
        if "PROGRESS MARK" in raw.upper() and raw.startswith("###"):
            flow.append(Paragraph("PROGRESS MARK", sty["Label"]))
            flow.append(CheckLine(["I did the reading", "I wrote the incident", "I set the commitment"]))
            flow.append(Spacer(1, 6))
            i += 1
            continue
        if raw.startswith("☐"):
            i += 1
            continue
        # field prompts with underscores on same conceptual page
        if re.search(r"_{5,}", raw):
            label = re.sub(r"_+", "", raw).strip()
            if label:
                flow.append(Paragraph(esc(label), sty["Body"]))
            flow.append(WriteLines(3, gap=18))
            i += 1
            continue
        # Soft page break cues before major exercise blocks
        if raw.startswith("### ") and any(
            k in raw.upper()
            for k in (
                "PRACTICE COMMITMENT",
                "HIDDEN PATTERN",
                "AVOIDANCE MAP",
                "SELF-DECEPTION",
                "CONTROL SORT",
                "VIRTUE MIRROR",
                "CHARACTER AUDIT",
                "PERSONAL STANDARD",
                "ASSENT PAUSE",
                "PATTERN NAME",
                "DRIVER MAP",
            )
        ):
            flow.append(PageBreak())
            flow.append(Paragraph(esc(raw[4:].strip()), sty["Label"]))
            i += 1
            continue
        flow.append(
            Paragraph(
                esc(raw),
                sty["Small"]
                if raw.startswith("**What this")
                or raw.startswith("**If you need")
                or raw.startswith("- Not ")
                else sty["Body"],
            )
        )
        i += 1
    return flow


def page_span(title: str) -> int:
    m = re.search(r"Pages?\s+(\d+)\s*[–-]\s*(\d+)", title, re.I)
    if m:
        a, b = int(m.group(1)), int(m.group(2))
        return max(1, b - a + 1)
    heavy = (
        "PRACTICE",
        "LOG",
        "MAP",
        "AUDIT",
        "CARD",
        "SORT",
        "PAUSE",
        "MIRROR",
        "INTERROGATION",
        "COMMITMENT",
        "DIAGNOSTIC",
        "RE-ENTRY",
        "NOTES",
        "BASELINE",
        "DRIVER",
    )
    if any(h in title.upper() for h in heavy):
        return 2
    if "Lesson" in title or "lesson" in title:
        return 2
    return 1


def build():
    register_fonts()
    sty = styles()
    text = MS_PATH.read_text(encoding="utf-8")
    text = re.split(r"\n# MANUSCRIPT PRODUCTION NOTES", text)[0]
    pages = parse_manuscript(text)
    if not pages:
        raise SystemExit("No pages parsed from manuscript")

    out = OUT_DIR / "Stoic_Shadow_Work_Journal_Book2_INTERIOR.pdf"
    doc = BookDoc(str(out))
    story = []
    story.append(NextPageTemplate("Odd"))

    for idx, (title, body) in enumerate(pages):
        if idx > 0:
            story.append(PageBreak())
            if (idx + 1) % 2 == 1:
                story.append(NextPageTemplate("Odd"))
            else:
                story.append(NextPageTemplate("Even"))

        if "Half-Title" in title:
            story.append(Spacer(1, 2.2 * IN))
            story.append(Paragraph("STOIC SHADOW WORK JOURNAL", sty["HalfTitle"]))
            continue
        if "Title Page" in title:
            story.append(Spacer(1, 1.5 * IN))
            story.append(Paragraph("STOIC SHADOW WORK JOURNAL", sty["TitleMain"]))
            story.append(
                Paragraph(
                    "A Guided Journey Through Self-Reflection, Virtue &amp; Personal Growth",
                    sty["SubTitle"],
                )
            )
            story.append(Paragraph("The Stoic Collection — Book 2", sty["BodyCenter"]))
            story.append(Spacer(1, 0.8 * IN))
            story.append(Paragraph("UnlovedProductions", sty["BodyCenter"]))
            continue

        story.append(Paragraph(esc(title), sty["Label"]))
        story.append(HRFlowable(width="100%", thickness=0.6, color=(0.2, 0.2, 0.2), spaceAfter=8))
        story.extend(body_to_flowables(body, sty))

        span = page_span(title)
        for _extra in range(1, span):
            story.append(PageBreak())
            story.append(Paragraph(esc(f"{title} (continued)"), sty["Label"]))
            story.append(HRFlowable(width="100%", thickness=0.4, color=(0.5, 0.5, 0.5), spaceAfter=8))
            story.append(Paragraph("Continued writing space for this section.", sty["Orient"]))
            story.append(WriteLines(18, gap=18))

    doc.build(story)

    from pypdf import PdfReader, PdfWriter
    from reportlab.pdfgen import canvas

    reader = PdfReader(str(out))
    n = len(reader.pages)
    print(f"Initial page count: {n}")

    TARGET_MIN = 116
    while n < TARGET_MIN:
        blank = OUT_DIR / "_extra.pdf"
        c = canvas.Canvas(str(blank), pagesize=(PAGE_W, PAGE_H))
        odd = (n + 1) % 2 == 1
        left = GUTTER if odd else OUTER
        right = PAGE_W - (OUTER if odd else GUTTER)
        c.setFont("LibSerif-Bold", 11)
        c.drawString(left, PAGE_H - TOP - 10, "PRACTICE LOG")
        c.setFont("LibSerif", 9)
        c.drawString(
            left,
            PAGE_H - TOP - 28,
            "Date: ____________________   Pattern / cue: _______________________________",
        )
        y = PAGE_H - TOP - 50
        c.setStrokeColorRGB(0.35, 0.35, 0.35)
        c.setLineWidth(0.4)
        while y > BOTTOM + 20:
            c.line(left, y, right, y)
            y -= 18
        c.setFont("LibSans", 8)
        label = str(n + 1 - 8) if n + 1 > 8 else ""
        c.drawCentredString(PAGE_W / 2, 0.38 * IN, label)
        c.showPage()
        c.save()
        writer = PdfWriter()
        for p in reader.pages:
            writer.add_page(p)
        writer.add_page(PdfReader(str(blank)).pages[0])
        with open(out, "wb") as f:
            writer.write(f)
        blank.unlink(missing_ok=True)
        reader = PdfReader(str(out))
        n = len(reader.pages)

    if n % 2 == 1:
        blank = OUT_DIR / "_blank.pdf"
        c = canvas.Canvas(str(blank), pagesize=(PAGE_W, PAGE_H))
        c.showPage()
        c.save()
        writer = PdfWriter()
        for p in reader.pages:
            writer.add_page(p)
        writer.add_page(PdfReader(str(blank)).pages[0])
        with open(out, "wb") as f:
            writer.write(f)
        blank.unlink(missing_ok=True)
        n += 1
        print(f"Padded to even: {n}")

    if n > 124:
        print(f"WARNING: {n} pages exceeds MDS band 116–124; consider tightening write-in.")

    meta = OUT_DIR / "interior_page_count.txt"
    meta.write_text(f"{n}\n", encoding="utf-8")
    print(f"Wrote {out} ({n} pages)")
    return out, n


if __name__ == "__main__":
    build()
