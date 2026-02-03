import svgwrite
from svg_module import draw_module 
from svg_logic import draw_mux


def draw_input_area(dwg,x,y):
    dx = 0

    for i in ["RA1","RA2", "WA","WE","WD"]:
        dwg.add(dwg.text(
            f"{i}",
            insert=(x+dx,y),
            font_size = 14,
            text_anchor="middle"
        ))
        dwg.add(dwg.rect(
            insert=(x+dx+14,y-15),
            size=(60,30),
            fill="none",
            stroke="black",
            stroke_width="2"
        ))
        dx += 100

margin = 40

width = 750
height = 300

dwg = svgwrite.Drawing("outputs/lec5/q1.svg", size=(width,height))

draw_module(dwg,margin*1,margin*2,140,140,["RA1","RA2", "WA","WE","WD",">"],["RD1", "RD2"],"Register File")


import random
dwg.add(dwg.text(
        f"What signals should be set to set R{random.randint(0,31)} = {random.randint(-8,8)}?",
        insert=(margin*3 + 120, margin*2),
        text_anchor="start",
        font_size=14
    ))

draw_input_area(dwg, x = margin*3 + 120, y = margin*3)

dwg.add(dwg.text(
        f"What signals should be set to read R{random.randint(0,31)} and R{random.randint(0,31)}?",
        insert=(margin*3 + 120, margin*4),
        text_anchor="start",
        font_size=14
    ))

draw_input_area(dwg, x = margin*3 + 120, y = margin*5)



dwg.save()