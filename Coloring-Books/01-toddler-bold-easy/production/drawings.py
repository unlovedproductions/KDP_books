"""100 unique toddler coloring drawings: black stroke, no fill, no shading."""

from __future__ import annotations

from reportlab.pdfgen.canvas import Canvas

OUTER = 8.0
INNER = 5.0


def _stroke(c: Canvas, w: float) -> None:
    c.setStrokeColorRGB(0, 0, 0)
    c.setFillColorRGB(1, 1, 1)
    c.setLineWidth(w)
    c.setLineCap(1)
    c.setLineJoin(1)


def circle(c: Canvas, x: float, y: float, r: float, w: float = OUTER) -> None:
    _stroke(c, w)
    c.circle(x, y, r, stroke=1, fill=0)


def ellipse(c: Canvas, x: float, y: float, rx: float, ry: float, w: float = OUTER) -> None:
    _stroke(c, w)
    c.ellipse(x - rx, y - ry, x + rx, y + ry, stroke=1, fill=0)


def rrect(c: Canvas, x: float, y: float, width: float, height: float, r: float = 12, w: float = OUTER) -> None:
    _stroke(c, w)
    c.roundRect(x, y, width, height, r, stroke=1, fill=0)


def line(c: Canvas, x1: float, y1: float, x2: float, y2: float, w: float = OUTER) -> None:
    _stroke(c, w)
    c.line(x1, y1, x2, y2)


def poly(c: Canvas, pts: list[tuple[float, float]], w: float = OUTER, close: bool = True) -> None:
    _stroke(c, w)
    p = c.beginPath()
    p.moveTo(pts[0][0], pts[0][1])
    for x, y in pts[1:]:
        p.lineTo(x, y)
    if close:
        p.close()
    c.drawPath(p, stroke=1, fill=0)


def arc(c: Canvas, x1: float, y1: float, x2: float, y2: float, start: float, extent: float, w: float = OUTER) -> None:
    _stroke(c, w)
    c.arc(x1, y1, x2, y2, start, extent)


# --- animals ---

def cat(c, x, y):
    ellipse(c, x, y - 20, 95, 70)
    circle(c, x + 70, y + 70, 55)
    poly(c, [(x + 40, y + 110), (x + 28, y + 165), (x + 70, y + 125)])
    poly(c, [(x + 100, y + 110), (x + 130, y + 165), (x + 112, y + 120)])
    circle(c, x + 55, y + 78, 8, INNER)
    circle(c, x + 88, y + 78, 8, INNER)
    arc(c, x + 50, y + 50, x + 90, y + 72, 200, 140, INNER)
    line(c, x - 95, y - 40, x - 95, y - 110)
    line(c, x - 50, y - 70, x - 50, y - 120)
    line(c, x + 40, y - 70, x + 40, y - 120)
    line(c, x + 80, y - 40, x + 80, y - 110)
    arc(c, x - 150, y - 10, x - 80, y + 50, 20, 160)


def dog(c, x, y):
    ellipse(c, x, y - 10, 110, 65)
    circle(c, x + 90, y + 55, 50)
    ellipse(c, x + 55, y + 40, 18, 35)
    ellipse(c, x + 125, y + 40, 18, 35)
    circle(c, x + 78, y + 62, 7, INNER)
    circle(c, x + 105, y + 62, 7, INNER)
    ellipse(c, x + 95, y + 42, 10, 7, INNER)
    line(c, x - 70, y - 50, x - 80, y - 120)
    line(c, x - 30, y - 70, x - 25, y - 125)
    line(c, x + 20, y - 70, x + 15, y - 125)
    line(c, x + 60, y - 50, x + 70, y - 120)
    poly(c, [(x - 110, y + 10), (x - 165, y + 25), (x - 110, y - 5)])


def fish(c, x, y):
    ellipse(c, x, y, 120, 60)
    poly(c, [(x - 120, y), (x - 185, y + 55), (x - 185, y - 55)])
    poly(c, [(x + 10, y + 58), (x + 40, y + 105), (x + 55, y + 55)])
    circle(c, x + 70, y + 12, 12, INNER)
    circle(c, x + 74, y + 14, 4, INNER)
    arc(c, x + 20, y - 15, x + 70, y + 15, 190, 160, INNER)


def bird(c, x, y):
    ellipse(c, x, y, 80, 50)
    circle(c, x + 70, y + 35, 38)
    poly(c, [(x + 100, y + 35), (x + 145, y + 45), (x + 100, y + 20)])
    circle(c, x + 80, y + 42, 7, INNER)
    ellipse(c, x - 20, y + 10, 40, 18, INNER)
    line(c, x - 10, y - 48, x - 20, y - 95)
    line(c, x + 20, y - 48, x + 30, y - 95)
    line(c, x - 35, y - 95, x - 5, y - 95, INNER)
    line(c, x + 15, y - 95, x + 45, y - 95, INNER)


def duck(c, x, y):
    ellipse(c, x, y - 20, 90, 55)
    circle(c, x + 75, y + 50, 42)
    ellipse(c, x + 115, y + 48, 28, 12)
    circle(c, x + 70, y + 58, 7, INNER)
    arc(c, x - 40, y - 90, x + 80, y - 20, 200, 140)
    line(c, x - 20, y - 70, x - 30, y - 110)
    line(c, x + 30, y - 70, x + 40, y - 110)


def frog(c, x, y):
    ellipse(c, x, y, 100, 70)
    circle(c, x - 45, y + 70, 28)
    circle(c, x + 45, y + 70, 28)
    circle(c, x - 45, y + 70, 10, INNER)
    circle(c, x + 45, y + 70, 10, INNER)
    arc(c, x - 30, y - 10, x + 30, y + 25, 200, 140, INNER)
    ellipse(c, x - 90, y - 80, 40, 22)
    ellipse(c, x + 90, y - 80, 40, 22)
    line(c, x - 50, y - 50, x - 70, y - 80)
    line(c, x + 50, y - 50, x + 70, y - 80)


def bunny(c, x, y):
    ellipse(c, x, y - 30, 85, 70)
    circle(c, x, y + 70, 50)
    ellipse(c, x - 22, y + 140, 16, 50)
    ellipse(c, x + 22, y + 140, 16, 50)
    circle(c, x - 15, y + 75, 7, INNER)
    circle(c, x + 15, y + 75, 7, INNER)
    ellipse(c, x, y + 55, 10, 8, INNER)
    line(c, x - 40, y - 80, x - 50, y - 130)
    line(c, x + 40, y - 80, x + 50, y - 130)
    ellipse(c, x, y - 95, 22, 14)


