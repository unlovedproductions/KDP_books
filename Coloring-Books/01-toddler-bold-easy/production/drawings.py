"""100 unique toddler coloring drawings: closed black stroke, no fill, no shading."""

from __future__ import annotations

from math import atan2, cos, degrees, hypot, radians, sin

from reportlab.pdfgen.canvas import Canvas

OUTER = 8.0
INNER = 5.0
# Set by the page code to 1/scale so printed stroke widths stay at OUTER/INNER.
STROKE_K = 1.0


def _stroke(c: Canvas, w: float) -> None:
    c.setStrokeColorRGB(0, 0, 0)
    c.setFillColorRGB(1, 1, 1)
    c.setLineWidth(w * STROKE_K)
    c.setLineCap(1)
    c.setLineJoin(1)


def circle(c: Canvas, x: float, y: float, r: float, w: float = OUTER) -> None:
    _stroke(c, w)
    c.circle(x, y, r, stroke=1, fill=1)


def ellipse(c: Canvas, x: float, y: float, rx: float, ry: float, w: float = OUTER) -> None:
    _stroke(c, w)
    c.ellipse(x - rx, y - ry, x + rx, y + ry, stroke=1, fill=1)


def rrect(c: Canvas, x: float, y: float, width: float, height: float, r: float = 12, w: float = OUTER) -> None:
    _stroke(c, w)
    c.roundRect(x, y, width, height, r, stroke=1, fill=1)


def poly(c: Canvas, pts: list[tuple[float, float]], w: float = OUTER, close: bool = True) -> None:
    _stroke(c, w)
    p = c.beginPath()
    p.moveTo(pts[0][0], pts[0][1])
    for px, py in pts[1:]:
        p.lineTo(px, py)
    if close:
        p.close()
    c.drawPath(p, stroke=1, fill=1 if close else 0)


def arc(c: Canvas, x1: float, y1: float, x2: float, y2: float, start: float, extent: float, w: float = OUTER) -> None:
    _stroke(c, w)
    c.arc(x1, y1, x2, y2, start, extent)


def capsule(c: Canvas, x1: float, y1: float, x2: float, y2: float, r: float, w: float = OUTER) -> None:
    """Closed stadium (leg, neck, tail). Never a stick line."""
    _stroke(c, w)
    dx, dy = x2 - x1, y2 - y1
    length = hypot(dx, dy)
    if length < 1:
        circle(c, x1, y1, r, w)
        return
    c.saveState()
    c.setStrokeColorRGB(0, 0, 0)
    c.setFillColorRGB(1, 1, 1)
    c.setLineWidth(w * STROKE_K)
    c.setLineCap(1)
    c.setLineJoin(1)
    c.translate(x1, y1)
    c.rotate(degrees(atan2(dy, dx)))
    c.roundRect(-r, -r, length + 2 * r, 2 * r, r, stroke=1, fill=1)
    c.restoreState()


def face(c: Canvas, x: float, y: float, eye: float = 8, spread: float = 18, smile: bool = True) -> None:
    circle(c, x - spread, y, eye, INNER)
    circle(c, x + spread, y, eye, INNER)
    if smile:
        arc(c, x - 16, y - 22, x + 16, y - 2, 200, 140, INNER)


# --- animals ---

def cat(c, x, y):
    ellipse(c, x - 115, y - 10, 48, 16)
    ellipse(c, x, y - 20, 95, 78)
    ellipse(c, x - 72, y - 70, 30, 38)
    ellipse(c, x + 72, y - 70, 30, 38)
    capsule(c, x - 30, y - 50, x - 30, y - 128, 15)
    capsule(c, x + 30, y - 50, x + 30, y - 128, 15)
    ellipse(c, x - 30, y - 138, 20, 11)
    ellipse(c, x + 30, y - 138, 20, 11)
    circle(c, x, y + 88, 58)
    poly(c, [(x - 48, y + 122), (x - 60, y + 178), (x - 16, y + 138)])
    poly(c, [(x + 48, y + 122), (x + 60, y + 178), (x + 16, y + 138)])
    poly(c, [(x - 44, y + 130), (x - 50, y + 158), (x - 28, y + 138)], INNER)
    poly(c, [(x + 44, y + 130), (x + 50, y + 158), (x + 28, y + 138)], INNER)
    face(c, x, y + 90, 8, 18)
    poly(c, [(x, y + 78), (x - 8, y + 68), (x + 8, y + 68)], INNER)


def dog(c, x, y):
    ellipse(c, x - 120, y - 5, 42, 16)
    ellipse(c, x, y - 15, 105, 72)
    capsule(c, x - 45, y - 50, x - 55, y - 130, 16)
    capsule(c, x - 10, y - 60, x - 8, y - 135, 15)
    capsule(c, x + 25, y - 60, x + 28, y - 135, 15)
    capsule(c, x + 55, y - 50, x + 62, y - 128, 16)
    ellipse(c, x - 55, y - 140, 20, 11)
    ellipse(c, x - 8, y - 144, 18, 10)
    ellipse(c, x + 28, y - 144, 18, 10)
    ellipse(c, x + 62, y - 138, 20, 11)
    circle(c, x + 70, y + 70, 52)
    ellipse(c, x + 42, y + 48, 16, 32)
    ellipse(c, x + 100, y + 48, 16, 32)
    face(c, x + 72, y + 74, 7, 16)
    ellipse(c, x + 78, y + 52, 12, 8, INNER)


def fish(c, x, y):
    ellipse(c, x + 10, y, 125, 62)
    poly(c, [(x - 110, y), (x - 185, y + 58), (x - 160, y), (x - 185, y - 58)])
    poly(c, [(x + 20, y + 60), (x + 55, y + 108), (x + 70, y + 52)])
    poly(c, [(x + 10, y - 58), (x - 10, y - 95), (x + 40, y - 55)])
    circle(c, x + 85, y + 12, 14, INNER)
    circle(c, x + 90, y + 14, 5, INNER)
    ellipse(c, x - 10, y, 28, 18, INNER)
    arc(c, x + 40, y - 18, x + 90, y + 12, 190, 150, INNER)


def bird(c, x, y):
    ellipse(c, x, y, 78, 52)
    circle(c, x + 72, y + 38, 36)
    poly(c, [(x + 100, y + 38), (x + 148, y + 48), (x + 148, y + 22), (x + 100, y + 28)])
    ellipse(c, x - 30, y + 8, 38, 16, INNER)
    capsule(c, x - 12, y - 48, x - 18, y - 100, 8)
    capsule(c, x + 18, y - 48, x + 24, y - 100, 8)
    poly(c, [(x - 18, y - 100), (x - 40, y - 112), (x + 2, y - 108), (x - 8, y - 100)])
    poly(c, [(x + 24, y - 100), (x + 8, y - 108), (x + 48, y - 112), (x + 32, y - 100)])
    circle(c, x + 82, y + 46, 7, INNER)


def duck(c, x, y):
    ellipse(c, x, y - 15, 95, 58)
    circle(c, x + 78, y + 52, 40)
    ellipse(c, x + 118, y + 50, 30, 12)
    circle(c, x + 72, y + 60, 7, INNER)
    ellipse(c, x + 10, y - 55, 70, 22)
    capsule(c, x - 18, y - 70, x - 28, y - 118, 9)
    capsule(c, x + 28, y - 70, x + 38, y - 118, 9)
    poly(c, [(x - 28, y - 118), (x - 50, y - 128), (x - 8, y - 124)])
    poly(c, [(x + 38, y - 118), (x + 18, y - 124), (x + 60, y - 128)])


