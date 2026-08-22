"""100 unique toddler truck/construction drawings: closed black stroke, white fill."""

from __future__ import annotations

from math import atan2, cos, degrees, hypot, radians, sin

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
    dx, dy = x2 - x1, y2 - y1
    length = hypot(dx, dy)
    if length < 1:
        circle(c, x1, y1, r, w)
        return
    c.saveState()
    _stroke(c, w)
    c.translate(x1, y1)
    c.rotate(degrees(atan2(dy, dx)))
    c.roundRect(-r, -r, length + 2 * r, 2 * r, r, stroke=1, fill=1)
    c.restoreState()


def _wheel(c, x, y, r=28) -> None:
    circle(c, x, y, r)
    circle(c, x, y, r * 0.4, INNER)


def _cab(c, x, y, w=90, h=80) -> None:
    rrect(c, x, y, w, h, 10)
    rrect(c, x + 14, y + 22, w * 0.52, h * 0.42, 8, INNER)


def _tracks(c, x, y, w=160, h=28) -> None:
    rrect(c, x, y, w, h, 12)
    rrect(c, x + 10, y + 6, w - 20, h - 12, 8, INNER)


def dump_truck(c, x, y):
    _cab(c, x - 130, y + 8)
    rrect(c, x - 40, y - 8, 160, 72, 12)
    _wheel(c, x - 85, y - 28, 24)
    _wheel(c, x + 20, y - 28, 24)
    _wheel(c, x + 95, y - 28, 24)


def dump_up(c, x, y):
    _cab(c, x - 130, y + 8)
    poly(c, [(x - 40, y + 8), (x + 130, y + 95), (x + 150, y + 55), (x - 20, y - 8)])
    _wheel(c, x - 85, y - 28, 24)
    _wheel(c, x + 10, y - 28, 24)
    _wheel(c, x + 85, y - 28, 24)


def mini_dump(c, x, y):
    _cab(c, x - 90, y, 70, 65)
    rrect(c, x - 20, y - 8, 100, 50, 10)
    _wheel(c, x - 50, y - 28, 22)
    _wheel(c, x + 55, y - 28, 22)


def digger(c, x, y):
    rrect(c, x - 80, y - 5, 130, 55, 12)
    rrect(c, x - 50, y + 48, 55, 42, 8)
    rrect(c, x - 40, y + 58, 32, 22, 6, INNER)
    capsule(c, x + 40, y + 30, x + 120, y + 90, 12)
    poly(c, [(x + 118, y + 90), (x + 165, y + 70), (x + 155, y + 40), (x + 110, y + 70)])
    _wheel(c, x - 55, y - 28, 26)
    _wheel(c, x + 25, y - 28, 26)


def long_digger(c, x, y):
    rrect(c, x - 90, y - 8, 120, 50, 12)
    rrect(c, x - 60, y + 40, 48, 38, 8)
    rrect(c, x - 50, y + 50, 28, 20, 6, INNER)
    capsule(c, x + 20, y + 28, x + 90, y + 80, 11)
    capsule(c, x + 90, y + 80, x + 160, y + 40, 10)
    poly(c, [(x + 155, y + 40), (x + 195, y + 20), (x + 175, y - 5), (x + 140, y + 25)])
    _wheel(c, x - 60, y - 28, 24)
    _wheel(c, x + 10, y - 28, 24)


def mini_digger(c, x, y):
    rrect(c, x - 50, y - 5, 90, 42, 10)
    rrect(c, x - 30, y + 35, 40, 32, 8)
    rrect(c, x - 22, y + 44, 24, 16, 5, INNER)
    capsule(c, x + 30, y + 20, x + 95, y + 70, 9)
    poly(c, [(x + 92, y + 70), (x + 125, y + 55), (x + 115, y + 30), (x + 85, y + 52)])
    _wheel(c, x - 30, y - 24, 20)
    _wheel(c, x + 25, y - 24, 20)


def bulldozer(c, x, y):
    rrect(c, x - 50, y, 140, 70, 12)
    rrect(c, x - 20, y + 68, 70, 42, 10)
    rrect(c, x - 8, y + 78, 44, 24, 6, INNER)
    poly(c, [(x - 130, y - 20), (x - 50, y - 20), (x - 50, y + 70), (x - 130, y + 40)])
    _tracks(c, x - 70, y - 38, 180, 30)


def loader(c, x, y):
    rrect(c, x - 40, y - 5, 130, 60, 12)
    rrect(c, x - 10, y + 52, 60, 42, 10)
    rrect(c, x + 2, y + 62, 36, 22, 6, INNER)
    capsule(c, x - 40, y + 20, x - 120, y + 50, 12)
    poly(c, [(x - 170, y + 10), (x - 120, y + 70), (x - 100, y + 40), (x - 150, y - 10)])
    _wheel(c, x - 20, y - 28, 28)
    _wheel(c, x + 70, y - 28, 28)


def front_loader(c, x, y):
    rrect(c, x - 20, y, 140, 55, 12)
    rrect(c, x + 20, y + 52, 55, 40, 8)
    rrect(c, x + 30, y + 62, 32, 20, 6, INNER)
    poly(c, [(x - 150, y - 20), (x - 40, y + 10), (x - 40, y + 55), (x - 150, y + 80)])
    _wheel(c, x, y - 28, 30)
    _wheel(c, x + 95, y - 28, 26)


def skid_steer(c, x, y):
    rrect(c, x - 40, y - 5, 100, 70, 14)
    rrect(c, x - 22, y + 22, 64, 32, 8, INNER)
    poly(c, [(x - 110, y - 15), (x - 40, y + 10), (x - 40, y + 45), (x - 110, y + 55)])
    _tracks(c, x - 55, y - 38, 130, 26)