def bear(c, x, y):
    ellipse(c, x, y - 20, 100, 80)
    circle(c, x, y + 75, 55)
    circle(c, x - 45, y + 115, 22)
    circle(c, x + 45, y + 115, 22)
    circle(c, x - 18, y + 80, 8, INNER)
    circle(c, x + 18, y + 80, 8, INNER)
    ellipse(c, x, y + 55, 18, 14, INNER)
    line(c, x - 55, y - 80, x - 65, y - 130)
    line(c, x - 20, y - 95, x - 20, y - 140)
    line(c, x + 20, y - 95, x + 20, y - 140)
    line(c, x + 55, y - 80, x + 65, y - 130)


def pig(c, x, y):
    ellipse(c, x, y, 100, 65)
    circle(c, x + 80, y + 40, 48)
    ellipse(c, x + 95, y + 35, 22, 16)
    circle(c, x + 88, y + 35, 5, INNER)
    circle(c, x + 102, y + 35, 5, INNER)
    circle(c, x + 70, y + 55, 7, INNER)
    circle(c, x + 95, y + 58, 7, INNER)
    circle(c, x + 55, y + 80, 14)
    circle(c, x + 100, y + 82, 14)
    line(c, x - 50, y - 50, x - 55, y - 105)
    line(c, x - 15, y - 62, x - 10, y - 110)
    line(c, x + 25, y - 62, x + 30, y - 110)
    line(c, x + 55, y - 50, x + 60, y - 105)
    arc(c, x - 140, y - 20, x - 90, y + 30, 0, 180)


def cow(c, x, y):
    ellipse(c, x, y - 10, 120, 70)
    circle(c, x + 100, y + 50, 48)
    ellipse(c, x + 100, y + 20, 28, 16)
    circle(c, x + 85, y + 58, 7, INNER)
    circle(c, x + 115, y + 58, 7, INNER)
    line(c, x + 70, y + 90, x + 55, y + 125)
    line(c, x + 130, y + 90, x + 145, y + 125)
    ellipse(c, x + 48, y + 125, 14, 10)
    ellipse(c, x + 152, y + 125, 14, 10)
    circle(c, x - 20, y + 20, 22, INNER)
    circle(c, x + 25, y - 15, 18, INNER)
    line(c, x - 70, y - 60, x - 80, y - 125)
    line(c, x - 20, y - 75, x - 15, y - 130)
    line(c, x + 30, y - 75, x + 35, y - 130)
    line(c, x + 70, y - 55, x + 80, y - 120)


def horse(c, x, y):
    ellipse(c, x, y, 115, 55)
    ellipse(c, x + 100, y + 55, 35, 50)
    ellipse(c, x + 125, y + 85, 40, 22)
    circle(c, x + 145, y + 92, 7, INNER)
    line(c, x + 155, y + 80, x + 185, y + 70, INNER)
    line(c, x - 50, y - 40, x - 55, y - 130)
    line(c, x - 10, y - 50, x - 5, y - 135)
    line(c, x + 40, y - 50, x + 45, y - 135)
    line(c, x + 80, y - 40, x + 90, y - 125)
    poly(c, [(x - 100, y + 20), (x - 130, y + 80), (x - 70, y + 30)])
    line(c, x - 110, y + 5, x - 155, y - 20)


def sheep(c, x, y):
    circle(c, x - 40, y, 40)
    circle(c, x + 10, y + 25, 38)
    circle(c, x + 50, y - 5, 42)
    circle(c, x - 5, y - 35, 36)
    circle(c, x + 35, y + 35, 32)
    circle(c, x + 95, y + 20, 40)
    circle(c, x + 80, y + 55, 12, INNER)
    circle(c, x + 105, y + 55, 12, INNER)
    ellipse(c, x + 95, y + 30, 14, 10, INNER)
    line(c, x - 30, y - 55, x - 35, y - 110)
    line(c, x + 15, y - 60, x + 20, y - 115)
    line(c, x + 50, y - 55, x + 55, y - 110)
    line(c, x + 85, y - 45, x + 90, y - 100)


def chick(c, x, y):
    circle(c, x, y, 70)
    circle(c, x + 15, y + 20, 10, INNER)
    poly(c, [(x + 55, y + 5), (x + 95, y + 15), (x + 55, y - 10)])
    poly(c, [(x - 20, y + 70), (x, y + 115), (x + 20, y + 70)])
    line(c, x - 15, y - 68, x - 25, y - 110)
    line(c, x + 15, y - 68, x + 25, y - 110)
    line(c, x - 40, y - 110, x - 10, y - 110, INNER)
    line(c, x + 10, y - 110, x + 40, y - 110, INNER)


def owl(c, x, y):
    ellipse(c, x, y, 70, 95)
    circle(c, x - 28, y + 35, 28)
    circle(c, x + 28, y + 35, 28)
    circle(c, x - 28, y + 35, 10, INNER)
    circle(c, x + 28, y + 35, 10, INNER)
    poly(c, [(x, y + 10), (x - 12, y - 8), (x + 12, y - 8)])
    ellipse(c, x - 55, y, 22, 40, INNER)
    ellipse(c, x + 55, y, 22, 40, INNER)
    line(c, x - 15, y - 95, x - 25, y - 125)
    line(c, x + 15, y - 95, x + 25, y - 125)


def turtle(c, x, y):
    ellipse(c, x, y, 110, 75)
    ellipse(c, x, y, 70, 45, INNER)
    circle(c, x + 125, y, 32)
    circle(c, x + 135, y + 8, 6, INNER)
    ellipse(c, x - 40, y + 85, 28, 16)
    ellipse(c, x + 40, y + 85, 28, 16)
    ellipse(c, x - 40, y - 85, 28, 16)
    ellipse(c, x + 40, y - 85, 28, 16)
    line(c, x - 20, y, x + 20, y, INNER)
    line(c, x, y - 20, x, y + 20, INNER)


def mouse(c, x, y):
    ellipse(c, x, y, 70, 40)
    circle(c, x + 55, y + 25, 32)
    circle(c, x + 35, y + 55, 22)
    circle(c, x + 75, y + 55, 22)
    circle(c, x + 48, y + 30, 6, INNER)
    circle(c, x + 68, y + 30, 6, INNER)
    line(c, x - 70, y, x - 140, y - 30)
    line(c, x + 20, y - 35, x + 10, y - 80)
    line(c, x + 50, y - 35, x + 60, y - 80)


