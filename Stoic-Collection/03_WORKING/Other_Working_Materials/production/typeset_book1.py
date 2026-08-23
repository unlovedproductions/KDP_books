#!/usr/bin/env python3
"""Typeset Book 1 interior to KDP 6x9 B&W no-bleed PDF.

House stack matches Book 2 (Liberation + reportlab). Reads the Approved
manuscript. Does not overwrite Book 2 outputs.
"""

from __future__ import annotations

import re
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_RIGHT
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch as IN
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import (
    BaseDocTemplate,
    Flowable,
    Frame,
    HRFlowable,
    KeepInFrame,
    NextPageTemplate,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

PROD = Path(__file__).resolve().parent
COLLECTION = Path(__file__).resolve().parents[3]
MS_PATH = (
    COLLECTION
    / "02_APPROVED"
    / "Manuscripts"
    / "BOOK 1 — STOIC FOUNDATIONS — MANUSCRIPT.md"
)
OUT_DIR = PROD / "output"
FONT_DIR = PROD / "fonts"
COUNT_FILE = OUT_DIR / "book1_interior_page_count.txt"
OUT_PDF = OUT_DIR / "Stoic_Foundations_Book1_INTERIOR.pdf"

PAGE_W, PAGE_H = 6 * IN, 9 * IN
GUTTER = 0.75 * IN
OUTER = 0.60 * IN
TOP = 0.60 * IN
BOTTOM = 0.65 * IN

TARGET = 120
BAND_MIN = 116
BAND_MAX = 124

STRUCT_H1 = re.compile(
    r"^# (CHAPTER |INTRODUCTION|FRONT MATTER|STOIC TERMINOLOGY|"
    r"SOURCES|FURTHER READING|THE STOIC COLLECTION|END OF BOOK)"
)


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
    pdfmetrics.registerFont(
        TTFont("LibSerif-BoldItalic", str(FONT_DIR / "LiberationSerif-BoldItalic.ttf"))
    )
    pdfmetrics.registerFont(TTFont("LibSans", str(FONT_DIR / "LiberationSans-Regular.ttf")))
    pdfmetrics.registerFont(TTFont("LibSans-Bold", str(FONT_DIR / "LiberationSans-Bold.ttf")))
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
    s.add(
        ParagraphStyle(
            name="Body",
            fontName="LibSerif",
            fontSize=11,
            leading=14,
            alignment=TA_JUSTIFY,
            spaceAfter=8,
        )
    )
    s.add(
        ParagraphStyle(
            name="BodyCenter",
            fontName="LibSerif",
            fontSize=11,
            leading=15,
            alignment=TA_CENTER,
            spaceAfter=8,
        )
    )
    s.add(
        ParagraphStyle(
            name="H1",
            fontName="LibSerif-Bold",
            fontSize=18,
            leading=22,
            alignment=TA_CENTER,
            spaceBefore=12,
            spaceAfter=14,
        )
    )
    s.add(
        ParagraphStyle(
            name="H2",
            fontName="LibSans-Bold",
            fontSize=12,
            leading=15,
            spaceBefore=10,
            spaceAfter=6,
        )
    )
    s.add(
        ParagraphStyle(
            name="H3",
            fontName="LibSans-Bold",
            fontSize=11,
            leading=13,
            spaceBefore=8,
            spaceAfter=4,
        )
    )
    s.add(
        ParagraphStyle(
            name="Label",
            fontName="LibSans-Bold",
            fontSize=9,
            leading=11,
            spaceBefore=8,
            spaceAfter=4,
        )
    )
    s.add(
        ParagraphStyle(
            name="Quote",
            fontName="LibSerif-Italic",
            fontSize=10.5,
            leading=14,
            leftIndent=12,
            rightIndent=12,
            spaceBefore=8,
            spaceAfter=4,
        )
    )
    s.add(
        ParagraphStyle(
            name="Attr",
            fontName="LibSans",
            fontSize=8,
            leading=10,
            alignment=TA_RIGHT,
            rightIndent=12,
            spaceAfter=10,
        )
    )
    s.add(
        ParagraphStyle(
            name="Small",
            fontName="LibSerif",
            fontSize=9,
            leading=11.5,
            alignment=TA_JUSTIFY,
            spaceAfter=4,
        )
    )
    s.add(
        ParagraphStyle(
            name="BodyBullet",
            fontName="LibSerif",
            fontSize=10.5,
            leading=14,
            leftIndent=14,
            spaceAfter=4,
        )
    )
    s.add(
        ParagraphStyle(
            name="Orient",
            fontName="LibSerif-Italic",
            fontSize=10.5,
            leading=14,
            spaceAfter=10,
        )
    )
    s.add(
        ParagraphStyle(
            name="HalfTitle",
            fontName="LibSerif-Bold",
            fontSize=22,
            leading=28,
            alignment=TA_CENTER,
        )
    )
    s.add(
        ParagraphStyle(
            name="TitleMain",
            fontName="LibSerif-Bold",
            fontSize=20,
            leading=24,
            alignment=TA_CENTER,
            spaceAfter=10,
        )
    )
    s.add(
        ParagraphStyle(
            name="SubTitle",
            fontName="LibSerif-Italic",
            fontSize=11,
            leading=14,
            alignment=TA_CENTER,
            spaceAfter=18,
        )
    )
    return s


def esc(t: str) -> str:
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    t = re.sub(r"\*{1,3}([^*]+)\*{1,3}", r"<b>\1</b>", t)
    t = t.replace("*", "")
    t = re.sub(r"`([^`]+)`", r"<font face='LibSans' size='9'>\1</font>", t)
    return t


def odd_frame():
    return Frame(GUTTER, BOTTOM, PAGE_W - GUTTER - OUTER, PAGE_H - TOP - BOTTOM, id="odd")


def even_frame():
    return Frame(OUTER, BOTTOM, PAGE_W - GUTTER - OUTER, PAGE_H - TOP - BOTTOM, id="even")


class BookDoc(BaseDocTemplate):
    def __init__(self, path: str):
        super().__init__(
            path,
            pagesize=(PAGE_W, PAGE_H),
            title="Stoic Foundations",
            author="UnlovedProductions",
        )
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
            canv.drawRightString(PAGE_W - GUTTER, y, "Stoic Foundations")
        canv.restoreState()

    def _on_odd(self, canv, doc):
        self._footer(canv, doc, self._roman_or_arabic(doc))

    def _on_even(self, canv, doc):
        self._footer(canv, doc, self._roman_or_arabic(doc))

    def _roman_or_arabic(self, doc):
        if doc.page <= 8:
            romans = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii"]
            return romans[doc.page - 1]
        return str(doc.page - 8)


def is_wrapper(title: str) -> bool:
    t = title.strip()
    return bool(re.match(r"^Pages?\s+\d+\s*[–-]\s*\d+\s*(·.*)?$", t) and " — " not in t)


def is_write_in_span(title: str) -> bool:
    u = title.upper()
    keys = (
        "LESSON",
        "PROMPT",
        "CARD",
        "COMMITMENT",
        "CAPTURE",
        "SPLIT",
        "CONTROL SORT",
        "ASSENT PAUSE",
        "VIRTUE MIRROR",
        "EVENING EXAMINATION",
        "RE-ENTRY",
        "BASELINE",
        "OVERFLOW",
        "L1",
        "L2",
        "L4",
        "L5",
        "BRIDGE",
        "EXAM",
    )
    return any(k in u for k in keys)


def page_span(title: str) -> int:
    m = re.search(r"Pages?\s+(\d+)\s*[–-]\s*(\d+)", title, re.I)
    if not m:
        return 1
    if not is_write_in_span(title):
        return 1
    a, b = int(m.group(1)), int(m.group(2))
    return max(1, b - a + 1)


# First unique body hit after front matter (PDF pages 1–8). Not TOC labels.
TOC_NEEDLES = (
    ("Introduction: The Work Begins Here", "finishable program that installs"),
    ("1. Start With the Method", "Chapter 1 Start With the Method"),
    ("2. What Hits the Mind", "Chapter 2 What Hits the Mind"),
    ("3. Facts and Additions", "Chapter 3 Facts and Additions"),
    ("4. Up to You", "Chapter 4 Up to You"),
    ("5. Before You Assent", "Chapter 5 Before You Assent"),
    ("6. Ownership Without Abuse", "Chapter 6 Ownership Without Abuse"),
    ("7. Virtue Tests the Next Act", "Chapter 7 Virtue Tests the Next Act"),
    ("8. Review Until It Is Ordinary", "Chapter 8 Review Until It Is Ordinary"),
    ("Integration: A Standard You Can Carry", "Completion here does not mean you have finished Stoicism"),
    ("Stoic Terminology & Concepts Guide", "This guide defines terms used in this book in plain language"),
    ("Sources & Citations", "On-page quotes include author, work, section, translator"),
    ("Further Reading", "Read these after this book if you want the pages behind the quotes"),
    ("The Stoic Collection", "No speculative later catalog"),
)


def patch_toc(text: str, arabic: dict[str, int]) -> str:
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    in_toc = False
    for line in lines:
        if line.startswith("## Page viii — Contents"):
            in_toc = True
        elif in_toc and line.startswith("## "):
            in_toc = False
        if in_toc and line.lstrip().startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) >= 2 and cells[0] in arabic:
                nl = "\n" if line.endswith("\n") else ""
                line = f"| {cells[0]} | {arabic[cells[0]]} |{nl}"
        out.append(line)
    return "".join(out)