def frog(c, x, y):
    ellipse(c, x, y, 100, 68)
    circle(c, x - 42, y + 72, 26)
    circle(c, x + 42, y + 72, 26)
    circle(c, x - 42, y + 74, 10, INNER)
    circle(c, x + 42, y + 74, 10, INNER)
    arc(c, x - 28, y - 8, x + 28, y + 22, 200, 140, INNER)
    capsule(c, x - 70, y - 30, x - 105, y - 85, 14)
    capsule(c, x + 70, y - 30, x + 105, y - 85, 14)
    ellipse(c, x - 115, y - 95, 32, 18)
    ellipse(c, x + 115, y - 95, 32, 18)
    capsule(c, x - 40, y - 55, x - 55, y - 100, 12)
    capsule(c, x + 40, y - 55, x + 55, y - 100, 12)
    ellipse(c, x - 58, y - 108, 22, 12)
    ellipse(c, x + 58, y - 108, 22, 12)


def bunny(c, x, y):
    ellipse(c, x, y - 25, 82, 70)
    circle(c, x, y + 72, 48)
    ellipse(c, x - 22, y + 145, 15, 52)
    ellipse(c, x + 22, y + 145, 15, 52)
    ellipse(c, x - 22, y + 140, 8, 32, INNER)
    ellipse(c, x + 22, y + 140, 8, 32, INNER)
    face(c, x, y + 74, 7, 15)
    ellipse(c, x, y + 56, 10, 8, INNER)
    capsule(c, x - 38, y - 70, x - 48, y - 128, 14)
    capsule(c, x + 38, y - 70, x + 48, y - 128, 14)
    ellipse(c, x - 48, y - 136, 20, 11)
    ellipse(c, x + 48, y - 136, 20, 11)
    ellipse(c, x, y - 90, 22, 14)


def bear(c, x, y):
    ellipse(c, x, y - 18, 100, 82)
    circle(c, x, y + 78, 56)
    circle(c, x - 46, y + 118, 20)
    circle(c, x + 46, y + 118, 20)
    face(c, x, y + 82, 8, 18)
    ellipse(c, x, y + 58, 18, 14, INNER)
    capsule(c, x - 50, y - 60, x - 62, y - 128, 16)
    capsule(c, x - 18, y - 75, x - 18, y - 138, 15)
    capsule(c, x + 18, y - 75, x + 18, y - 138, 15)
    capsule(c, x + 50, y - 60, x + 62, y - 128, 16)
    ellipse(c, x - 62, y - 138, 20, 11)
    ellipse(c, x - 18, y - 146, 18, 10)
    ellipse(c, x + 18, y - 146, 18, 10)
    ellipse(c, x + 62, y - 138, 20, 11)


def pig(c, x, y):
    ellipse(c, x, y, 102, 68)
    circle(c, x + 78, y + 42, 46)
    ellipse(c, x + 96, y + 36, 22, 16)
    circle(c, x + 88, y + 36, 5, INNER)
    circle(c, x + 104, y + 36, 5, INNER)
    circle(c, x + 68, y + 56, 7, INNER)
    circle(c, x + 92, y + 58, 7, INNER)
    ellipse(c, x + 52, y + 78, 14, 16)
    ellipse(c, x + 100, y + 80, 14, 16)
    capsule(c, x - 48, y - 48, x - 52, y - 108, 14)
    capsule(c, x - 12, y - 58, x - 10, y - 112, 13)
    capsule(c, x + 28, y - 58, x + 30, y - 112, 13)
    capsule(c, x + 58, y - 48, x + 62, y - 108, 14)
    ellipse(c, x - 130, y, 18, 22)


def cow(c, x, y):
    ellipse(c, x, y - 8, 118, 70)
    circle(c, x + 98, y + 52, 46)
    ellipse(c, x + 100, y + 22, 26, 16)
    circle(c, x + 84, y + 60, 7, INNER)
    circle(c, x + 114, y + 60, 7, INNER)
    capsule(c, x + 72, y + 90, x + 58, y + 118, 7)
    capsule(c, x + 124, y + 90, x + 138, y + 118, 7)
    ellipse(c, x + 52, y + 124, 14, 10)
    ellipse(c, x + 146, y + 124, 14, 10)
    circle(c, x - 20, y + 18, 20, INNER)
    circle(c, x + 22, y - 12, 16, INNER)
    capsule(c, x - 68, y - 55, x - 78, y - 128, 15)
    capsule(c, x - 18, y - 70, x - 14, y - 132, 14)
    capsule(c, x + 28, y - 70, x + 32, y - 132, 14)
    capsule(c, x + 68, y - 52, x + 78, y - 124, 15)


def horse(c, x, y):
    ellipse(c, x, y, 112, 52)
    capsule(c, x + 70, y + 20, x + 95, y + 95, 18)
    ellipse(c, x + 118, y + 108, 38, 22)
    circle(c, x + 140, y + 114, 7, INNER)
    ellipse(c, x + 158, y + 100, 16, 8, INNER)
    capsule(c, x - 48, y - 35, x - 55, y - 128, 14)
    capsule(c, x - 8, y - 48, x - 5, y - 132, 13)
    capsule(c, x + 38, y - 48, x + 42, y - 132, 13)
    capsule(c, x + 75, y - 35, x + 85, y - 124, 14)
    poly(c, [(x - 100, y + 18), (x - 128, y + 85), (x - 108, y + 88), (x - 72, y + 28)])
    ellipse(c, x - 118, y - 8, 22, 10)
    ellipse(c, x + 78, y + 55, 10, 14, INNER)


def sheep(c, x, y):
    circle(c, x - 40, y, 42)
    circle(c, x + 8, y + 28, 40)
    circle(c, x + 52, y - 2, 44)
    circle(c, x - 8, y - 38, 38)
    circle(c, x + 32, y + 38, 34)
    circle(c, x + 95, y + 18, 38)
    circle(c, x + 92, y + 58, 28)
    circle(c, x + 82, y + 62, 7, INNER)
    circle(c, x + 104, y + 62, 7, INNER)
    ellipse(c, x + 94, y + 42, 12, 8, INNER)
    capsule(c, x - 28, y - 55, x - 32, y - 112, 12)
    capsule(c, x + 12, y - 62, x + 16, y - 118, 12)
    capsule(c, x + 48, y - 55, x + 52, y - 112, 12)
    capsule(c, x + 82, y - 42, x + 88, y - 100, 12)


def chick(c, x, y):
    circle(c, x, y + 10, 72)
    circle(c, x + 16, y + 28, 10, INNER)
    poly(c, [(x + 58, y + 12), (x + 102, y + 22), (x + 102, y), (x + 58, y - 4)])
    poly(c, [(x - 18, y + 72), (x, y + 118), (x + 18, y + 72)])
    ellipse(c, x - 48, y + 8, 22, 12, INNER)
    capsule(c, x - 16, y - 58, x - 22, y - 108, 8)
    capsule(c, x + 16, y - 58, x + 22, y - 108, 8)
    poly(c, [(x - 22, y - 108), (x - 44, y - 118), (x - 4, y - 114)])
    poly(c, [(x + 22, y - 108), (x + 4, y - 114), (x + 44, y - 118)])