def backhoe(c, x, y):
    rrect(c, x - 40, y - 5, 110, 50, 12)
    rrect(c, x - 15, y + 42, 50, 38, 8)
    rrect(c, x - 5, y + 52, 28, 20, 6, INNER)
    poly(c, [(x - 120, y), (x - 40, y + 8), (x - 40, y + 40), (x - 120, y + 28)])
    capsule(c, x + 70, y + 20, x + 130, y + 80, 10)
    poly(c, [(x + 128, y + 80), (x + 170, y + 60), (x + 155, y + 30), (x + 118, y + 62)])
    _wheel(c, x - 20, y - 28, 24)
    _wheel(c, x + 55, y - 28, 24)


def grader(c, x, y):
    rrect(c, x - 40, y + 5, 90, 45, 10)
    rrect(c, x - 20, y + 48, 45, 32, 8)
    rrect(c, x - 12, y + 56, 28, 16, 5, INNER)
    rrect(c, x - 160, y - 8, 280, 22, 8)
    poly(c, [(x - 80, y - 20), (x + 40, y - 20), (x + 50, y + 8), (x - 90, y + 8)])
    _wheel(c, x - 120, y - 28, 20)
    _wheel(c, x - 20, y - 28, 22)
    _wheel(c, x + 90, y - 28, 22)


def steamroller(c, x, y):
    rrect(c, x - 20, y, 110, 55, 12)
    rrect(c, x + 10, y + 52, 55, 40, 10)
    rrect(c, x + 20, y + 62, 32, 22, 6, INNER)
    ellipse(c, x - 90, y, 40, 55)
    ellipse(c, x - 90, y, 22, 35, INNER)
    _wheel(c, x + 70, y - 22, 32)


def road_roller(c, x, y):
    rrect(c, x - 30, y + 5, 120, 50, 12)
    rrect(c, x, y + 52, 50, 36, 8)
    rrect(c, x + 10, y + 60, 30, 18, 5, INNER)
    ellipse(c, x - 95, y - 5, 36, 48)
    ellipse(c, x + 95, y - 5, 36, 48)


def forklift(c, x, y):
    rrect(c, x - 20, y - 5, 90, 70, 10)
    rrect(c, x - 5, y + 18, 50, 32, 8, INNER)
    rrect(c, x + 70, y - 20, 18, 130, 6)
    rrect(c, x + 88, y + 85, 90, 12, 4)
    rrect(c, x + 88, y + 55, 90, 12, 4)
    _wheel(c, x - 5, y - 28, 22)
    _wheel(c, x + 50, y - 28, 22)


def cement_mixer(c, x, y):
    _cab(c, x - 130, y + 5, 90, 70)
    ellipse(c, x + 30, y + 30, 70, 50)
    ellipse(c, x + 30, y + 30, 48, 32, INNER)
    rrect(c, x - 40, y - 8, 50, 40, 8)
    _wheel(c, x - 80, y - 28, 24)
    _wheel(c, x + 20, y - 28, 24)
    _wheel(c, x + 80, y - 28, 24)


def mixer_truck(c, x, y):
    _cab(c, x - 140, y, 85, 72)
    ellipse(c, x + 10, y + 40, 80, 55)
    circle(c, x + 10, y + 40, 22, INNER)
    _wheel(c, x - 90, y - 28, 24)
    _wheel(c, x - 10, y - 28, 24)
    _wheel(c, x + 70, y - 28, 24)


def crane(c, x, y):
    rrect(c, x - 90, y - 8, 130, 50, 10)
    capsule(c, x + 20, y + 40, x + 20, y + 140, 12)
    capsule(c, x + 20, y + 140, x + 130, y + 100, 10)
    circle(c, x + 138, y + 92, 10)
    capsule(c, x + 138, y + 82, x + 138, y + 40, 4, INNER)
    rrect(c, x + 118, y + 18, 40, 22, 4)
    _wheel(c, x - 55, y - 28, 24)
    _wheel(c, x + 20, y - 28, 24)


def tower_crane(c, x, y):
    rrect(c, x - 18, y - 40, 36, 160, 6)
    rrect(c, x - 140, y + 118, 260, 18, 6)
    rrect(c, x - 30, y + 136, 50, 28, 6)
    capsule(c, x + 100, y + 118, x + 100, y + 50, 4, INNER)
    rrect(c, x + 80, y + 30, 40, 22, 4)
    rrect(c, x - 50, y - 55, 100, 18, 6)


def crawler_crane(c, x, y):
    _tracks(c, x - 80, y - 40, 160, 32)
    rrect(c, x - 50, y - 8, 100, 45, 10)
    capsule(c, x, y + 35, x + 40, y + 130, 12)
    capsule(c, x + 40, y + 130, x + 140, y + 80, 10)
    circle(c, x + 148, y + 72, 10)


def cherry_picker(c, x, y):
    _cab(c, x - 110, y, 80, 65)
    rrect(c, x - 30, y - 8, 90, 28, 8)
    capsule(c, x + 40, y + 20, x + 100, y + 90, 10)
    rrect(c, x + 85, y + 90, 50, 32, 8)
    rrect(c, x + 95, y + 100, 28, 14, 4, INNER)
    _wheel(c, x - 70, y - 28, 22)
    _wheel(c, x + 30, y - 28, 22)


def boom_truck(c, x, y):
    _cab(c, x - 130, y + 5)
    rrect(c, x - 40, y - 8, 150, 32, 8)
    capsule(c, x + 20, y + 24, x + 20, y + 120, 11)
    capsule(c, x + 20, y + 120, x + 110, y + 70, 9)
    rrect(c, x + 95, y + 55, 40, 24, 6)
    _wheel(c, x - 80, y - 28, 22)
    _wheel(c, x + 20, y - 28, 22)
    _wheel(c, x + 85, y - 28, 22)