def measure_toc(pdf_path: Path) -> dict[str, int]:
    reader = PdfReader(str(pdf_path))
    remaining = list(TOC_NEEDLES)
    found: dict[str, int] = {}
    for i, page in enumerate(reader.pages):
        if i < 8:
            continue
        blob = re.sub(r"\s+", " ", page.extract_text() or "")
        still = []
        for label, needle in remaining:
            if needle in blob:
                found[label] = i + 1 - 8
            else:
                still.append((label, needle))
        remaining = still
        if not remaining:
            break
    if remaining:
        missing = ", ".join(label for label, _ in remaining)
        raise SystemExit(f"TOC anchors not found in interior PDF: {missing}")
    return found


FRAME_W = PAGE_W - GUTTER - OUTER
FRAME_H = PAGE_H - TOP - BOTTOM


def parse_manuscript(text: str) -> list[tuple[str, str]]:
    parts = re.split(r"\n(?=## Pages? )", text)
    pages = []
    for part in parts:
        if not re.match(r"^## Pages? ", part.strip()):
            continue
        lines = part.strip().splitlines()
        title = lines[0].replace("## ", "").strip()
        if is_wrapper(title):
            continue
        body_lines = []
        for line in lines[1:]:
            if STRUCT_H1.match(line.strip()):
                continue
            body_lines.append(line)
        pages.append((title, "\n".join(body_lines).strip()))
    return pages