def fox(c, x, y):
    ellipse(c, x, y - 10, 90, 50)
    poly(c, [(x + 70, y + 20), (x + 40, y + 95), (x + 110, y + 95), (x + 95, y + 20)])
    poly(c, [(x + 50, y + 95), (x + 35, y + 130), (x + 65, y + 100)])
    poly(c, [(x + 95, y + 95), (x + 120, y + 130), (x + 85, y + 100)])
    circle(c, x + 65, y + 55, 6, INNER)
    circle(c, x + 90, y + 55, 6, INNER)
    poly(c, [(x - 90, y), (x - 150, y + 20), (x - 90, y - 20)])
    line(c, x - 40, y - 50, x - 50, y - 110)
    line(c, x + 10, y - 55, x + 5, y - 115)
    line(c, x + 50, y - 50, x + 60, y - 110)


def elephant(c, x, y):
    ellipse(c, x, y, 110, 70)
    circle(c, x + 90, y + 40, 50)
    circle(c, x + 55, y + 70, 28)
    circle(c, x + 120, y + 70, 28)
    circle(c, x + 80, y + 50, 8, INNER)
    circle(c, x + 108, y + 50, 8, INNER)
    arc(c, x + 100, y - 80, x + 160, y + 40, 250, 200)
    line(c, x - 60, y - 55, x - 70, y - 130)
    line(c, x - 20, y - 70, x - 15, y - 135)
    line(c, x + 25, y - 70, x + 30, y - 135)
    line(c, x + 65, y - 55, x + 75, y - 125)


def lion(c, x, y):
    circle(c, x, y + 20, 55)
    for ang in range(0, 360, 30):
        from math import cos, radians, sin

        x1 = x + 55 * cos(radians(ang))
        y1 = y + 20 + 55 * sin(radians(ang))
        x2 = x + 90 * cos(radians(ang))
        y2 = y + 20 + 90 * sin(radians(ang))
        line(c, x1, y1, x2, y2)
    circle(c, x - 18, y + 30, 8, INNER)
    circle(c, x + 18, y + 30, 8, INNER)
    ellipse(c, x, y + 8, 14, 10, INNER)
    ellipse(c, x, y - 70, 70, 45)
    line(c, x - 40, y - 100, x - 50, y - 145)
    line(c, x + 40, y - 100, x + 50, y - 145)
    line(c, x + 70, y - 70, x + 120, y - 90)


def giraffe(c, x, y):
    ellipse(c, x, y - 40, 70, 45)
    rrect(c, x + 40, y - 20, 28, 140, 12)
    circle(c, x + 85, y + 130, 32)
    line(c, x + 75, y + 160, x + 70, y + 185)
    line(c, x + 95, y + 160, x + 100, y + 185)
    circle(c, x + 70, y + 188, 8)
    circle(c, x + 100, y + 188, 8)
    circle(c, x + 95, y + 135, 6, INNER)
    line(c, x - 40, y - 70, x - 50, y - 140)
    line(c, x - 10, y - 80, x - 5, y - 145)
    line(c, x + 25, y - 80, x + 30, y - 145)
    line(c, x + 50, y - 70, x + 60, y - 135)
    circle(c, x + 30, y + 40, 8, INNER)
    circle(c, x + 50, y + 80, 8, INNER)


def monkey(c, x, y):
    circle(c, x, y + 50, 50)
    ellipse(c, x, y + 40, 32, 28, INNER)
    circle(c, x - 15, y + 58, 7, INNER)
    circle(c, x + 15, y + 58, 7, INNER)
    circle(c, x - 48, y + 55, 18)
    circle(c, x + 48, y + 55, 18)
    ellipse(c, x, y - 40, 55, 50)
    arc(c, x - 90, y - 40, x - 40, y + 40, 90, 180)
    arc(c, x + 40, y - 40, x + 90, y + 40, 270, 180)
    line(c, x - 25, y - 85, x - 30, y - 125)
    line(c, x + 25, y - 85, x + 30, y - 125)


def panda(c, x, y):
    ellipse(c, x, y - 30, 85, 70)
    circle(c, x, y + 70, 52)
    ellipse(c, x - 22, y + 78, 16, 20)
    ellipse(c, x + 22, y + 78, 16, 20)
    circle(c, x - 22, y + 78, 7, INNER)
    circle(c, x + 22, y + 78, 7, INNER)
    ellipse(c, x, y + 48, 16, 12, INNER)
    circle(c, x - 40, y + 110, 16)
    circle(c, x + 40, y + 110, 16)
    line(c, x - 45, y - 80, x - 55, y - 125)
    line(c, x + 45, y - 80, x + 55, y - 125)


def whale(c, x, y):
    ellipse(c, x, y, 140, 55)
    poly(c, [(x - 140, y), (x - 200, y + 60), (x - 175, y), (x - 200, y - 45)])
    circle(c, x + 90, y + 10, 10, INNER)
    arc(c, x + 40, y - 5, x + 90, y + 20, 200, 120, INNER)
    poly(c, [(x - 20, y + 54), (x, y + 100), (x + 25, y + 54)])
    arc(c, x - 40, y - 90, x + 80, y - 20, 200, 140, INNER)


def crab(c, x, y):
    ellipse(c, x, y, 80, 45)
    circle(c, x - 30, y + 15, 8, INNER)
    circle(c, x + 30, y + 15, 8, INNER)
    line(c, x - 80, y + 10, x - 130, y + 50)
    line(c, x + 80, y + 10, x + 130, y + 50)
    circle(c, x - 145, y + 55, 22)
    circle(c, x + 145, y + 55, 22)
    for dx in (-50, -20, 20, 50):
        line(c, x + dx, y - 40, x + dx - 10, y - 85)
        line(c, x + dx, y - 40, x + dx + 10, y - 85)


def butterfly(c, x, y):
    ellipse(c, x - 70, y + 40, 55, 70)
    ellipse(c, x + 70, y + 40, 55, 70)
    ellipse(c, x - 65, y - 50, 45, 50)
    ellipse(c, x + 65, y - 50, 45, 50)
    rrect(c, x - 10, y - 80, 20, 160, 8)
    circle(c, x, y + 90, 14)
    line(c, x - 5, y + 102, x - 25, y + 130, INNER)
    line(c, x + 5, y + 102, x + 25, y + 130, INNER)
    circle(c, x - 70, y + 40, 18, INNER)
    circle(c, x + 70, y + 40, 18, INNER)