def paver(c, x, y):
    rrect(c, x - 110, y, 220, 55, 12)
    rrect(c, x - 40, y + 52, 70, 40, 10)
    rrect(c, x - 28, y + 62, 44, 22, 6, INNER)
    poly(c, [(x - 110, y), (x - 150, y - 25), (x + 150, y - 25), (x + 110, y)])
    _tracks(c, x - 90, y - 42, 180, 26)


def tanker(c, x, y):
    _cab(c, x - 140, y + 5, 85, 70)
    ellipse(c, x + 20, y + 18, 120, 42)
    circle(c, x - 40, y + 40, 10, INNER)
    circle(c, x + 20, y + 40, 10, INNER)
    circle(c, x + 80, y + 40, 10, INNER)
    _wheel(c, x - 90, y - 28, 24)
    _wheel(c, x + 10, y - 28, 24)
    _wheel(c, x + 90, y - 28, 24)


def tanker_truck(c, x, y):
    _cab(c, x - 145, y, 80, 68)
    ellipse(c, x + 15, y + 22, 130, 38)
    rrect(c, x - 20, y + 48, 18, 18, 4)
    _wheel(c, x - 95, y - 28, 22)
    _wheel(c, x - 10, y - 28, 22)
    _wheel(c, x + 70, y - 28, 22)
    _wheel(c, x + 115, y - 28, 22)


def flatbed(c, x, y):
    _cab(c, x - 140, y + 8)
    rrect(c, x - 50, y - 8, 200, 22, 8)
    _wheel(c, x - 90, y - 28, 22)
    _wheel(c, x + 20, y - 28, 22)
    _wheel(c, x + 110, y - 28, 22)


def logging_truck(c, x, y):
    _cab(c, x - 140, y + 8)
    rrect(c, x - 50, y - 8, 190, 18, 6)
    ellipse(c, x + 20, y + 28, 90, 16)
    ellipse(c, x + 20, y + 50, 90, 16)
    ellipse(c, x + 20, y + 72, 90, 16)
    _wheel(c, x - 90, y - 28, 22)
    _wheel(c, x + 30, y - 28, 22)
    _wheel(c, x + 110, y - 28, 22)


def snowplow(c, x, y):
    _cab(c, x - 40, y + 5, 90, 75)
    rrect(c, x - 40, y - 8, 140, 28, 8)
    poly(c, [(x - 140, y - 30), (x - 40, y - 8), (x - 40, y + 50), (x - 150, y + 20)])
    _wheel(c, x - 10, y - 28, 24)
    _wheel(c, x + 80, y - 28, 24)


def sweeper(c, x, y):
    _cab(c, x - 90, y + 8, 80, 70)
    rrect(c, x - 10, y - 8, 120, 70, 12)
    ellipse(c, x + 20, y - 32, 28, 14)
    ellipse(c, x + 80, y - 32, 28, 14)
    _wheel(c, x - 50, y - 22, 20)
    _wheel(c, x + 90, y - 22, 22)


def garbage_truck(c, x, y):
    rrect(c, x - 30, y - 8, 160, 90, 12)
    _cab(c, x - 130, y + 5, 100, 70)
    rrect(c, x + 90, y + 40, 28, 50, 6)
    _wheel(c, x - 80, y - 28, 24)
    _wheel(c, x + 20, y - 28, 24)
    _wheel(c, x + 90, y - 28, 24)


def dumpster(c, x, y):
    poly(c, [(x - 120, y - 20), (x + 120, y - 20), (x + 100, y + 70), (x - 100, y + 70)])
    rrect(c, x - 90, y + 20, 50, 28, 6, INNER)
    rrect(c, x + 40, y + 20, 50, 28, 6, INNER)
    rrect(c, x - 40, y - 40, 80, 18, 6)


def concrete_pump(c, x, y):
    _cab(c, x - 120, y, 80, 65)
    rrect(c, x - 40, y - 8, 90, 30, 8)
    capsule(c, x + 30, y + 22, x + 30, y + 110, 11)
    capsule(c, x + 30, y + 110, x + 130, y + 70, 9)
    capsule(c, x + 130, y + 70, x + 160, y + 20, 8)
    _wheel(c, x - 80, y - 28, 22)
    _wheel(c, x + 20, y - 28, 22)


def pile_driver(c, x, y):
    _tracks(c, x - 70, y - 40, 140, 28)
    rrect(c, x - 40, y - 10, 80, 40, 10)
    rrect(c, x - 12, y + 28, 24, 130, 6)
    rrect(c, x - 28, y + 140, 56, 28, 6)


def drill_rig(c, x, y):
    _tracks(c, x - 80, y - 38, 150, 28)
    rrect(c, x - 50, y - 8, 90, 40, 10)
    poly(c, [(x - 20, y + 30), (x + 20, y + 30), (x + 8, y + 150), (x - 8, y + 150)])
    circle(c, x, y + 160, 12)


def tow_truck(c, x, y):
    _cab(c, x - 130, y + 5, 100, 65)
    rrect(c, x - 30, y - 8, 150, 28, 8)
    capsule(c, x + 20, y + 20, x + 110, y + 80, 10)
    circle(c, x + 118, y + 88, 12)
    _wheel(c, x - 80, y - 28, 24)
    _wheel(c, x + 40, y - 28, 24)
    _wheel(c, x + 95, y - 28, 24)


def pickup(c, x, y):
    rrect(c, x - 20, y - 8, 140, 50, 10)
    _cab(c, x - 130, y - 8, 110, 70)
    _wheel(c, x - 75, y - 28, 26)
    _wheel(c, x + 70, y - 28, 26)