def owl(c, x, y):
    ellipse(c, x, y, 72, 98)
    circle(c, x - 28, y + 38, 28)
    circle(c, x + 28, y + 38, 28)
    circle(c, x - 28, y + 38, 10, INNER)
    circle(c, x + 28, y + 38, 10, INNER)
    poly(c, [(x, y + 12), (x - 14, y - 8), (x + 14, y - 8)])
    ellipse(c, x - 58, y, 22, 42, INNER)
    ellipse(c, x + 58, y, 22, 42, INNER)
    poly(c, [(x - 22, y + 98), (x - 38, y + 128), (x - 6, y + 108)])
    poly(c, [(x + 22, y + 98), (x + 38, y + 128), (x + 6, y + 108)])
    capsule(c, x - 16, y - 92, x - 22, y - 122, 8)
    capsule(c, x + 16, y - 92, x + 22, y - 122, 8)
    poly(c, [(x - 22, y - 122), (x - 40, y - 132), (x - 6, y - 128)])
    poly(c, [(x + 22, y - 122), (x + 6, y - 128), (x + 40, y - 132)])


def turtle(c, x, y):
    ellipse(c, x, y, 112, 72)
    ellipse(c, x, y, 70, 42, INNER)
    circle(c, x + 128, y + 4, 32)
    circle(c, x + 138, y + 12, 6, INNER)
    ellipse(c, x - 42, y + 82, 28, 16)
    ellipse(c, x + 42, y + 82, 28, 16)
    ellipse(c, x - 42, y - 82, 28, 16)
    ellipse(c, x + 42, y - 82, 28, 16)
    ellipse(c, x - 118, y - 8, 18, 10)
    line_grid = ((-25, 0, 25, 0), (0, -18, 0, 18))
    for x1, y1, x2, y2 in line_grid:
        capsule(c, x + x1, y + y1, x + x2, y + y2, 3, INNER)


def mouse(c, x, y):
    ellipse(c, x, y, 72, 42)
    circle(c, x + 58, y + 28, 30)
    circle(c, x + 38, y + 58, 22)
    circle(c, x + 78, y + 58, 22)
    circle(c, x + 38, y + 58, 10, INNER)
    circle(c, x + 78, y + 58, 10, INNER)
    circle(c, x + 50, y + 32, 6, INNER)
    circle(c, x + 70, y + 32, 6, INNER)
    ellipse(c, x - 100, y - 18, 40, 10)
    capsule(c, x + 18, y - 32, x + 12, y - 78, 8)
    capsule(c, x + 48, y - 32, x + 54, y - 78, 8)


def fox(c, x, y):
    ellipse(c, x, y - 8, 92, 50)
    poly(c, [(x + 68, y + 18), (x + 38, y + 98), (x + 108, y + 98), (x + 92, y + 18)])
    poly(c, [(x + 48, y + 98), (x + 32, y + 138), (x + 68, y + 102)])
    poly(c, [(x + 92, y + 98), (x + 118, y + 138), (x + 82, y + 102)])
    circle(c, x + 62, y + 58, 6, INNER)
    circle(c, x + 88, y + 58, 6, INNER)
    poly(c, [(x - 90, y), (x - 155, y + 22), (x - 148, y - 8), (x - 90, y - 22)])
    capsule(c, x - 38, y - 42, x - 48, y - 112, 13)
    capsule(c, x + 12, y - 50, x + 8, y - 118, 12)
    capsule(c, x + 52, y - 42, x + 62, y - 110, 13)


def elephant(c, x, y):
    ellipse(c, x, y, 112, 70)
    circle(c, x + 88, y + 42, 50)
    circle(c, x + 52, y + 72, 28)
    circle(c, x + 118, y + 72, 28)
    circle(c, x + 52, y + 72, 12, INNER)
    circle(c, x + 118, y + 72, 12, INNER)
    circle(c, x + 78, y + 50, 8, INNER)
    circle(c, x + 106, y + 50, 8, INNER)
    capsule(c, x + 108, y + 20, x + 138, y - 70, 14)
    ellipse(c, x + 148, y - 82, 18, 14)
    capsule(c, x - 58, y - 52, x - 68, y - 128, 16)
    capsule(c, x - 16, y - 68, x - 12, y - 135, 15)
    capsule(c, x + 28, y - 68, x + 32, y - 135, 15)
    capsule(c, x + 62, y - 52, x + 72, y - 124, 16)


def lion(c, x, y):
    for ang in range(0, 360, 30):
        ellipse(
            c,
            x + 82 * cos(radians(ang)),
            y + 28 + 82 * sin(radians(ang)),
            18,
            28,
        )
    circle(c, x, y + 28, 52)
    face(c, x, y + 34, 8, 18)
    ellipse(c, x, y + 12, 14, 10, INNER)
    ellipse(c, x, y - 70, 70, 42)
    capsule(c, x - 38, y - 95, x - 48, y - 140, 13)
    capsule(c, x + 38, y - 95, x + 48, y - 140, 13)
    ellipse(c, x + 95, y - 78, 36, 12)


def giraffe(c, x, y):
    ellipse(c, x, y - 42, 72, 42)
    capsule(c, x + 48, y - 10, x + 72, y + 118, 16)
    circle(c, x + 88, y + 138, 30)
    capsule(c, x + 78, y + 162, x + 74, y + 182, 5)
    capsule(c, x + 98, y + 162, x + 102, y + 182, 5)
    circle(c, x + 74, y + 188, 8)
    circle(c, x + 102, y + 188, 8)
    circle(c, x + 98, y + 142, 6, INNER)
    capsule(c, x - 38, y - 68, x - 48, y - 138, 13)
    capsule(c, x - 8, y - 78, x - 4, y - 142, 12)
    capsule(c, x + 28, y - 78, x + 32, y - 142, 12)
    capsule(c, x + 52, y - 68, x + 62, y - 132, 13)
    circle(c, x + 28, y + 28, 8, INNER)
    circle(c, x + 48, y + 72, 8, INNER)


def monkey(c, x, y):
    circle(c, x, y + 52, 48)
    ellipse(c, x, y + 42, 30, 26, INNER)
    circle(c, x - 14, y + 58, 7, INNER)
    circle(c, x + 14, y + 58, 7, INNER)
    circle(c, x - 50, y + 58, 18)
    circle(c, x + 50, y + 58, 18)
    ellipse(c, x, y - 38, 52, 48)
    capsule(c, x - 52, y - 10, x - 95, y + 40, 12)
    capsule(c, x + 52, y - 10, x + 95, y + 40, 12)
    capsule(c, x - 22, y - 78, x - 28, y - 122, 12)
    capsule(c, x + 22, y - 78, x + 28, y - 122, 12)


def panda(c, x, y):
    ellipse(c, x, y - 28, 88, 72)
    circle(c, x, y + 72, 52)
    ellipse(c, x - 22, y + 80, 16, 20)
    ellipse(c, x + 22, y + 80, 16, 20)
    circle(c, x - 22, y + 80, 7, INNER)
    circle(c, x + 22, y + 80, 7, INNER)
    ellipse(c, x, y + 50, 16, 12, INNER)
    circle(c, x - 40, y + 112, 16)
    circle(c, x + 40, y + 112, 16)
    capsule(c, x - 42, y - 72, x - 52, y - 124, 14)
    capsule(c, x + 42, y - 72, x + 52, y - 124, 14)