def bee(c, x, y):
    ellipse(c, x, y, 70, 45)
    line(c, x - 25, y + 40, x - 25, y - 40, INNER)
    line(c, x, y + 44, x, y - 44, INNER)
    line(c, x + 25, y + 40, x + 25, y - 40, INNER)
    circle(c, x + 70, y + 10, 22)
    circle(c, x + 78, y + 16, 5, INNER)
    ellipse(c, x - 20, y + 70, 35, 22)
    ellipse(c, x + 25, y + 70, 35, 22)
    line(c, x + 88, y + 5, x + 115, y, INNER)
    line(c, x - 40, y - 40, x - 40, y - 70, INNER)
    line(c, x + 10, y - 40, x + 10, y - 70, INNER)


def snail(c, x, y):
    circle(c, x - 20, y + 20, 70)
    circle(c, x - 20, y + 20, 45, INNER)
    circle(c, x - 20, y + 20, 22, INNER)
    ellipse(c, x + 50, y - 40, 80, 28)
    circle(c, x + 110, y - 20, 22)
    line(c, x + 118, y - 5, x + 118, y + 35, INNER)
    line(c, x + 130, y - 8, x + 140, y + 30, INNER)
    circle(c, x + 118, y + 40, 6, INNER)
    circle(c, x + 140, y + 35, 6, INNER)


def ladybug(c, x, y):
    ellipse(c, x, y, 80, 70)
    line(c, x, y + 70, x, y - 70, INNER)
    circle(c, x, y + 75, 28)
    circle(c, x - 10, y + 80, 5, INNER)
    circle(c, x + 10, y + 80, 5, INNER)
    circle(c, x - 35, y + 20, 14, INNER)
    circle(c, x + 35, y + 15, 14, INNER)
    circle(c, x - 30, y - 25, 12, INNER)
    circle(c, x + 40, y - 30, 12, INNER)
    line(c, x - 8, y + 100, x - 30, y + 125, INNER)
    line(c, x + 8, y + 100, x + 30, y + 125, INNER)


def hedgehog(c, x, y):
    ellipse(c, x, y, 90, 55)
    for i, (dx, dy) in enumerate(
        [(-40, 50), (-10, 70), (20, 75), (50, 60), (-55, 20), (60, 25), (-20, 40), (10, 45)]
    ):
        poly(c, [(x + dx, y + dy - 15), (x + dx, y + dy + 35), (x + dx + 18, y + dy - 10)])
    circle(c, x + 80, y, 28)
    circle(c, x + 90, y + 6, 6, INNER)
    ellipse(c, x + 100, y - 8, 10, 6, INNER)
    line(c, x - 40, y - 50, x - 45, y - 90)
    line(c, x + 20, y - 52, x + 25, y - 92)


def penguin(c, x, y):
    ellipse(c, x, y, 55, 95)
    ellipse(c, x, y - 10, 32, 60, INNER)
    circle(c, x, y + 95, 32)
    circle(c, x - 10, y + 100, 6, INNER)
    circle(c, x + 10, y + 100, 6, INNER)
    poly(c, [(x, y + 88), (x - 10, y + 75), (x + 10, y + 75)])
    ellipse(c, x - 55, y + 10, 18, 40)
    ellipse(c, x + 55, y + 10, 18, 40)
    ellipse(c, x - 18, y - 100, 22, 12)
    ellipse(c, x + 18, y - 100, 22, 12)


# --- vehicles ---

def car(c, x, y):
    rrect(c, x - 130, y - 10, 260, 70, 18)
    rrect(c, x - 70, y + 55, 140, 50, 14)
    circle(c, x - 80, y - 20, 28)
    circle(c, x + 80, y - 20, 28)
    circle(c, x - 80, y - 20, 12, INNER)
    circle(c, x + 80, y - 20, 12, INNER)
    rrect(c, x - 55, y + 65, 50, 30, 6, INNER)
    rrect(c, x + 10, y + 65, 50, 30, 6, INNER)


def dump_truck(c, x, y):
    rrect(c, x + 40, y, 90, 70, 10)
    rrect(c, x + 55, y + 20, 40, 28, 6, INNER)
    rrect(c, x - 140, y + 10, 175, 90, 8)
    line(c, x - 140, y + 55, x + 35, y + 55, INNER)
    circle(c, x - 90, y - 15, 26)
    circle(c, x - 20, y - 15, 26)
    circle(c, x + 85, y - 15, 26)
    circle(c, x - 90, y - 15, 10, INNER)
    circle(c, x - 20, y - 15, 10, INNER)
    circle(c, x + 85, y - 15, 10, INNER)


def fire_truck(c, x, y):
    rrect(c, x - 140, y, 280, 70, 8)
    rrect(c, x + 40, y + 70, 90, 55, 8)
    rrect(c, x - 120, y + 70, 140, 20, 4)
    rrect(c, x + 55, y + 85, 40, 28, 4, INNER)
    circle(c, x - 90, y - 10, 26)
    circle(c, x - 20, y - 10, 26)
    circle(c, x + 90, y - 10, 26)
    line(c, x - 40, y + 35, x + 20, y + 35, INNER)
    circle(c, x - 110, y + 35, 12, INNER)


def bus(c, x, y):
    rrect(c, x - 150, y, 300, 100, 16)
    for i in range(5):
        rrect(c, x - 120 + i * 48, y + 40, 36, 36, 6, INNER)
    rrect(c, x + 90, y + 20, 40, 55, 6, INNER)
    circle(c, x - 90, y - 10, 26)
    circle(c, x + 90, y - 10, 26)
    circle(c, x - 90, y - 10, 10, INNER)
    circle(c, x + 90, y - 10, 10, INNER)


def train(c, x, y):
    rrect(c, x - 40, y, 90, 90, 8)
    rrect(c, x - 25, y + 40, 40, 30, 4, INNER)
    rrect(c, x - 15, y + 90, 30, 35, 4)
    circle(c, x + 5, y + 140, 18)
    rrect(c, x - 150, y, 95, 70, 8)
    rrect(c, x + 65, y, 95, 70, 8)
    circle(c, x - 110, y - 15, 22)
    circle(c, x - 70, y - 15, 22)
    circle(c, x + 5, y - 15, 22)
    circle(c, x + 90, y - 15, 22)
    circle(c, x + 130, y - 15, 22)