def work_van(c, x, y):
    rrect(c, x - 130, y - 10, 260, 80, 18)
    rrect(c, x - 40, y + 68, 150, 42, 12)
    rrect(c, x - 20, y + 78, 50, 24, 6, INNER)
    rrect(c, x + 45, y + 78, 50, 24, 6, INNER)
    rrect(c, x - 110, y + 18, 40, 28, 6, INNER)
    _wheel(c, x - 75, y - 28, 26)
    _wheel(c, x + 75, y - 28, 26)


def car(c, x, y):
    rrect(c, x - 120, y - 20, 240, 70, 22)
    rrect(c, x - 70, y + 48, 140, 48, 16)
    rrect(c, x - 55, y + 58, 50, 28, 8, INNER)
    rrect(c, x + 8, y + 58, 50, 28, 8, INNER)
    _wheel(c, x - 70, y - 28)
    _wheel(c, x + 70, y - 28)


def taxi(c, x, y):
    rrect(c, x - 115, y - 18, 230, 68, 20)
    rrect(c, x - 65, y + 48, 130, 44, 14)
    rrect(c, x - 50, y + 58, 46, 24, 6, INNER)
    rrect(c, x + 8, y + 58, 46, 24, 6, INNER)
    rrect(c, x - 18, y + 92, 36, 14, 4)
    _wheel(c, x - 70, y - 28)
    _wheel(c, x + 70, y - 28)


def jeep(c, x, y):
    rrect(c, x - 100, y - 10, 200, 70, 14)
    rrect(c, x - 50, y + 58, 100, 40, 10)
    rrect(c, x - 38, y + 68, 36, 22, 6, INNER)
    rrect(c, x + 4, y + 68, 36, 22, 6, INNER)
    _wheel(c, x - 70, y - 28, 32)
    _wheel(c, x + 70, y - 28, 32)


def convertible(c, x, y):
    rrect(c, x - 125, y - 18, 250, 50, 18)
    rrect(c, x - 20, y + 30, 70, 28, 10)
    rrect(c, x - 10, y + 38, 40, 14, 5, INNER)
    _wheel(c, x - 75, y - 28)
    _wheel(c, x + 75, y - 28)


def race_car(c, x, y):
    ellipse(c, x, y, 140, 32)
    rrect(c, x - 30, y + 20, 70, 28, 10)
    rrect(c, x - 18, y + 28, 44, 14, 5, INNER)
    poly(c, [(x - 40, y + 8), (x - 70, y + 40), (x - 20, y + 18)])
    _wheel(c, x - 80, y - 18, 22)
    _wheel(c, x + 80, y - 18, 22)


def monster_truck(c, x, y):
    rrect(c, x - 90, y + 20, 180, 50, 14)
    rrect(c, x - 40, y + 68, 80, 36, 10)
    rrect(c, x - 28, y + 76, 54, 20, 6, INNER)
    _wheel(c, x - 70, y - 20, 48)
    _wheel(c, x + 70, y - 20, 48)


def limo(c, x, y):
    rrect(c, x - 170, y - 15, 340, 50, 16)
    rrect(c, x + 40, y + 32, 90, 36, 12)
    rrect(c, x + 55, y + 42, 50, 18, 6, INNER)
    for i in range(4):
        rrect(c, x - 140 + i * 42, y + 8, 28, 18, 4, INNER)
    _wheel(c, x - 110, y - 28, 24)
    _wheel(c, x + 110, y - 28, 24)


def van(c, x, y):
    rrect(c, x - 130, y - 10, 260, 90, 18)
    rrect(c, x + 20, y + 40, 70, 32, 8, INNER)
    rrect(c, x - 80, y + 40, 70, 32, 8, INNER)
    _wheel(c, x - 75, y - 28, 26)
    _wheel(c, x + 75, y - 28, 26)


def camper(c, x, y):
    rrect(c, x - 130, y - 8, 260, 100, 14)
    rrect(c, x - 100, y + 30, 50, 40, 8, INNER)
    rrect(c, x - 20, y + 30, 50, 40, 8, INNER)
    rrect(c, x + 70, y + 30, 40, 50, 8, INNER)
    _wheel(c, x - 70, y - 28, 24)
    _wheel(c, x + 80, y - 28, 24)


def rv(c, x, y):
    rrect(c, x - 150, y - 8, 300, 95, 16)
    rrect(c, x - 120, y + 28, 46, 36, 8, INNER)
    rrect(c, x - 50, y + 28, 46, 36, 8, INNER)
    rrect(c, x + 30, y + 28, 46, 36, 8, INNER)
    rrect(c, x + 100, y + 18, 36, 50, 8, INNER)
    _wheel(c, x - 90, y - 28, 24)
    _wheel(c, x + 20, y - 28, 24)
    _wheel(c, x + 100, y - 28, 24)


def bus(c, x, y):
    rrect(c, x - 150, y - 10, 300, 90, 18)
    for i in range(5):
        rrect(c, x - 125 + i * 52, y + 28, 40, 32, 6, INNER)
    rrect(c, x + 110, y + 12, 28, 50, 6, INNER)
    _wheel(c, x - 90, y - 28, 26)
    _wheel(c, x + 90, y - 28, 26)


def school_bus(c, x, y):
    rrect(c, x - 155, y - 10, 310, 85, 16)
    for i in range(6):
        rrect(c, x - 130 + i * 42, y + 22, 32, 28, 5, INNER)
    rrect(c, x - 20, y + 78, 40, 12, 4)
    _wheel(c, x - 95, y - 28, 24)
    _wheel(c, x + 95, y - 28, 24)