def whale(c, x, y):
    ellipse(c, x, y, 138, 55)
    poly(c, [(x - 138, y), (x - 198, y + 58), (x - 168, y), (x - 198, y - 42)])
    circle(c, x + 88, y + 10, 10, INNER)
    arc(c, x + 42, y - 4, x + 88, y + 18, 200, 120, INNER)
    poly(c, [(x - 18, y + 52), (x + 4, y + 102), (x + 28, y + 52)])
    ellipse(c, x + 20, y - 48, 70, 16, INNER)


def crab(c, x, y):
    ellipse(c, x, y, 82, 46)
    circle(c, x - 28, y + 14, 8, INNER)
    circle(c, x + 28, y + 14, 8, INNER)
    capsule(c, x - 80, y + 8, x - 128, y + 48, 10)
    capsule(c, x + 80, y + 8, x + 128, y + 48, 10)
    circle(c, x - 142, y + 55, 22)
    circle(c, x + 142, y + 55, 22)
    for dx in (-48, -16, 16, 48):
        capsule(c, x + dx, y - 38, x + dx - 8, y - 82, 7)
        capsule(c, x + dx, y - 38, x + dx + 8, y - 82, 7)


def butterfly(c, x, y):
    ellipse(c, x - 72, y + 42, 55, 70)
    ellipse(c, x + 72, y + 42, 55, 70)
    ellipse(c, x - 65, y - 48, 45, 48)
    ellipse(c, x + 65, y - 48, 45, 48)
    rrect(c, x - 12, y - 78, 24, 158, 10)
    circle(c, x, y + 92, 16)
    capsule(c, x - 4, y + 104, x - 28, y + 132, 4, INNER)
    capsule(c, x + 4, y + 104, x + 28, y + 132, 4, INNER)
    circle(c, x - 72, y + 42, 18, INNER)
    circle(c, x + 72, y + 42, 18, INNER)


def bee(c, x, y):
    ellipse(c, x, y, 72, 46)
    capsule(c, x - 22, y + 40, x - 22, y - 40, 3, INNER)
    capsule(c, x + 8, y + 40, x + 8, y - 40, 3, INNER)
    circle(c, x + 78, y + 8, 22)
    circle(c, x + 88, y + 14, 6, INNER)
    ellipse(c, x - 20, y + 70, 38, 22)
    ellipse(c, x + 28, y + 70, 38, 22)
    capsule(c, x - 8, y - 42, x - 12, y - 72, 5)
    capsule(c, x + 18, y - 42, x + 22, y - 72, 5)


def snail(c, x, y):
    circle(c, x + 20, y + 20, 70)
    circle(c, x + 20, y + 20, 42, INNER)
    circle(c, x + 20, y + 20, 18, INNER)
    ellipse(c, x - 70, y - 40, 70, 28)
    circle(c, x - 125, y - 18, 22)
    capsule(c, x - 138, y + 2, x - 152, y + 42, 5)
    capsule(c, x - 118, y + 2, x - 128, y + 42, 5)
    circle(c, x - 152, y + 48, 7)
    circle(c, x - 128, y + 48, 7)


def ladybug(c, x, y):
    ellipse(c, x, y, 80, 70)
    capsule(c, x, y + 68, x, y - 68, 3, INNER)
    circle(c, x, y + 82, 22)
    circle(c, x - 8, y + 86, 5, INNER)
    circle(c, x + 8, y + 86, 5, INNER)
    circle(c, x - 32, y + 18, 14, INNER)
    circle(c, x + 32, y + 10, 14, INNER)
    circle(c, x - 22, y - 28, 12, INNER)
    circle(c, x + 28, y - 32, 12, INNER)
    for dx in (-28, 0, 28):
        capsule(c, x + dx, y - 65, x + dx, y - 95, 4)


def hedgehog(c, x, y):
    for ang in range(20, 170, 18):
        tx = x + 95 * cos(radians(ang))
        ty = y + 20 + 70 * sin(radians(ang))
        poly(
            c,
            [
                (x + 50 * cos(radians(ang)), y + 20 + 30 * sin(radians(ang))),
                (tx - 8, ty + 10),
                (tx + 8, ty - 6),
            ],
        )
    ellipse(c, x, y, 90, 50)
    circle(c, x + 85, y + 8, 28)
    circle(c, x + 95, y + 14, 6, INNER)
    ellipse(c, x + 112, y + 4, 12, 7, INNER)
    capsule(c, x - 30, y - 42, x - 35, y - 78, 10)
    capsule(c, x + 30, y - 42, x + 35, y - 78, 10)


def penguin(c, x, y):
    ellipse(c, x, y, 62, 100)
    ellipse(c, x, y - 8, 38, 70, INNER)
    circle(c, x, y + 88, 38)
    circle(c, x - 12, y + 94, 6, INNER)
    circle(c, x + 12, y + 94, 6, INNER)
    poly(c, [(x, y + 82), (x - 12, y + 70), (x + 12, y + 70)])
    ellipse(c, x - 58, y, 18, 32)
    ellipse(c, x + 58, y, 18, 32)
    ellipse(c, x - 22, y - 108, 24, 12)
    ellipse(c, x + 22, y - 108, 24, 12)


# --- vehicles ---

def _wheel(c, x, y, r=28):
    circle(c, x, y, r)
    circle(c, x, y, r * 0.4, INNER)


def car(c, x, y):
    rrect(c, x - 120, y - 20, 240, 70, 22)
    rrect(c, x - 70, y + 48, 140, 48, 16)
    rrect(c, x - 55, y + 58, 50, 28, 8, INNER)
    rrect(c, x + 8, y + 58, 50, 28, 8, INNER)
    _wheel(c, x - 70, y - 28)
    _wheel(c, x + 70, y - 28)
    circle(c, x + 108, y + 8, 8, INNER)


def dump_truck(c, x, y):
    rrect(c, x - 40, y - 10, 150, 70, 12)
    rrect(c, x - 130, y + 10, 90, 85, 10)
    rrect(c, x - 115, y + 28, 50, 40, 8, INNER)
    _wheel(c, x - 85, y - 28, 24)
    _wheel(c, x + 10, y - 28, 24)
    _wheel(c, x + 85, y - 28, 24)


def fire_truck(c, x, y):
    rrect(c, x - 140, y - 8, 260, 70, 12)
    rrect(c, x + 20, y + 60, 90, 55, 10)
    rrect(c, x + 35, y + 72, 55, 32, 8, INNER)
    rrect(c, x - 120, y + 62, 130, 18, 6)
    circle(c, x - 90, y + 28, 10, INNER)
    circle(c, x - 50, y + 28, 10, INNER)
    _wheel(c, x - 80, y - 28, 26)
    _wheel(c, x + 80, y - 28, 26)


def bus(c, x, y):
    rrect(c, x - 150, y - 10, 300, 90, 18)
    for i in range(5):
        rrect(c, x - 125 + i * 52, y + 28, 40, 32, 6, INNER)
    rrect(c, x + 110, y + 12, 28, 50, 6, INNER)
    _wheel(c, x - 90, y - 28, 26)
    _wheel(c, x + 90, y - 28, 26)


def train(c, x, y):
    rrect(c, x - 40, y - 10, 150, 80, 14)
    rrect(c, x - 20, y + 70, 70, 40, 10)
    rrect(c, x - 8, y + 82, 46, 22, 6, INNER)
    rrect(c, x + 70, y + 55, 28, 70, 8)
    circle(c, x + 84, y + 140, 16)
    _wheel(c, x - 5, y - 28, 24)
    _wheel(c, x + 70, y - 28, 24)
    circle(c, x + 100, y + 20, 10, INNER)