def train_car(c, x, y):
    rrect(c, x - 140, y, 280, 90, 10)
    rrect(c, x - 110, y + 20, 70, 50, 6, INNER)
    rrect(c, x - 20, y + 20, 70, 50, 6, INNER)
    rrect(c, x + 70, y + 20, 70, 50, 6, INNER)
    circle(c, x - 80, y - 15, 24)
    circle(c, x + 80, y - 15, 24)
    line(c, x - 150, y + 40, x - 175, y + 40)
    line(c, x + 140, y + 40, x + 175, y + 40)


def plane(c, x, y):
    ellipse(c, x, y, 140, 32)
    poly(c, [(x - 10, y), (x - 40, y + 90), (x + 40, y)])
    poly(c, [(x - 10, y), (x - 40, y - 90), (x + 40, y)])
    poly(c, [(x - 130, y), (x - 170, y + 40), (x - 150, y), (x - 170, y - 40)])
    circle(c, x + 80, y + 8, 8, INNER)
    rrect(c, x + 100, y - 8, 40, 16, 6)


def helicopter(c, x, y):
    ellipse(c, x, y, 80, 40)
    rrect(c, x + 70, y - 8, 90, 16, 6)
    circle(c, x + 160, y, 18)
    line(c, x, y + 40, x, y + 70)
    line(c, x - 110, y + 70, x + 110, y + 70)
    line(c, x - 20, y + 70, x, y + 95, INNER)
    line(c, x + 20, y + 70, x, y + 95, INNER)
    rrect(c, x - 25, y - 8, 40, 22, 4, INNER)
    line(c, x - 30, y - 40, x - 50, y - 55)
    line(c, x + 30, y - 40, x + 50, y - 55)
    line(c, x - 50, y - 55, x + 50, y - 55)


def boat(c, x, y):
    poly(c, [(x - 140, y), (x + 140, y), (x + 100, y - 60), (x - 100, y - 60)])
    rrect(c, x - 40, y, 80, 50, 8)
    rrect(c, x - 20, y + 15, 40, 22, 4, INNER)
    line(c, x, y + 50, x, y + 130)
    poly(c, [(x, y + 125), (x + 70, y + 80), (x, y + 80)])


def sailboat(c, x, y):
    poly(c, [(x - 110, y - 20), (x + 110, y - 20), (x + 70, y - 70), (x - 70, y - 70)])
    line(c, x, y - 20, x, y + 140)
    poly(c, [(x, y + 135), (x + 90, y + 20), (x, y + 20)])
    poly(c, [(x, y + 100), (x - 70, y + 15), (x, y + 15)])


def bicycle(c, x, y):
    circle(c, x - 90, y - 40, 45)
    circle(c, x + 90, y - 40, 45)
    circle(c, x - 90, y - 40, 18, INNER)
    circle(c, x + 90, y - 40, 18, INNER)
    line(c, x - 90, y - 40, x, y + 40)
    line(c, x + 90, y - 40, x, y + 40)
    line(c, x - 90, y - 40, x + 90, y - 40)
    line(c, x, y + 40, x + 50, y + 70)
    circle(c, x + 50, y + 70, 16)
    line(c, x, y + 40, x - 20, y + 75)
    rrect(c, x - 40, y + 75, 40, 12, 4)


def scooter(c, x, y):
    line(c, x - 80, y - 20, x + 90, y - 20)
    circle(c, x - 80, y - 40, 22)
    circle(c, x + 90, y - 40, 22)
    line(c, x + 90, y - 20, x + 90, y + 90)
    line(c, x + 70, y + 90, x + 110, y + 90)
    rrect(c, x - 40, y - 12, 70, 14, 6)


def tractor(c, x, y):
    rrect(c, x - 20, y, 110, 70, 10)
    rrect(c, x + 10, y + 25, 45, 30, 6, INNER)
    rrect(c, x - 100, y + 10, 70, 40, 8)
    circle(c, x - 70, y - 10, 40)
    circle(c, x + 70, y - 5, 26)
    circle(c, x - 70, y - 10, 16, INNER)
    circle(c, x + 70, y - 5, 10, INNER)
    line(c, x + 90, y + 40, x + 90, y + 85)
    circle(c, x + 90, y + 95, 14)


def digger(c, x, y):
    rrect(c, x - 80, y, 120, 55, 10)
    rrect(c, x - 50, y + 55, 55, 40, 8)
    rrect(c, x - 40, y + 68, 30, 20, 4, INNER)
    circle(c, x - 50, y - 10, 28)
    circle(c, x + 20, y - 10, 28)
    line(c, x + 40, y + 40, x + 130, y + 90)
    line(c, x + 130, y + 90, x + 150, y + 20)
    poly(c, [(x + 140, y + 20), (x + 175, y + 10), (x + 160, y - 25), (x + 125, y - 5)])


def garbage_truck(c, x, y):
    rrect(c, x - 140, y, 180, 100, 8)
    rrect(c, x + 45, y, 85, 75, 8)
    rrect(c, x + 58, y + 25, 40, 30, 4, INNER)
    line(c, x - 140, y + 50, x + 40, y + 50, INNER)
    circle(c, x - 90, y - 15, 24)
    circle(c, x - 30, y - 15, 24)
    circle(c, x + 85, y - 15, 24)


def motorcycle(c, x, y):
    circle(c, x - 90, y - 30, 40)
    circle(c, x + 90, y - 30, 40)
    circle(c, x - 90, y - 30, 16, INNER)
    circle(c, x + 90, y - 30, 16, INNER)
    line(c, x - 90, y - 30, x + 20, y + 30)
    line(c, x + 90, y - 30, x + 20, y + 30)
    ellipse(c, x + 10, y + 40, 40, 16)
    line(c, x + 40, y + 40, x + 80, y + 85)
    line(c, x + 60, y + 85, x + 95, y + 85)


def rocket(c, x, y):
    ellipse(c, x, y + 20, 40, 110)
    circle(c, x, y + 130, 28)
    poly(c, [(x - 40, y - 40), (x - 80, y - 90), (x - 20, y - 70)])
    poly(c, [(x + 40, y - 40), (x + 80, y - 90), (x + 20, y - 70)])
    poly(c, [(x - 18, y - 80), (x, y - 140), (x + 18, y - 80)])
    circle(c, x, y + 40, 16, INNER)
    circle(c, x, y, 16, INNER)