def double_decker(c, x, y):
    rrect(c, x - 140, y - 8, 280, 70, 12)
    rrect(c, x - 140, y + 62, 280, 55, 12)
    for i in range(4):
        rrect(c, x - 115 + i * 58, y + 18, 40, 26, 5, INNER)
        rrect(c, x - 115 + i * 58, y + 78, 40, 26, 5, INNER)
    _wheel(c, x - 85, y - 28, 24)
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


def fire_ladder(c, x, y):
    rrect(c, x - 140, y - 8, 200, 60, 12)
    _cab(c, x + 50, y + 5, 80, 70)
    rrect(c, x - 120, y + 55, 160, 16, 4)
    capsule(c, x - 40, y + 70, x + 80, y + 140, 8)
    _wheel(c, x - 90, y - 28, 24)
    _wheel(c, x + 20, y - 28, 24)
    _wheel(c, x + 90, y - 28, 24)


def ambulance(c, x, y):
    rrect(c, x - 130, y - 8, 260, 90, 14)
    rrect(c, x + 30, y + 22, 70, 40, 8, INNER)
    rrect(c, x - 90, y + 22, 70, 40, 8, INNER)
    rrect(c, x - 20, y + 85, 40, 22, 6)
    _wheel(c, x - 75, y - 28, 26)
    _wheel(c, x + 75, y - 28, 26)


def patrol_car(c, x, y):
    rrect(c, x - 120, y - 18, 240, 65, 18)
    rrect(c, x - 70, y + 45, 140, 42, 14)
    rrect(c, x - 55, y + 55, 50, 24, 6, INNER)
    rrect(c, x + 8, y + 55, 50, 24, 6, INNER)
    rrect(c, x - 22, y + 88, 44, 14, 4)
    _wheel(c, x - 70, y - 28)
    _wheel(c, x + 70, y - 28)


def motorcycle(c, x, y):
    _wheel(c, x - 80, y - 30, 36)
    _wheel(c, x + 80, y - 30, 36)
    ellipse(c, x, y + 10, 55, 18)
    capsule(c, x + 40, y + 10, x + 80, y - 30, 8)
    capsule(c, x - 40, y + 10, x - 80, y - 30, 8)
    ellipse(c, x - 10, y + 40, 28, 14)
    capsule(c, x + 30, y + 18, x + 20, y + 70, 6)
    ellipse(c, x + 8, y + 80, 20, 7)


def dirt_bike(c, x, y):
    _wheel(c, x - 75, y - 28, 34)
    _wheel(c, x + 75, y - 28, 34)
    poly(c, [(x - 75, y - 28), (x - 10, y + 50), (x + 50, y + 10)], OUTER, False)
    ellipse(c, x - 5, y + 62, 24, 12)
    capsule(c, x + 50, y + 10, x + 40, y + 70, 6)
    ellipse(c, x + 28, y + 80, 18, 7)


def bicycle(c, x, y):
    _wheel(c, x - 80, y - 40, 42)
    _wheel(c, x + 80, y - 40, 42)
    poly(c, [(x - 80, y - 40), (x - 10, y + 40), (x + 55, y + 8), (x - 80, y - 40)], OUTER, False)
    capsule(c, x - 10, y + 40, x - 10, y + 70, 6)
    ellipse(c, x - 10, y + 82, 22, 8)
    capsule(c, x + 55, y + 8, x + 80, y - 40, 6)
    ellipse(c, x + 40, y + 8, 18, 8)


def tricycle(c, x, y):
    _wheel(c, x, y + 40, 36)
    _wheel(c, x - 70, y - 50, 28)
    _wheel(c, x + 70, y - 50, 28)
    capsule(c, x, y + 40, x, y - 20, 8)
    ellipse(c, x, y - 20, 40, 14)
    capsule(c, x, y + 70, x, y + 100, 6)
    ellipse(c, x, y + 110, 20, 8)


def scooter(c, x, y):
    rrect(c, x - 90, y - 20, 150, 18, 8)
    capsule(c, x + 60, y - 10, x + 40, y + 90, 8)
    ellipse(c, x + 28, y + 102, 22, 8)
    _wheel(c, x - 70, y - 40, 24)
    _wheel(c, x + 70, y - 40, 24)


def trike(c, x, y):
    _wheel(c, x, y + 20, 40)
    _wheel(c, x - 80, y - 40, 30)
    _wheel(c, x + 80, y - 40, 30)
    rrect(c, x - 40, y - 10, 80, 36, 10)
    capsule(c, x, y + 24, x, y + 80, 7)
    ellipse(c, x, y + 92, 22, 8)


def atv(c, x, y):
    rrect(c, x - 70, y, 140, 40, 12)
    rrect(c, x - 30, y + 38, 60, 28, 8)
    _wheel(c, x - 70, y - 18, 32)
    _wheel(c, x + 70, y - 18, 32)
    ellipse(c, x, y + 78, 22, 8)


def go_kart(c, x, y):
    rrect(c, x - 90, y - 8, 180, 28, 10)
    rrect(c, x - 30, y + 18, 60, 24, 8)
    _wheel(c, x - 80, y - 22, 22)
    _wheel(c, x + 80, y - 22, 22)
    ellipse(c, x, y + 52, 18, 8)


def tractor(c, x, y):
    rrect(c, x - 20, y - 5, 110, 55, 12)
    rrect(c, x + 10, y + 48, 60, 48, 10)
    rrect(c, x + 22, y + 60, 36, 26, 6, INNER)
    _wheel(c, x - 70, y - 10, 48)
    _wheel(c, x + 70, y - 28, 28)


def farm_truck(c, x, y):
    _cab(c, x - 120, y, 90, 72)
    rrect(c, x - 30, y - 8, 150, 55, 10)
    rrect(c, x, y + 12, 50, 22, 6, INNER)
    rrect(c, x + 60, y + 12, 50, 22, 6, INNER)
    _wheel(c, x - 70, y - 28, 26)
    _wheel(c, x + 90, y - 28, 26)


