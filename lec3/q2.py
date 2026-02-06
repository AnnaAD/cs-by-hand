

import svgwrite
from svg_module import draw_module
from svg_logic import draw_mux_2
from svg_truthtable import draw_truth_table


margin = 50

width = 400
height = 250

dwg = svgwrite.Drawing("outputs/lec3/q2.svg", size=(width,height))

draw_mux_2(dwg,margin,margin,80,["Q\'","D"], "Q", select_label = "WE")

draw_truth_table(dwg, margin*2 + 30, margin,20,20,["D","WE","Q\'"],["Q"])


draw_module(dwg,margin*3 + 30+100,margin,80,100,["D","WE"],["Q"],"D-latch")

dwg.add(dwg.text(
        f"Complete the Truth Table",
        insert=(width/2, margin/2),
        text_anchor="middle",
        font_size=14
    ))

dwg.save()