def train_car(c, x, y):
    rrect(c, x - 120, y - 8, 240, 90, 14)
    rrect(c, x - 90, y + 22, 70, 40, 8, INNER)
    rrect(c, x + 20, y + 22, 70, 40, 8, INNER)
    _wheel(c, x - 70, y - 28, 22)
    _wheel(c, x + 70, y - 28, 22)
    rrect(c, x - 138, y + 20, 18, 18, 4)
    rrect(c, x + 120, y + 20, 18, 18, 4)


def plane(c, x, y):
    ellipse(c, x, y, 140, 32)
    ellipse(c, x + 20, y, 90, 12, INNER)
    poly(c, [(x - 20, y), (x - 50, y + 90), (x + 40, y + 18), (x + 20, y)])
    poly(c, [(x - 20, y), (x - 50, y - 90), (x + 40, y - 18), (x + 20, y)])
    poly(c, [(x - 130, y), (x - 165, y + 40), (x - 140, y), (x - 165, y - 40)])
    circle(c, x + 90, y + 8, 8, INNER)


def helicopter(c, x, y):
    ellipse(c, x, y, 80, 40)
    rrect(c, x + 40, y - 8, 90, 22, 8)
    circle(c, x - 20, y + 8, 16, INNER)
    rrect(c, x - 12, y + 40, 24, 18, 4)
    ellipse(c, x, y + 70, 130, 10)
    capsule(c, x + 128, y, x + 128, y + 50, 5)
    ellipse(c, x + 128, y + 62, 28, 8)
    capsule(c, x - 30, y - 40, x - 30, y - 70, 6)
    capsule(c, x + 30, y - 40, x + 30, y - 70, 6)
    ellipse(c, x, y - 78, 50, 8)


def boat(c, x, y):
    poly(c, [(x - 130, y + 10), (x + 130, y + 10), (x + 90, y - 50), (x - 90, y - 50)])
    rrect(c, x - 40, y + 10, 80, 40, 8)
    rrect(c, x - 22, y + 22, 44, 20, 6, INNER)
    circle(c, x, y + 70, 10)


def sailboat(c, x, y):
    poly(c, [(x - 110, y - 10), (x + 110, y - 10), (x + 70, y - 55), (x - 70, y - 55)])
    capsule(c, x, y - 10, x, y + 130, 6)
    poly(c, [(x + 8, y + 120), (x + 95, y + 20), (x + 8, y + 20)])
    poly(c, [(x - 8, y + 90), (x - 70, y + 20), (x - 8, y + 20)])


def bicycle(c, x, y):
    _wheel(c, x - 80, y - 40, 42)
    _wheel(c, x + 80, y - 40, 42)
    poly(c, [(x - 80, y - 40), (x - 10, y + 40), (x + 55, y + 8), (x - 80, y - 40)], OUTER, False)
    capsule(c, x - 10, y + 40, x - 10, y + 70, 6)
    ellipse(c, x - 10, y + 82, 22, 8)
    capsule(c, x + 55, y + 8, x + 80, y - 40, 6)
    ellipse(c, x + 40, y + 8, 18, 8)


def scooter(c, x, y):
    rrect(c, x - 90, y - 20, 150, 18, 8)
    capsule(c, x + 60, y - 10, x + 40, y + 90, 8)
    ellipse(c, x + 28, y + 102, 22, 8)
    _wheel(c, x - 70, y - 40, 24)
    _wheel(c, x + 70, y - 40, 24)


def tractor(c, x, y):
    rrect(c, x - 20, y - 5, 110, 55, 12)
    rrect(c, x + 10, y + 48, 60, 48, 10)
    rrect(c, x + 22, y + 60, 36, 26, 6, INNER)
    _wheel(c, x - 70, y - 10, 48)
    _wheel(c, x + 70, y - 28, 28)
    circle(c, x - 20, y + 28, 10, INNER)


def digger(c, x, y):
    rrect(c, x - 80, y - 5, 130, 55, 12)
    rrect(c, x - 50, y + 48, 55, 42, 8)
    rrect(c, x - 40, y + 58, 32, 22, 6, INNER)
    capsule(c, x + 40, y + 30, x + 120, y + 90, 12)
    poly(c, [(x + 118, y + 90), (x + 165, y + 70), (x + 155, y + 40), (x + 110, y + 70)])
    _wheel(c, x - 55, y - 28, 26)
    _wheel(c, x + 25, y - 28, 26)


def garbage_truck(c, x, y):
    rrect(c, x - 30, y - 8, 160, 90, 12)
    rrect(c, x - 130, y + 5, 100, 70, 10)
    rrect(c, x - 115, y + 22, 50, 38, 8, INNER)
    rrect(c, x + 90, y + 40, 28, 50, 6)
    _wheel(c, x - 80, y - 28, 24)
    _wheel(c, x + 20, y - 28, 24)
    _wheel(c, x + 90, y - 28, 24)


def motorcycle(c, x, y):
    _wheel(c, x - 80, y - 30, 36)
    _wheel(c, x + 80, y - 30, 36)
    ellipse(c, x, y + 10, 55, 18)
    capsule(c, x + 40, y + 10, x + 80, y - 30, 8)
    capsule(c, x - 40, y + 10, x - 80, y - 30, 8)
    ellipse(c, x - 10, y + 40, 28, 14)
    capsule(c, x + 30, y + 18, x + 20, y + 70, 6)
    ellipse(c, x + 8, y + 80, 20, 7)


def rocket(c, x, y):
    ellipse(c, x, y + 40, 40, 110)
    poly(c, [(x - 40, y - 40), (x - 80, y - 100), (x - 18, y - 70)])
    poly(c, [(x + 40, y - 40), (x + 80, y - 100), (x + 18, y - 70)])
    circle(c, x, y + 70, 16, INNER)
    circle(c, x, y + 20, 12, INNER)
    poly(c, [(x - 18, y - 68), (x, y - 120), (x + 18, y - 68)])


def submarine(c, x, y):
    ellipse(c, x, y, 140, 48)
    rrect(c, x - 20, y + 45, 55, 32, 8)
    capsule(c, x + 8, y + 75, x + 8, y + 115, 6)
    circle(c, x - 50, y + 8, 10, INNER)
    circle(c, x - 10, y + 8, 10, INNER)
    circle(c, x + 30, y + 8, 10, INNER)
    poly(c, [(x - 140, y), (x - 175, y + 28), (x - 175, y - 28)])


def cement_mixer(c, x, y):
    rrect(c, x - 130, y + 5, 95, 65, 10)
    rrect(c, x - 115, y + 22, 48, 32, 8, INNER)
    ellipse(c, x + 30, y + 30, 70, 50)
    ellipse(c, x + 30, y + 30, 48, 32, INNER)
    rrect(c, x - 40, y - 8, 50, 40, 8)
    _wheel(c, x - 80, y - 28, 24)
    _wheel(c, x + 20, y - 28, 24)
    _wheel(c, x + 80, y - 28, 24)