def submarine(c, x, y):
    ellipse(c, x, y, 140, 45)
    rrect(c, x - 20, y + 40, 50, 35, 8)
    line(c, x + 5, y + 75, x + 5, y + 110)
    circle(c, x + 5, y + 118, 10)
    circle(c, x - 40, y + 5, 10, INNER)
    circle(c, x, y + 5, 10, INNER)
    circle(c, x + 40, y + 5, 10, INNER)
    poly(c, [(x - 140, y), (x - 180, y + 25), (x - 180, y - 25)])
    ellipse(c, x + 80, y - 50, 30, 12)


def cement_mixer(c, x, y):
    rrect(c, x + 30, y, 90, 65, 8)
    rrect(c, x + 45, y + 20, 40, 28, 4, INNER)
    ellipse(c, x - 70, y + 40, 70, 50)
    ellipse(c, x - 70, y + 40, 40, 28, INNER)
    circle(c, x - 90, y - 15, 24)
    circle(c, x - 30, y - 15, 24)
    circle(c, x + 80, y - 15, 24)


def tow_truck(c, x, y):
    rrect(c, x + 20, y, 100, 60, 8)
    rrect(c, x + 40, y + 18, 45, 28, 4, INNER)
    rrect(c, x - 120, y, 130, 35, 6)
    line(c, x + 20, y + 50, x - 80, y + 90)
    line(c, x - 80, y + 90, x - 110, y + 20)
    circle(c, x - 110, y + 20, 10)
    circle(c, x - 70, y - 15, 24)
    circle(c, x + 70, y - 15, 24)


def van(c, x, y):
    rrect(c, x - 140, y, 280, 90, 18)
    rrect(c, x - 120, y + 30, 70, 40, 6, INNER)
    rrect(c, x - 30, y + 30, 70, 40, 6, INNER)
    rrect(c, x + 60, y + 30, 55, 40, 6, INNER)
    circle(c, x - 80, y - 15, 26)
    circle(c, x + 80, y - 15, 26)


def pickup(c, x, y):
    rrect(c, x + 20, y, 100, 70, 10)
    rrect(c, x + 40, y + 25, 50, 30, 6, INNER)
    rrect(c, x - 140, y, 155, 40, 8)
    circle(c, x - 80, y - 15, 26)
    circle(c, x + 80, y - 15, 26)


def crane(c, x, y):
    rrect(c, x - 90, y, 130, 50, 8)
    rrect(c, x - 50, y + 50, 50, 35, 6)
    line(c, x + 40, y + 40, x + 130, y + 140)
    line(c, x + 130, y + 140, x + 130, y + 40)
    circle(c, x + 130, y + 30, 14)
    circle(c, x - 60, y - 15, 24)
    circle(c, x + 20, y - 15, 24)


def wagon(c, x, y):
    rrect(c, x - 100, y, 200, 70, 12)
    line(c, x - 100, y + 35, x - 160, y + 55)
    circle(c, x - 165, y + 55, 10)
    circle(c, x - 60, y - 15, 24)
    circle(c, x + 60, y - 15, 24)
    circle(c, x, y + 20, 16, INNER)


# --- foods ---

def apple(c, x, y):
    circle(c, x, y, 80)
    line(c, x, y + 80, x + 10, y + 120)
    ellipse(c, x + 35, y + 115, 30, 14)
    ellipse(c, x - 50, y + 20, 16, 28, INNER)


def banana(c, x, y):
    arc(c, x - 100, y - 80, x + 100, y + 80, 200, 140)
    arc(c, x - 70, y - 50, x + 70, y + 50, 200, 140)
    line(c, x + 70, y + 55, x + 90, y + 85)
    line(c, x - 70, y - 40, x - 90, y - 20)


def grapes(c, x, y):
    for dx, dy in [
        (0, 40),
        (-30, 10),
        (30, 10),
        (-50, -25),
        (0, -25),
        (50, -25),
        (-30, -60),
        (30, -60),
        (0, -90),
    ]:
        circle(c, x + dx, y + dy, 22)
    line(c, x, y + 62, x + 10, y + 100)
    ellipse(c, x + 30, y + 105, 22, 12)


def watermelon(c, x, y):
    arc(c, x - 120, y - 80, x + 120, y + 100, 200, 160)
    arc(c, x - 90, y - 50, x + 90, y + 80, 200, 160, INNER)
    circle(c, x - 30, y, 8, INNER)
    circle(c, x + 20, y + 15, 8, INNER)
    circle(c, x + 10, y - 25, 8, INNER)
    circle(c, x - 15, y - 30, 8, INNER)


def carrot(c, x, y):
    poly(c, [(x, y + 90), (x - 40, y - 100), (x + 40, y - 100)])
    line(c, x, y + 90, x - 25, y + 140, INNER)
    line(c, x, y + 90, x, y + 150, INNER)
    line(c, x, y + 90, x + 25, y + 140, INNER)


def ice_cream(c, x, y):
    poly(c, [(x - 50, y + 20), (x + 50, y + 20), (x, y - 120)])
    circle(c, x, y + 55, 50)
    circle(c, x - 28, y + 90, 28)
    circle(c, x + 28, y + 90, 28)
    circle(c, x, y + 115, 26)
    ellipse(c, x, y + 20, 52, 14)


def cupcake(c, x, y):
    poly(c, [(x - 55, y + 10), (x + 55, y + 10), (x + 40, y - 70), (x - 40, y - 70)])
    ellipse(c, x, y + 20, 70, 22)
    circle(c, x - 25, y + 50, 28)
    circle(c, x + 25, y + 50, 28)
    circle(c, x, y + 78, 24)
    line(c, x, y + 100, x, y + 125, INNER)
    circle(c, x, y + 132, 10)


def cookie(c, x, y):
    circle(c, x, y, 85)
    for dx, dy in [(-25, 20), (20, 25), (5, -20), (-30, -25), (35, -5), (0, 5)]:
        circle(c, x + dx, y + dy, 10, INNER)


def pizza(c, x, y):
    poly(c, [(x, y + 110), (x - 100, y - 80), (x + 100, y - 80)])
    arc(c, x - 40, y + 20, x + 40, y + 80, 200, 140, INNER)
    circle(c, x - 20, y + 10, 14, INNER)
    circle(c, x + 30, y, 14, INNER)
    circle(c, x, y - 30, 14, INNER)


def bread(c, x, y):
    ellipse(c, x, y, 110, 55)
    arc(c, x - 70, y, x - 20, y + 40, 20, 160, INNER)
    arc(c, x - 10, y, x + 40, y + 40, 20, 160, INNER)
    arc(c, x + 30, y, x + 80, y + 40, 20, 160, INNER)