def md_table_to_flowables(block: str, sty) -> list:
    rows = []
    for line in block.strip().splitlines():
        if re.match(r"^\|?\s*-+", line):
            continue
        if "|" not in line:
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        rows.append([Paragraph(esc(c) if c else " ", sty["Small"]) for c in cells])
    if not rows:
        return []
    col_n = max(len(r) for r in rows)
    for r in rows:
        while len(r) < col_n:
            r.append(Paragraph(" ", sty["Small"]))
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
                ("TOPPADDING", (0, 0), (-1, 0), 3),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 3),
                ("TOPPADDING", (0, 1), (-1, -1), 10),
                ("BOTTOMPADDING", (0, 1), (-1, -1), 10),
            ]
        )
    )
    return [Spacer(1, 6), t, Spacer(1, 8)]


def body_to_flowables(body: str, sty, compact: bool) -> list:
    flow = []
    lines = body.splitlines()
    i = 0
    body_style = sty["Small"] if compact else sty["Body"]
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
            label = raw[4:].strip()
            if "PROGRESS MARK" in label.upper():
                flow.append(Paragraph("PROGRESS MARK", sty["Label"]))
                flow.append(
                    CheckLine(["I did the reading", "I wrote the incident", "I set the commitment"])
                )
                flow.append(Spacer(1, 6))
                i += 1
                continue
            flow.append(Paragraph(esc(label), sty["H3"]))
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
        if set(raw) <= {"_", " "} and len(raw) > 10:
            n = 1
            i += 1
            while i < len(lines) and set(lines[i].strip() or "x") <= {"_"}:
                n += 1
                i += 1
            n = max(n, 2) if compact else max(n + 2, min(n * 2, 14))
            flow.append(WriteLines(n, gap=16 if compact else 18))
            flow.append(Spacer(1, 6))
            continue
        if raw.startswith("**After this chapter"):
            flow.append(Paragraph(esc(raw), sty["Orient"]))
            i += 1
            continue
        if raw.startswith("☐"):
            i += 1
            continue
        if re.search(r"_{5,}", raw):
            label = re.sub(r"_+", "", raw).strip()
            if label:
                flow.append(Paragraph(esc(label), body_style))
            flow.append(WriteLines(1 if compact else 3, gap=16 if compact else 18))
            i += 1
            continue
        flow.append(Paragraph(esc(raw), body_style))
        i += 1
    return flow