def combine(c, x, y):
    rrect(c, x - 40, y, 140, 70, 12)
    rrect(c, x - 10, y + 68, 60, 40, 10)
    rrect(c, x + 2, y + 78, 36, 22, 6, INNER)
    rrect(c, x - 140, y - 20, 100, 40, 8)
    _wheel(c, x - 20, y - 28, 36)
    _wheel(c, x + 80, y - 22, 24)


def wagon(c, x, y):
    rrect(c, x - 90, y - 5, 180, 55, 12)
    capsule(c, x - 90, y + 20, x - 150, y + 50, 8)
    circle(c, x - 158, y + 55, 10)
    _wheel(c, x - 50, y - 32, 24)
    _wheel(c, x + 50, y - 32, 24)


def cart(c, x, y):
    rrect(c, x - 70, y, 140, 50, 10)
    capsule(c, x - 70, y + 20, x - 130, y + 40, 7)
    _wheel(c, x - 40, y - 28, 22)
    _wheel(c, x + 40, y - 28, 22)


def wheelbarrow(c, x, y):
    poly(c, [(x - 40, y + 10), (x + 90, y + 40), (x + 80, y - 10), (x - 50, y - 30)])
    capsule(c, x - 40, y + 10, x - 130, y + 50, 8)
    capsule(c, x - 50, y - 30, x - 130, y + 20, 8)
    _wheel(c, x + 70, y - 28, 28)


def golf_cart(c, x, y):
    rrect(c, x - 80, y - 8, 160, 40, 10)
    rrect(c, x - 50, y + 30, 50, 28, 8)
    rrect(c, x + 10, y + 30, 50, 28, 8)
    rrect(c, x - 70, y + 70, 140, 12, 4)
    capsule(c, x - 60, y + 40, x - 60, y + 70, 5)
    capsule(c, x + 60, y + 40, x + 60, y + 70, 5)
    _wheel(c, x - 55, y - 28, 22)
    _wheel(c, x + 55, y - 28, 22)


def train(c, x, y):
    rrect(c, x - 40, y - 10, 150, 80, 14)
    rrect(c, x - 20, y + 70, 70, 40, 10)
    rrect(c, x - 8, y + 82, 46, 22, 6, INNER)
    rrect(c, x + 70, y + 55, 28, 70, 8)
    circle(c, x + 84, y + 140, 16)
    _wheel(c, x - 5, y - 28, 24)
    _wheel(c, x + 70, y - 28, 24)


def train_car(c, x, y):
    rrect(c, x - 120, y - 8, 240, 90, 14)
    rrect(c, x - 90, y + 22, 70, 40, 8, INNER)
    rrect(c, x + 20, y + 22, 70, 40, 8, INNER)
    _wheel(c, x - 70, y - 28, 22)
    _wheel(c, x + 70, y - 28, 22)


def caboose(c, x, y):
    rrect(c, x - 110, y - 8, 220, 80, 12)
    rrect(c, x - 30, y + 72, 60, 40, 8)
    rrect(c, x - 18, y + 82, 36, 20, 5, INNER)
    rrect(c, x - 80, y + 20, 40, 30, 6, INNER)
    rrect(c, x + 40, y + 20, 40, 30, 6, INNER)
    _wheel(c, x - 60, y - 28, 22)
    _wheel(c, x + 60, y - 28, 22)


def freight_car(c, x, y):
    rrect(c, x - 130, y - 8, 260, 70, 8)
    _wheel(c, x - 80, y - 28, 20)
    _wheel(c, x - 30, y - 28, 20)
    _wheel(c, x + 30, y - 28, 20)
    _wheel(c, x + 80, y - 28, 20)


def subway(c, x, y):
    rrect(c, x - 150, y - 8, 300, 85, 22)
    for i in range(4):
        rrect(c, x - 120 + i * 68, y + 22, 50, 36, 8, INNER)
    ellipse(c, x, y + 90, 16, 10)
    _wheel(c, x - 90, y - 28, 20)
    _wheel(c, x + 90, y - 28, 20)


def tram(c, x, y):
    rrect(c, x - 140, y - 8, 280, 80, 18)
    rrect(c, x - 100, y + 22, 55, 32, 6, INNER)
    rrect(c, x - 20, y + 22, 55, 32, 6, INNER)
    rrect(c, x + 60, y + 22, 55, 32, 6, INNER)
    capsule(c, x, y + 72, x, y + 120, 5)
    ellipse(c, x, y + 128, 40, 8)
    _wheel(c, x - 80, y - 28, 20)
    _wheel(c, x + 80, y - 28, 20)


def plane(c, x, y):
    ellipse(c, x, y, 140, 32)
    poly(c, [(x - 20, y), (x - 50, y + 90), (x + 40, y + 18), (x + 20, y)])
    poly(c, [(x - 20, y), (x - 50, y - 90), (x + 40, y - 18), (x + 20, y)])
    poly(c, [(x - 130, y), (x - 165, y + 40), (x - 140, y), (x - 165, y - 40)])
    circle(c, x + 90, y + 8, 8, INNER)


def jet(c, x, y):
    ellipse(c, x + 10, y, 150, 24)
    poly(c, [(x, y), (x - 30, y + 70), (x + 50, y + 12)])
    poly(c, [(x, y), (x - 30, y - 70), (x + 50, y - 12)])
    poly(c, [(x - 130, y), (x - 170, y + 28), (x - 150, y), (x - 170, y - 28)])
    circle(c, x + 110, y + 4, 7, INNER)