def pear(c, x, y):
    circle(c, x, y - 40, 55)
    circle(c, x, y + 40, 40)
    line(c, x, y + 80, x + 8, y + 115)
    ellipse(c, x + 28, y + 110, 22, 12)


def strawberry(c, x, y):
    poly(c, [(x, y - 90), (x - 70, y + 40), (x + 70, y + 40)])
    ellipse(c, x, y + 55, 50, 18)
    line(c, x, y + 70, x, y + 105)
    circle(c, x - 20, y, 6, INNER)
    circle(c, x + 15, y + 10, 6, INNER)
    circle(c, x, y - 25, 6, INNER)
    circle(c, x - 25, y - 35, 6, INNER)
    circle(c, x + 25, y - 20, 6, INNER)


def orange(c, x, y):
    circle(c, x, y, 80)
    circle(c, x, y, 12, INNER)
    for dx, dy in [(0, 40), (35, 20), (35, -20), (0, -40), (-35, -20), (-35, 20)]:
        line(c, x, y, x + dx, y + dy, INNER)
    ellipse(c, x + 15, y + 85, 18, 10)


def donut(c, x, y):
    circle(c, x, y, 80)
    circle(c, x, y, 30)
    arc(c, x - 50, y + 10, x + 20, y + 70, 20, 140, INNER)
    circle(c, x + 40, y + 20, 8, INNER)
    circle(c, x - 35, y - 25, 8, INNER)
    circle(c, x + 15, y - 40, 8, INNER)


def sandwich(c, x, y):
    rrect(c, x - 90, y - 20, 180, 80, 12)
    line(c, x - 90, y + 20, x + 90, y + 20, INNER)
    ellipse(c, x - 20, y + 5, 30, 12, INNER)
    ellipse(c, x + 30, y + 8, 24, 10, INNER)
    rrect(c, x - 70, y + 60, 140, 18, 6)


def cheese(c, x, y):
    poly(c, [(x - 90, y - 50), (x + 100, y - 50), (x + 70, y + 70), (x - 60, y + 70)])
    line(c, x - 60, y + 70, x - 90, y - 50)
    circle(c, x - 20, y + 10, 16, INNER)
    circle(c, x + 30, y, 12, INNER)
    circle(c, x + 10, y - 25, 14, INNER)


def milk(c, x, y):
    rrect(c, x - 40, y - 90, 80, 150, 12)
    rrect(c, x - 22, y + 60, 44, 35, 8)
    ellipse(c, x, y + 60, 40, 10)
    line(c, x - 25, y - 20, x + 25, y - 20, INNER)


def corn(c, x, y):
    ellipse(c, x, y, 40, 110)
    for row in range(-3, 4):
        for col in (-1, 1, 0):
            circle(c, x + col * 16, y + row * 24, 8, INNER)
    poly(c, [(x - 40, y + 40), (x - 80, y + 100), (x - 20, y + 80)])
    poly(c, [(x + 40, y + 40), (x + 80, y + 100), (x + 20, y + 80)])


def mushroom(c, x, y):
    rrect(c, x - 22, y - 80, 44, 80, 10)
    ellipse(c, x, y + 20, 90, 50)
    circle(c, x - 30, y + 20, 10, INNER)
    circle(c, x + 10, y + 35, 10, INNER)
    circle(c, x + 35, y + 10, 10, INNER)


# --- objects ---

def ball(c, x, y):
    circle(c, x, y, 85)
    ellipse(c, x, y, 85, 28, INNER)
    line(c, x, y + 85, x, y - 85, INNER)


def balloon(c, x, y):
    ellipse(c, x, y + 40, 50, 70)
    poly(c, [(x - 12, y - 30), (x, y - 50), (x + 12, y - 30)])
    line(c, x, y - 50, x - 10, y - 130)


def kite(c, x, y):
    poly(c, [(x, y + 110), (x + 70, y), (x, y - 70), (x - 70, y)])
    line(c, x - 70, y, x + 70, y, INNER)
    line(c, x, y + 110, x, y - 70, INNER)
    line(c, x, y - 70, x + 30, y - 130)
    line(c, x + 20, y - 100, x + 50, y - 95, INNER)
    line(c, x + 25, y - 115, x + 55, y - 110, INNER)


def house(c, x, y):
    rrect(c, x - 90, y - 70, 180, 110, 4)
    poly(c, [(x - 110, y + 40), (x, y + 130), (x + 110, y + 40)])
    rrect(c, x - 25, y - 70, 50, 70, 4)
    circle(c, x + 18, y - 30, 6, INNER)
    rrect(c, x - 70, y - 10, 35, 35, 4, INNER)
    rrect(c, x + 40, y - 10, 35, 35, 4, INNER)


def tree(c, x, y):
    rrect(c, x - 18, y - 110, 36, 90, 6)
    circle(c, x, y + 40, 70)
    circle(c, x - 45, y + 10, 40)
    circle(c, x + 45, y + 10, 40)


def flower(c, x, y):
    line(c, x, y - 110, x, y)
    ellipse(c, x - 25, y - 40, 18, 30, INNER)
    for dx, dy in [(0, 40), (38, 12), (24, -32), (-24, -32), (-38, 12)]:
        ellipse(c, x + dx, y + dy + 20, 22, 30)
    circle(c, x, y + 20, 20)


def sun(c, x, y):
    circle(c, x, y, 55)
    for i in range(12):
        from math import cos, radians, sin

        a = i * 30
        line(
            c,
            x + 70 * cos(radians(a)),
            y + 70 * sin(radians(a)),
            x + 105 * cos(radians(a)),
            y + 105 * sin(radians(a)),
        )


def moon(c, x, y):
    circle(c, x, y, 80)
    circle(c, x + 30, y + 15, 60)
    circle(c, x - 30, y + 25, 12, INNER)
    circle(c, x + 10, y - 20, 8, INNER)


def star_shape(c, x, y):
    from math import cos, pi, sin

    pts = []
    for i in range(10):
        r = 90 if i % 2 == 0 else 38
        a = -pi / 2 + i * pi / 5
        pts.append((x + r * cos(a), y + r * sin(a)))
    poly(c, pts)


def cloud(c, x, y):
    circle(c, x - 50, y, 45)
    circle(c, x + 10, y + 20, 55)
    circle(c, x + 60, y, 42)
    ellipse(c, x + 5, y - 25, 95, 35)