def _append_write_in_page(writer: PdfWriter, n: int, kind: str) -> int:
    blank = OUT_DIR / "_extra_book1.pdf"
    c = canvas.Canvas(str(blank), pagesize=(PAGE_W, PAGE_H))
    odd = (n + 1) % 2 == 1
    left = GUTTER if odd else OUTER
    right = PAGE_W - (OUTER if odd else GUTTER)
    register_fonts()
    if kind == "sort":
        title = "CONTROL SORT (continued)"
        note = "Ordinary incident. My share is a teaching aid, not a third classical category."
        headers = "Up to me                 Not up to me                 My share"
    else:
        title = "EVENING EXAMINATION (continued)"
        note = "Series form. Inspired by the examination tradition — not an ancient worksheet."
        headers = "1. Impression / what I added     2. Up to me / my share     3. Tomorrow's one act"
    c.setFont("LibSans-Bold", 10)
    c.drawString(left, PAGE_H - TOP - 10, title)
    c.setFont("LibSerif", 9)
    c.drawString(left, PAGE_H - TOP - 26, note)
    c.setFont("LibSans", 8)
    c.drawString(left, PAGE_H - TOP - 42, headers)
    y = PAGE_H - TOP - 60
    c.setStrokeColorRGB(0.35, 0.35, 0.35)
    c.setLineWidth(0.4)
    while y > BOTTOM + 20:
        c.line(left, y, right, y)
        y -= 18
    c.setFont("LibSans", 8)
    label = str(n + 1 - 8) if n + 1 > 8 else ""
    if (n + 1) % 2 == 1:
        c.drawRightString(PAGE_W - OUTER, 0.38 * IN, label)
        c.drawString(GUTTER, 0.38 * IN, "The Stoic Collection")
    else:
        c.drawString(OUTER, 0.38 * IN, label)
        c.drawRightString(PAGE_W - GUTTER, 0.38 * IN, "Stoic Foundations")
    c.showPage()
    c.save()
    writer.add_page(PdfReader(str(blank)).pages[0])
    blank.unlink(missing_ok=True)
    return n + 1


