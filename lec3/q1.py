import svgwrite
from svg_logic import draw_wire, draw_buffer




width = 600
height = 140
dwg = svgwrite.Drawing("outputs/lec3/q1.svg", size=(width,height))


b1 = draw_buffer(dwg, 50,50, negate = True)
b2 = draw_buffer(dwg, 150,50, negate = True)

draw_wire(dwg,b1["output"], b2["input"])

br = tuple(map(sum, zip(b2["output"], (20,0))))
bl = tuple(map(sum, zip(b1["input"], (-20,0))))

tl = tuple(map(sum, zip(bl, (0,-50))))
tr = tuple(map(sum, zip(br, (0,-50))))

draw_wire(dwg,b2["output"], br)
draw_wire(dwg,b1["input"], bl)
draw_wire(dwg, bl,tl)
draw_wire(dwg, br,tr)
draw_wire(dwg, tr,tl)

dwg.add(dwg.text(
    "0",
    insert=tuple(map(sum, zip(b1["input"], (-10,15)))),
    text_anchor = "middle", font_size = 14
))


# draw_wire(dwg,b1["input"], b1["input"]-50)
# draw_wire(dwg,b2["output"], b2["output"])

dwg.save()