def book(c, x, y):
    rrect(c, x - 80, y - 70, 160, 140, 8)
    line(c, x, y - 70, x, y + 70)
    line(c, x - 50, y + 40, x - 15, y + 40, INNER)
    line(c, x + 15, y + 40, x + 50, y + 40, INNER)
    line(c, x - 50, y + 10, x - 15, y + 10, INNER)


def pencil(c, x, y):
    rrect(c, x - 20, y - 90, 40, 160, 4)
    poly(c, [(x - 20, y + 70), (x, y + 120), (x + 20, y + 70)])
    line(c, x, y + 120, x, y + 70, INNER)
    rrect(c, x - 20, y - 110, 40, 22, 4)
    ellipse(c, x, y - 110, 20, 8)


def chair(c, x, y):
    rrect(c, x - 60, y, 120, 18, 6)
    rrect(c, x - 60, y + 18, 18, 100, 4)
    line(c, x - 50, y, x - 55, y - 70)
    line(c, x + 50, y, x + 55, y - 70)
    line(c, x - 45, y + 18, x - 45, y - 70)
    line(c, x + 45, y + 18, x + 45, y - 70)


def bed(c, x, y):
    rrect(c, x - 130, y - 20, 260, 50, 8)
    rrect(c, x - 130, y + 30, 18, 70, 4)
    rrect(c, x + 112, y + 30, 18, 50, 4)
    ellipse(c, x - 70, y + 40, 35, 20)
    rrect(c, x - 20, y + 28, 120, 22, 8)


def cup(c, x, y):
    rrect(c, x - 45, y - 60, 90, 90, 12)
    ellipse(c, x, y + 30, 45, 14)
    arc(c, x + 45, y - 20, x + 90, y + 40, 270, 180)


def spoon(c, x, y):
    ellipse(c, x, y + 70, 32, 42)
    rrect(c, x - 10, y - 100, 20, 140, 8)


def toothbrush(c, x, y):
    rrect(c, x - 12, y - 100, 24, 150, 8)
    rrect(c, x - 28, y + 50, 56, 50, 8)
    for i in range(5):
        line(c, x - 18 + i * 9, y + 55, x - 18 + i * 9, y + 95, INNER)


def teddy(c, x, y):
    ellipse(c, x, y - 20, 70, 80)
    circle(c, x, y + 75, 42)
    circle(c, x - 32, y + 110, 16)
    circle(c, x + 32, y + 110, 16)
    circle(c, x - 12, y + 78, 6, INNER)
    circle(c, x + 12, y + 78, 6, INNER)
    ellipse(c, x, y + 60, 12, 9, INNER)
    circle(c, x - 55, y + 10, 22)
    circle(c, x + 55, y + 10, 22)
    ellipse(c, x - 25, y - 100, 18, 12)
    ellipse(c, x + 25, y - 100, 18, 12)


def blocks(c, x, y):
    rrect(c, x - 90, y - 40, 70, 70, 6)
    rrect(c, x - 10, y - 40, 70, 70, 6)
    rrect(c, x - 50, y + 30, 70, 70, 6)


def drum(c, x, y):
    ellipse(c, x, y + 40, 80, 28)
    rrect(c, x - 80, y - 60, 160, 100, 8)
    ellipse(c, x, y - 60, 80, 28)
    line(c, x - 30, y + 80, x - 70, y + 120)
    line(c, x + 30, y + 80, x + 70, y + 120)
    circle(c, x - 75, y + 125, 10)
    circle(c, x + 75, y + 125, 10)


def clock(c, x, y):
    circle(c, x, y, 85)
    circle(c, x, y, 8, INNER)
    line(c, x, y, x, y + 50, INNER)
    line(c, x, y, x + 35, y - 10, INNER)
    circle(c, x - 40, y + 90, 12)
    circle(c, x + 40, y + 90, 12)


def umbrella(c, x, y):
    arc(c, x - 110, y - 20, x + 110, y + 100, 0, 180)
    line(c, x - 110, y + 40, x + 110, y + 40)
    line(c, x, y + 40, x, y - 90)
    arc(c, x, y - 110, x + 30, y - 80, 180, 180)
    line(c, x - 55, y + 40, x - 55, y + 85, INNER)
    line(c, x + 55, y + 40, x + 55, y + 85, INNER)


def backpack(c, x, y):
    rrect(c, x - 60, y - 80, 120, 150, 18)
    rrect(c, x - 40, y - 10, 80, 50, 10, INNER)
    ellipse(c, x, y + 70, 40, 12)
    arc(c, x - 90, y - 60, x - 50, y + 40, 90, 180)
    arc(c, x + 50, y - 60, x + 90, y + 40, 270, 180)


def socks(c, x, y):
    rrect(c, x - 80, y - 20, 40, 110, 16)
    ellipse(c, x - 85, y - 45, 40, 28)
    rrect(c, x + 20, y - 20, 40, 110, 16)
    ellipse(c, x + 15, y - 45, 40, 28)
    line(c, x - 80, y + 70, x - 40, y + 70, INNER)
    line(c, x + 20, y + 70, x + 60, y + 70, INNER)


def shoes(c, x, y):
    ellipse(c, x - 70, y, 70, 35)
    rrect(c, x - 90, y, 50, 40, 10)
    ellipse(c, x + 70, y, 70, 35)
    rrect(c, x + 40, y, 50, 40, 10)
    circle(c, x - 55, y + 10, 6, INNER)
    circle(c, x + 85, y + 10, 6, INNER)


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
]


def extra_pages() -> list[tuple[str, object]]:
    """Pad to 100 with distinct everyday extras if the main list is short."""
    extras = [
        ("leaf", lambda c, x, y: (
            ellipse(c, x, y, 40, 90),
            line(c, x, y + 90, x, y - 90, INNER),
            line(c, x, y + 20, x + 30, y + 40, INNER),
            line(c, x, y - 10, x - 28, y + 10, INNER),
        )),
        ("key", lambda c, x, y: (
            circle(c, x, y + 50, 32),
            circle(c, x, y + 50, 12, INNER),
            rrect(c, x - 10, y - 80, 20, 100, 4),
            line(c, x + 10, y - 50, x + 28, y - 50, INNER),
            line(c, x + 10, y - 70, x + 28, y - 70, INNER),
        )),
    ]
    return extras


assert len(PAGES) == 98, len(PAGES)
PAGES.extend(extra_pages())
assert len(PAGES) == 100, len(PAGES)