def biplane(c, x, y):
    ellipse(c, x, y, 110, 22)
    rrect(c, x - 60, y + 40, 140, 12, 4)
    rrect(c, x - 60, y - 40, 140, 12, 4)
    capsule(c, x - 40, y - 40, x - 40, y + 40, 4)
    capsule(c, x + 40, y - 40, x + 40, y + 40, 4)
    poly(c, [(x - 110, y), (x - 140, y + 30), (x - 120, y), (x - 140, y - 30)])
    circle(c, x + 80, y + 6, 7, INNER)


def helicopter(c, x, y):
    ellipse(c, x, y, 80, 40)
    rrect(c, x + 40, y - 8, 90, 22, 8)
    circle(c, x - 20, y + 8, 16, INNER)
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


def tugboat(c, x, y):
    poly(c, [(x - 110, y), (x + 110, y), (x + 80, y - 45), (x - 80, y - 45)])
    rrect(c, x - 40, y, 80, 50, 10)
    rrect(c, x - 22, y + 14, 44, 24, 6, INNER)
    rrect(c, x - 8, y + 50, 16, 40, 4)
    circle(c, x, y + 100, 12)


def barge(c, x, y):
    poly(c, [(x - 160, y), (x + 160, y), (x + 140, y - 40), (x - 140, y - 40)])
    rrect(c, x - 100, y + 8, 80, 40, 6)
    rrect(c, x + 20, y + 8, 80, 40, 6)


def sailboat(c, x, y):
    poly(c, [(x - 110, y - 10), (x + 110, y - 10), (x + 70, y - 55), (x - 70, y - 55)])
    capsule(c, x, y - 10, x, y + 130, 6)
    poly(c, [(x + 8, y + 120), (x + 95, y + 20), (x + 8, y + 20)])
    poly(c, [(x - 8, y + 90), (x - 70, y + 20), (x - 8, y + 20)])


def semi(c, x, y):
    _cab(c, x - 140, y + 10, 85, 90)
    rrect(c, x - 55, y - 8, 210, 85, 8)
    _wheel(c, x - 95, y - 28, 22)
    _wheel(c, x + 10, y - 28, 22)
    _wheel(c, x + 70, y - 28, 22)
    _wheel(c, x + 125, y - 28, 22)


def trailer(c, x, y):
    rrect(c, x - 140, y - 5, 280, 80, 8)
    rrect(c, x - 160, y + 20, 20, 20, 4)
    _wheel(c, x - 40, y - 28, 22)
    _wheel(c, x + 20, y - 28, 22)
    _wheel(c, x + 80, y - 28, 22)


def box_truck(c, x, y):
    _cab(c, x - 140, y + 5, 85, 75)
    rrect(c, x - 55, y - 8, 200, 100, 8)
    rrect(c, x + 20, y + 30, 70, 40, 6, INNER)
    _wheel(c, x - 90, y - 28, 24)
    _wheel(c, x + 20, y - 28, 24)
    _wheel(c, x + 110, y - 28, 24)


def moving_truck(c, x, y):
    _cab(c, x - 145, y, 80, 70)
    rrect(c, x - 65, y - 8, 220, 110, 10)
    rrect(c, x - 40, y + 40, 50, 36, 6, INNER)
    rrect(c, x + 40, y + 40, 50, 36, 6, INNER)
    _wheel(c, x - 95, y - 28, 24)
    _wheel(c, x + 30, y - 28, 24)
    _wheel(c, x + 120, y - 28, 24)


def ice_cream_truck(c, x, y):
    rrect(c, x - 130, y - 8, 260, 80, 16)
    rrect(c, x - 40, y + 70, 140, 40, 12)
    rrect(c, x - 20, y + 80, 44, 22, 6, INNER)
    rrect(c, x + 40, y + 80, 44, 22, 6, INNER)
    circle(c, x + 90, y + 28, 16, INNER)
    _wheel(c, x - 75, y - 28, 24)
    _wheel(c, x + 75, y - 28, 24)


def mail_truck(c, x, y):
    rrect(c, x - 110, y - 8, 220, 90, 14)
    rrect(c, x + 20, y + 28, 55, 36, 8, INNER)
    rrect(c, x - 70, y + 28, 55, 36, 8, INNER)
    rrect(c, x + 70, y + 12, 28, 50, 6)
    _wheel(c, x - 60, y - 28, 24)
    _wheel(c, x + 70, y - 28, 24)


def pickup_camper(c, x, y):
    _cab(c, x - 130, y - 5, 95, 70)
    rrect(c, x - 35, y - 5, 160, 95, 10)
    rrect(c, x + 10, y + 30, 50, 36, 8, INNER)
    _wheel(c, x - 80, y - 28, 24)
    _wheel(c, x + 90, y - 28, 24)


def construction_truck(c, x, y):
    _cab(c, x - 125, y + 8)
    rrect(c, x - 35, y - 8, 155, 60, 10)
    rrect(c, x - 15, y + 18, 40, 22, 5, INNER)
    rrect(c, x + 40, y + 18, 40, 22, 5, INNER)
    circle(c, x + 100, y + 40, 10, INNER)
    _wheel(c, x - 80, y - 28, 24)
    _wheel(c, x + 20, y - 28, 24)
    _wheel(c, x + 95, y - 28, 24)


def cone(c, x, y):
    poly(c, [(x - 70, y - 60), (x + 70, y - 60), (x + 18, y + 110), (x - 18, y + 110)])
    ellipse(c, x, y - 60, 80, 16)
    rrect(c, x - 28, y + 20, 56, 18, 4, INNER)


def hard_hat(c, x, y):
    ellipse(c, x, y + 20, 90, 55)
    ellipse(c, x, y - 20, 120, 22)
    rrect(c, x - 12, y + 50, 24, 18, 6)