def tow_truck(c, x, y):
    rrect(c, x - 130, y + 5, 100, 65, 10)
    rrect(c, x - 115, y + 22, 50, 32, 8, INNER)
    rrect(c, x - 30, y - 8, 150, 28, 8)
    capsule(c, x + 20, y + 20, x + 110, y + 80, 10)
    circle(c, x + 118, y + 88, 12)
    _wheel(c, x - 80, y - 28, 24)
    _wheel(c, x + 40, y - 28, 24)
    _wheel(c, x + 95, y - 28, 24)


def van(c, x, y):
    rrect(c, x - 130, y - 10, 260, 80, 18)
    rrect(c, x - 40, y + 68, 150, 42, 12)
    rrect(c, x - 20, y + 78, 50, 24, 6, INNER)
    rrect(c, x + 45, y + 78, 50, 24, 6, INNER)
    _wheel(c, x - 75, y - 28, 26)
    _wheel(c, x + 75, y - 28, 26)


def pickup(c, x, y):
    rrect(c, x - 20, y - 8, 140, 50, 10)
    rrect(c, x - 130, y - 8, 110, 70, 12)
    rrect(c, x - 115, y + 22, 55, 28, 8, INNER)
    _wheel(c, x - 75, y - 28, 26)
    _wheel(c, x + 70, y - 28, 26)


def crane(c, x, y):
    rrect(c, x - 90, y - 8, 130, 50, 10)
    capsule(c, x + 20, y + 40, x + 20, y + 140, 12)
    capsule(c, x + 20, y + 140, x + 130, y + 100, 10)
    circle(c, x + 138, y + 92, 10)
    capsule(c, x + 138, y + 82, x + 138, y + 40, 4, INNER)
    rrect(c, x + 118, y + 18, 40, 22, 4)
    _wheel(c, x - 55, y - 28, 24)
    _wheel(c, x + 20, y - 28, 24)


def wagon(c, x, y):
    rrect(c, x - 90, y - 5, 180, 55, 12)
    capsule(c, x - 90, y + 20, x - 150, y + 50, 8)
    circle(c, x - 158, y + 55, 10)
    _wheel(c, x - 50, y - 32, 24)
    _wheel(c, x + 50, y - 32, 24)


# --- foods ---

def apple(c, x, y):
    circle(c, x, y, 85)
    capsule(c, x, y + 80, x + 8, y + 125, 6)
    ellipse(c, x + 28, y + 118, 28, 14)
    ellipse(c, x - 20, y + 20, 18, 28, INNER)


def banana(c, x, y):
    arc(c, x - 120, y - 80, x + 80, y + 100, 200, 150)
    arc(c, x - 95, y - 55, x + 55, y + 75, 200, 150)
    poly(c, [(x + 62, y + 48), (x + 95, y + 70), (x + 78, y + 28)])
    poly(c, [(x - 95, y - 8), (x - 125, y - 35), (x - 88, y - 40)])


def grapes(c, x, y):
    for gx, gy in (
        (0, 40),
        (-28, 10),
        (28, 10),
        (-50, -22),
        (0, -22),
        (50, -22),
        (-28, -54),
        (28, -54),
        (0, -86),
    ):
        circle(c, x + gx, y + gy, 24)
    capsule(c, x, y + 62, x + 8, y + 110, 5)
    ellipse(c, x + 28, y + 112, 22, 12)


def watermelon(c, x, y):
    arc(c, x - 130, y - 80, x + 130, y + 90, 200, 140)
    arc(c, x - 110, y - 55, x + 110, y + 70, 200, 140, INNER)
    for sx, sy in ((-40, 0), (0, 18), (40, 0), (-20, -28), (20, -28)):
        ellipse(c, x + sx, y + sy, 6, 10, INNER)


def carrot(c, x, y):
    poly(c, [(x, y + 90), (x - 48, y - 20), (x, y - 130), (x + 48, y - 20)])
    capsule(c, x - 8, y + 90, x - 28, y + 145, 7)
    capsule(c, x, y + 90, x + 6, y + 155, 7)
    capsule(c, x + 8, y + 90, x + 32, y + 140, 7)
    capsule(c, x - 20, y + 20, x + 20, y + 20, 3, INNER)
    capsule(c, x - 14, y - 20, x + 14, y - 20, 3, INNER)


def ice_cream(c, x, y):
    poly(c, [(x - 55, y + 10), (x + 55, y + 10), (x, y - 130)])
    circle(c, x, y + 55, 58)
    circle(c, x - 22, y + 95, 28)
    circle(c, x + 24, y + 90, 26)
    ellipse(c, x + 8, y + 128, 16, 12)


def cupcake(c, x, y):
    poly(c, [(x - 70, y + 20), (x + 70, y + 20), (x + 50, y - 80), (x - 50, y - 80)])
    ellipse(c, x, y + 35, 80, 28)
    circle(c, x - 25, y + 70, 22)
    circle(c, x + 18, y + 78, 24)
    circle(c, x + 5, y + 108, 16)
    capsule(c, x, y + 120, x, y + 145, 4)
    ellipse(c, x + 8, y + 152, 10, 8)


def cookie(c, x, y):
    circle(c, x, y, 90)
    for px, py in ((-30, 25), (25, 20), (0, -10), (-35, -30), (30, -35), (10, 50)):
        circle(c, x + px, y + py, 10, INNER)


def pizza(c, x, y):
    circle(c, x, y, 110)
    circle(c, x, y, 88, INNER)
    for px, py in ((-30, 25), (35, 10), (0, -35), (-40, -20), (25, -15)):
        circle(c, x + px, y + py, 16, INNER)


def bread(c, x, y):
    ellipse(c, x, y, 120, 55)
    ellipse(c, x, y + 8, 90, 28, INNER)
    arc(c, x - 50, y + 10, x - 20, y + 40, 0, 180, INNER)
    arc(c, x - 10, y + 10, x + 20, y + 40, 0, 180, INNER)
    arc(c, x + 30, y + 10, x + 60, y + 40, 0, 180, INNER)


def pear(c, x, y):
    circle(c, x, y - 40, 70)
    ellipse(c, x, y + 50, 48, 55)
    capsule(c, x, y + 100, x + 6, y + 140, 5)
    ellipse(c, x + 24, y + 138, 22, 12)


def strawberry(c, x, y):
    poly(c, [(x, y - 110), (x - 80, y + 30), (x - 40, y + 70), (x + 40, y + 70), (x + 80, y + 30)])
    for px, py in ((-25, 10), (20, 5), (0, -30), (-30, -40), (28, -45), (0, 35)):
        circle(c, x + px, y + py, 6, INNER)
    ellipse(c, x - 22, y + 88, 16, 22)
    ellipse(c, x + 22, y + 88, 16, 22)
    ellipse(c, x, y + 100, 16, 24)


def orange(c, x, y):
    circle(c, x, y, 90)
    circle(c, x, y, 12, INNER)
    for ang in range(0, 360, 45):
        capsule(
            c,
            x + 18 * cos(radians(ang)),
            y + 18 * sin(radians(ang)),
            x + 70 * cos(radians(ang)),
            y + 70 * sin(radians(ang)),
            3,
            INNER,
        )
    ellipse(c, x + 8, y + 95, 18, 10)


def donut(c, x, y):
    circle(c, x, y, 90)
    circle(c, x, y, 32)
    circle(c, x, y, 70, INNER)
    for px, py in ((-40, 30), (35, 25), (0, -45), (45, -10)):
        ellipse(c, x + px, y + py, 8, 5, INNER)