def _append_blank(writer: PdfWriter, n: int) -> int:
    blank = OUT_DIR / "_blank_book1.pdf"
    c = canvas.Canvas(str(blank), pagesize=(PAGE_W, PAGE_H))
    c.showPage()
    c.save()
    writer.add_page(PdfReader(str(blank)).pages[0])
    blank.unlink(missing_ok=True)
    return n + 1


def build(ms_text: str | None = None):
    register_fonts()
    sty = styles()
    text = ms_text if ms_text is not None else MS_PATH.read_text(encoding="utf-8")
    pages = parse_manuscript(text)
    if not pages:
        raise SystemExit("No pages parsed from manuscript")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    doc = BookDoc(str(OUT_PDF))
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
            story.append(Paragraph("STOIC FOUNDATIONS", sty["HalfTitle"]))
            continue
        if "Title Page" in title:
            story.append(Spacer(1, 1.5 * IN))
            story.append(Paragraph("STOIC FOUNDATIONS", sty["TitleMain"]))
            story.append(
                Paragraph(
                    "A Guided Workbook on Judgment, Control, and Assent",
                    sty["SubTitle"],
                )
            )
            story.append(Paragraph("The Stoic Collection — Book 1", sty["BodyCenter"]))
            story.append(Spacer(1, 0.8 * IN))
            story.append(Paragraph("UnlovedProductions", sty["BodyCenter"]))
            continue
        if "End leaf" in title:
            continue

        compact = any(
            k in title.upper()
            for k in (
                "COPYRIGHT",
                "CONTENTS",
                "HOW TO USE",
                "OUTCOME MAP",
                "RE-ENTRY",
            )
        )
        flow = body_to_flowables(body, sty, compact)
        if compact or "Opening" in title or "PRINCIPLE" in title or title.endswith("Close"):
            story.append(KeepInFrame(FRAME_W, FRAME_H - 4, flow, mode="shrink", hAlign="LEFT"))
        else:
            story.extend(flow)

        span = page_span(title)
        for _extra in range(1, span):
            story.append(PageBreak())
            story.append(Paragraph(esc(f"{title} (continued)"), sty["Label"]))
            story.append(HRFlowable(width="100%", thickness=0.4, color=(0.5, 0.5, 0.5), spaceAfter=8))
            story.append(WriteLines(16, gap=18))

    doc.build(story)

    reader = PdfReader(str(OUT_PDF))
    n = len(reader.pages)
    print(f"Initial page count: {n}")

    writer = PdfWriter()
    for p in reader.pages:
        writer.add_page(p)

    pad_kind = "sort"
    while n < BAND_MIN:
        n = _append_write_in_page(writer, n, pad_kind)
        pad_kind = "exam" if pad_kind == "sort" else "sort"
    while n < TARGET and n % 2 == 1:
        n = _append_write_in_page(writer, n, pad_kind)

    if n % 2 == 1:
        n = _append_blank(writer, n)
        print(f"Padded to even: {n}")

    with open(OUT_PDF, "wb") as f:
        writer.write(f)

    if n > BAND_MAX:
        print(f"WARNING: {n} pages exceeds MDS band {BAND_MIN}–{BAND_MAX}")
    elif n < BAND_MIN:
        print(f"WARNING: {n} pages below MDS band {BAND_MIN}–{BAND_MAX}")

    COUNT_FILE.write_text(f"{n}\n", encoding="utf-8")
    print(f"Wrote {OUT_PDF} ({n} pages)")
    return OUT_PDF, n


def build_with_printed_toc():
    source = MS_PATH.read_text(encoding="utf-8")
    build(source)
    nums = measure_toc(OUT_PDF)
    patched = patch_toc(source, nums)
    if patched == source:
        print("TOC already matches printed arabic pages")
        return OUT_PDF
    print("TOC arabic:", nums)
    build(patched)
    nums2 = measure_toc(OUT_PDF)
    if nums2 != nums:
        print("TOC shifted after patch; second pass", nums2)
        build(patch_toc(source, nums2))
    return OUT_PDF


if __name__ == "__main__":
    build_with_printed_toc()