def barrier(c, x, y):
    rrect(c, x - 140, y - 10, 280, 50, 8)
    for i in range(5):
        rrect(c, x - 120 + i * 56, y, 40, 30, 4, INNER)
    capsule(c, x - 110, y - 10, x - 110, y - 70, 8)
    capsule(c, x + 110, y - 10, x + 110, y - 70, 8)


def traffic_light(c, x, y):
    rrect(c, x - 40, y - 20, 80, 160, 14)
    circle(c, x, y + 95, 22)
    circle(c, x, y + 40, 22)
    circle(c, x, y - 15, 22)
    capsule(c, x, y - 20, x, y - 90, 8)


def stop_sign(c, x, y):
    s = 70
    pts = []
    for i in range(8):
        a = radians(22.5 + i * 45)
        pts.append((x + s * cos(a), y + 20 + s * sin(a)))
    poly(c, pts)
    capsule(c, x, y - 50, x, y - 120, 8)


def snowmobile(c, x, y):
    rrect(c, x - 80, y, 150, 36, 12)
    rrect(c, x - 20, y + 34, 55, 28, 8)
    ellipse(c, x + 70, y - 18, 50, 12)
    ellipse(c, x - 70, y - 18, 40, 10)
    capsule(c, x + 40, y + 30, x + 55, y + 70, 6)
    ellipse(c, x + 42, y + 80, 18, 7)


def barrel(c, x, y):
    ellipse(c, x, y + 80, 55, 22)
    rrect(c, x - 55, y - 70, 110, 150, 20)
    ellipse(c, x, y - 70, 55, 22)
    rrect(c, x - 45, y + 20, 90, 12, 4, INNER)
    rrect(c, x - 45, y - 20, 90, 12, 4, INNER)


def shovel(c, x, y):
    capsule(c, x, y - 110, x, y + 70, 8)
    poly(c, [(x - 40, y + 70), (x + 40, y + 70), (x + 32, y + 130), (x - 32, y + 130)])
    ellipse(c, x, y - 120, 16, 10)


def toolbox(c, x, y):
    rrect(c, x - 110, y - 40, 220, 90, 12)
    rrect(c, x - 40, y + 50, 80, 22, 8)
    rrect(c, x - 90, y - 10, 70, 28, 6, INNER)
    rrect(c, x + 20, y - 10, 70, 28, 6, INNER)
    circle(c, x, y + 10, 8, INNER)


PAGES = [
    ("dump truck", dump_truck),
    ("dump up", dump_up),
    ("mini dump", mini_dump),
    ("digger", digger),
    ("long digger", long_digger),
    ("mini digger", mini_digger),
    ("bulldozer", bulldozer),
    ("loader", loader),
    ("front loader", front_loader),
    ("skid steer", skid_steer),
    ("backhoe", backhoe),
    ("grader", grader),
    ("steamroller", steamroller),
    ("road roller", road_roller),
    ("forklift", forklift),
    ("cement mixer", cement_mixer),
    ("mixer truck", mixer_truck),
    ("crane", crane),
    ("tower crane", tower_crane),
    ("crawler crane", crawler_crane),
    ("cherry picker", cherry_picker),
    ("boom truck", boom_truck),
    ("paver", paver),
    ("tanker", tanker),
    ("tanker truck", tanker_truck),
    ("flatbed", flatbed),
    ("logging truck", logging_truck),
    ("snowplow", snowplow),
    ("sweeper", sweeper),
    ("garbage truck", garbage_truck),
    ("dumpster", dumpster),
    ("concrete pump", concrete_pump),
    ("pile driver", pile_driver),
    ("drill rig", drill_rig),
    ("tow truck", tow_truck),
    ("pickup", pickup),
    ("work van", work_van),
    ("car", car),
    ("taxi", taxi),
    ("jeep", jeep),
    ("convertible", convertible),
    ("race car", race_car),
    ("monster truck", monster_truck),
    ("limo", limo),
    ("van", van),
    ("camper", camper),
    ("rv", rv),
    ("bus", bus),
    ("school bus", school_bus),
    ("double decker", double_decker),
    ("fire truck", fire_truck),
    ("fire ladder", fire_ladder),
    ("ambulance", ambulance),
    ("patrol car", patrol_car),
    ("motorcycle", motorcycle),
    ("dirt bike", dirt_bike),
    ("bicycle", bicycle),
    ("tricycle", tricycle),
    ("scooter", scooter),
    ("trike", trike),
    ("atv", atv),
    ("go kart", go_kart),
    ("tractor", tractor),
    ("farm truck", farm_truck),
    ("combine", combine),
    ("wagon", wagon),
    ("cart", cart),
    ("wheelbarrow", wheelbarrow),
    ("golf cart", golf_cart),
    ("train", train),
    ("train car", train_car),
    ("caboose", caboose),
    ("freight car", freight_car),
    ("subway", subway),
    ("tram", tram),
    ("plane", plane),
    ("jet", jet),
    ("biplane", biplane),
    ("helicopter", helicopter),
    ("boat", boat),
    ("tugboat", tugboat),
    ("barge", barge),
    ("sailboat", sailboat),
    ("semi", semi),
    ("trailer", trailer),
    ("box truck", box_truck),
    ("moving truck", moving_truck),
    ("ice cream truck", ice_cream_truck),
    ("mail truck", mail_truck),
    ("pickup camper", pickup_camper),
    ("construction truck", construction_truck),
    ("cone", cone),
    ("hard hat", hard_hat),
    ("barrier", barrier),
    ("traffic light", traffic_light),
    ("stop sign", stop_sign),
    ("snowmobile", snowmobile),
    ("barrel", barrel),
    ("shovel", shovel),
    ("toolbox", toolbox),
]

assert len(PAGES) == 100, len(PAGES)
assert len({label for label, _ in PAGES}) == 100, "duplicate labels"