def sandwich(c, x, y):
    rrect(c, x - 100, y - 20, 200, 70, 16)
    rrect(c, x - 100, y + 20, 200, 70, 16)
    ellipse(c, x, y + 20, 80, 12, INNER)
    circle(c, x - 30, y + 50, 10, INNER)
    circle(c, x + 25, y + 48, 10, INNER)


def cheese(c, x, y):
    poly(c, [(x - 110, y - 60), (x + 110, y - 60), (x + 40, y + 90), (x - 40, y + 90)])
    circle(c, x - 20, y, 16, INNER)
    circle(c, x + 30, y - 20, 12, INNER)
    circle(c, x + 10, y + 35, 14, INNER)


def milk(c, x, y):
    rrect(c, x - 50, y - 90, 100, 160, 16)
    rrect(c, x - 28, y + 70, 56, 40, 8)
    rrect(c, x - 35, y + 20, 70, 28, 6, INNER)


def corn(c, x, y):
    ellipse(c, x, y, 42, 110)
    for row in range(-4, 5):
        for col in (-1, 1, 0):
            circle(c, x + col * 16, y + row * 20, 7, INNER)
    poly(c, [(x - 40, y + 90), (x - 70, y + 150), (x - 10, y + 110)])
    poly(c, [(x + 40, y + 90), (x + 70, y + 150), (x + 10, y + 110)])


def mushroom(c, x, y):
    ellipse(c, x, y + 40, 90, 50)
    rrect(c, x - 28, y - 80, 56, 90, 16)
    circle(c, x - 30, y + 40, 10, INNER)
    circle(c, x + 20, y + 50, 10, INNER)
    circle(c, x + 10, y + 22, 8, INNER)


# --- everyday ---

def ball(c, x, y):
    circle(c, x, y, 95)
    arc(c, x - 95, y - 40, x + 95, y + 40, 0, 180, INNER)
    arc(c, x - 95, y - 40, x + 95, y + 40, 180, 180, INNER)
    capsule(c, x, y - 95, x, y + 95, 3, INNER)


def balloon(c, x, y):
    ellipse(c, x, y + 30, 60, 85)
    poly(c, [(x - 12, y - 52), (x, y - 78), (x + 12, y - 52)])
    poly(
        c,
        [(x, y - 78), (x - 18, y - 110), (x + 12, y - 140), (x - 8, y - 160)],
        INNER,
        False,
    )


def kite(c, x, y):
    poly(c, [(x, y + 120), (x + 80, y), (x, y - 70), (x - 80, y)])
    capsule(c, x - 80, y, x + 80, y, 3, INNER)
    capsule(c, x, y + 120, x, y - 70, 3, INNER)
    poly(
        c,
        [(x, y - 70), (x + 20, y - 110), (x - 10, y - 140), (x + 18, y - 170)],
        INNER,
        False,
    )


def house(c, x, y):
    rrect(c, x - 110, y - 80, 220, 140, 8)
    poly(c, [(x - 130, y + 60), (x, y + 150), (x + 130, y + 60)])
    rrect(c, x - 25, y - 80, 50, 70, 6, INNER)
    rrect(c, x - 85, y - 10, 45, 40, 6, INNER)
    rrect(c, x + 40, y - 10, 45, 40, 6, INNER)
    circle(c, x + 18, y - 45, 6, INNER)


def tree(c, x, y):
    rrect(c, x - 18, y - 120, 36, 90, 8)
    circle(c, x, y + 40, 80)
    circle(c, x - 50, y + 10, 45)
    circle(c, x + 50, y + 10, 45)
    circle(c, x, y + 90, 40)


def flower(c, x, y):
    for ang in range(0, 360, 60):
        ellipse(
            c,
            x + 48 * cos(radians(ang)),
            y + 40 + 48 * sin(radians(ang)),
            22,
            32,
        )
    circle(c, x, y + 40, 28)
    capsule(c, x, y + 10, x, y - 120, 8)
    ellipse(c, x - 28, y - 40, 22, 12)
    ellipse(c, x + 28, y - 20, 22, 12)


def sun(c, x, y):
    circle(c, x, y, 55)
    for ang in range(0, 360, 30):
        capsule(
            c,
            x + 68 * cos(radians(ang)),
            y + 68 * sin(radians(ang)),
            x + 108 * cos(radians(ang)),
            y + 108 * sin(radians(ang)),
            8,
        )
    face(c, x, y, 7, 16)


def moon(c, x, y):
    circle(c, x, y, 90)
    circle(c, x + 35, y + 20, 70)
    circle(c, x - 30, y + 30, 12, INNER)
    circle(c, x - 10, y - 20, 8, INNER)
    circle(c, x + 10, y + 50, 6, INNER)


def star_shape(c, x, y):
    pts = []
    for i in range(10):
        r = 110 if i % 2 == 0 else 45
        ang = radians(-90 + i * 36)
        pts.append((x + r * cos(ang), y + r * sin(ang)))
    poly(c, pts)


def cloud(c, x, y):
    ellipse(c, x, y, 90, 40)
    circle(c, x - 50, y + 20, 40)
    circle(c, x + 10, y + 35, 50)
    circle(c, x + 55, y + 15, 38)


def book(c, x, y):
    rrect(c, x - 90, y - 80, 180, 160, 8)
    capsule(c, x, y - 80, x, y + 80, 3)
    rrect(c, x - 75, y + 20, 60, 8, 3, INNER)
    rrect(c, x - 75, y - 5, 60, 8, 3, INNER)
    rrect(c, x + 15, y + 20, 60, 8, 3, INNER)


def pencil(c, x, y):
    rrect(c, x - 22, y - 90, 44, 160, 8)
    poly(c, [(x - 22, y + 70), (x, y + 130), (x + 22, y + 70)])
    circle(c, x, y + 118, 5, INNER)
    rrect(c, x - 22, y - 110, 44, 22, 6)
    ellipse(c, x, y - 118, 22, 10)


def chair(c, x, y):
    rrect(c, x - 70, y - 10, 140, 22, 8)
    rrect(c, x - 70, y + 12, 22, 110, 8)
    capsule(c, x - 60, y - 10, x - 60, y - 90, 8)
    capsule(c, x + 60, y - 10, x + 60, y - 90, 8)
    capsule(c, x - 60, y + 12, x - 60, y + 20, 8)


def bed(c, x, y):
    rrect(c, x - 140, y - 20, 280, 50, 12)
    rrect(c, x - 140, y + 28, 28, 80, 8)
    rrect(c, x + 112, y + 28, 28, 50, 8)
    ellipse(c, x - 80, y + 40, 32, 18)
    rrect(c, x - 40, y + 18, 140, 28, 10, INNER)


def cup(c, x, y):
    rrect(c, x - 50, y - 70, 100, 120, 16)
    ellipse(c, x, y + 50, 50, 16)
    ellipse(c, x + 70, y + 10, 22, 32)
    ellipse(c, x + 70, y + 10, 10, 18, INNER)


def spoon(c, x, y):
    ellipse(c, x, y + 70, 32, 48)
    capsule(c, x, y + 25, x, y - 120, 10)
    ellipse(c, x, y + 70, 18, 30, INNER)


def toothbrush(c, x, y):
    rrect(c, x - 16, y - 110, 32, 160, 10)
    rrect(c, x - 28, y + 50, 56, 70, 8)
    for i in range(5):
        capsule(c, x - 18, y + 58 + i * 12, x + 18, y + 58 + i * 12, 3, INNER)


def teddy(c, x, y):
    ellipse(c, x, y - 20, 80, 70)
    circle(c, x, y + 70, 48)
    circle(c, x - 38, y + 105, 16)
    circle(c, x + 38, y + 105, 16)
    face(c, x, y + 72, 7, 15)
    ellipse(c, x, y + 52, 12, 10, INNER)
    ellipse(c, x - 70, y - 10, 22, 18)
    ellipse(c, x + 70, y - 10, 22, 18)
    capsule(c, x - 35, y - 70, x - 40, y - 115, 12)
    capsule(c, x + 35, y - 70, x + 40, y - 115, 12)


def blocks(c, x, y):
    rrect(c, x - 90, y - 40, 80, 80, 8)
    rrect(c, x + 10, y - 40, 80, 80, 8)
    rrect(c, x - 40, y + 40, 80, 80, 8)
    rrect(c, x - 70, y - 20, 40, 8, 3, INNER)
    rrect(c, x + 30, y - 20, 40, 8, 3, INNER)
    rrect(c, x - 20, y + 70, 40, 8, 3, INNER)


def drum(c, x, y):
    ellipse(c, x, y + 50, 90, 28)
    rrect(c, x - 90, y - 70, 180, 120, 8)
    ellipse(c, x, y - 70, 90, 28)
    capsule(c, x - 40, y + 80, x - 90, y + 130, 6)
    capsule(c, x + 40, y + 80, x + 90, y + 130, 6)
    ellipse(c, x - 98, y + 138, 12, 8)
    ellipse(c, x + 98, y + 138, 12, 8)


def clock(c, x, y):
    circle(c, x, y, 90)
    circle(c, x, y, 8, INNER)
    capsule(c, x, y, x, y + 45, 4, INNER)
    capsule(c, x, y, x + 32, y - 8, 4, INNER)
    ellipse(c, x - 40, y + 95, 12, 12)
    ellipse(c, x + 40, y + 95, 12, 12)


def umbrella(c, x, y):
    arc(c, x - 115, y - 10, x + 115, y + 110, 0, 180)
    poly(c, [(x - 115, y + 50), (x + 115, y + 50), (x + 115, y + 50)])
    capsule(c, x - 115, y + 50, x + 115, y + 50, 4)
    capsule(c, x, y + 50, x, y - 90, 7)
    arc(c, x, y - 115, x + 32, y - 78, 180, 180)
    capsule(c, x - 55, y + 50, x - 55, y + 90, 4, INNER)
    capsule(c, x + 55, y + 50, x + 55, y + 90, 4, INNER)


def backpack(c, x, y):
    rrect(c, x - 60, y - 80, 120, 155, 20)
    rrect(c, x - 40, y - 10, 80, 50, 12, INNER)
    ellipse(c, x, y + 75, 40, 14)
    capsule(c, x - 78, y - 50, x - 78, y + 40, 10)
    capsule(c, x + 78, y - 50, x + 78, y + 40, 10)


def socks(c, x, y):
    rrect(c, x - 85, y - 10, 42, 110, 16)
    ellipse(c, x - 90, y - 40, 40, 28)
    rrect(c, x + 25, y - 10, 42, 110, 16)
    ellipse(c, x + 20, y - 40, 40, 28)
    capsule(c, x - 85, y + 70, x - 43, y + 70, 4, INNER)
    capsule(c, x + 25, y + 70, x + 67, y + 70, 4, INNER)


def shoes(c, x, y):
    ellipse(c, x - 70, y, 70, 32)
    rrect(c, x - 95, y, 50, 42, 12)
    ellipse(c, x + 70, y, 70, 32)
    rrect(c, x + 45, y, 50, 42, 12)
    circle(c, x - 55, y + 12, 6, INNER)
    circle(c, x + 85, y + 12, 6, INNER)


def leaf(c, x, y):
    ellipse(c, x, y, 42, 95)
    capsule(c, x, y + 95, x, y - 95, 3, INNER)
    capsule(c, x, y + 20, x + 28, y + 40, 3, INNER)
    capsule(c, x, y - 10, x - 28, y + 10, 3, INNER)


def key(c, x, y):
    circle(c, x, y + 50, 34)
    circle(c, x, y + 50, 14, INNER)
    rrect(c, x - 12, y - 80, 24, 100, 6)
    rrect(c, x + 10, y - 55, 22, 12, 3, INNER)
    rrect(c, x + 10, y - 75, 18, 12, 3, INNER)


PAGES: list[tuple[str, object]] = [
    ("cat", cat),
    ("dog", dog),
    ("fish", fish),
    ("bird", bird),
    ("duck", duck),
    ("frog", frog),
    ("bunny", bunny),
    ("bear", bear),
    ("pig", pig),
    ("cow", cow),
    ("horse", horse),
    ("sheep", sheep),
    ("chick", chick),
    ("owl", owl),
    ("turtle", turtle),
    ("mouse", mouse),
    ("fox", fox),
    ("elephant", elephant),
    ("lion", lion),
    ("giraffe", giraffe),
    ("monkey", monkey),
    ("panda", panda),
    ("whale", whale),
    ("crab", crab),
    ("butterfly", butterfly),
    ("bee", bee),
    ("snail", snail),
    ("ladybug", ladybug),
    ("hedgehog", hedgehog),
    ("penguin", penguin),
    ("car", car),
    ("dump truck", dump_truck),
    ("fire truck", fire_truck),
    ("bus", bus),
    ("train", train),
    ("train car", train_car),
    ("plane", plane),
    ("helicopter", helicopter),
    ("boat", boat),
    ("sailboat", sailboat),
    ("bicycle", bicycle),
    ("scooter", scooter),
    ("tractor", tractor),
    ("digger", digger),
    ("garbage truck", garbage_truck),
    ("motorcycle", motorcycle),
    ("rocket", rocket),
    ("submarine", submarine),
    ("cement mixer", cement_mixer),
    ("tow truck", tow_truck),
    ("van", van),
    ("pickup", pickup),
    ("crane", crane),
    ("wagon", wagon),
    ("apple", apple),
    ("banana", banana),
    ("grapes", grapes),
    ("watermelon", watermelon),
    ("carrot", carrot),
    ("ice cream", ice_cream),
    ("cupcake", cupcake),
    ("cookie", cookie),
    ("pizza", pizza),
    ("bread", bread),
    ("pear", pear),
    ("strawberry", strawberry),
    ("orange", orange),
    ("donut", donut),
    ("sandwich", sandwich),
    ("cheese", cheese),
    ("milk", milk),
    ("corn", corn),
    ("mushroom", mushroom),
    ("ball", ball),
    ("balloon", balloon),
    ("kite", kite),
    ("house", house),
    ("tree", tree),
    ("flower", flower),
    ("sun", sun),
    ("moon", moon),
    ("star", star_shape),
    ("cloud", cloud),
    ("book", book),
    ("pencil", pencil),
    ("chair", chair),
    ("bed", bed),
    ("cup", cup),
    ("spoon", spoon),
    ("toothbrush", toothbrush),
    ("teddy", teddy),
    ("blocks", blocks),
    ("drum", drum),
    ("clock", clock),
    ("umbrella", umbrella),
    ("backpack", backpack),
    ("socks", socks),
    ("shoes", shoes),
    ("leaf", leaf),
    ("key", key),
]

assert len(PAGES) == 100, len(PAGES)
