import svgwrite
from svg_logic import draw_and, draw_xor,draw_or, draw_mux_2
from svg_truthtable import draw_truth_table


width = 600
height = 400
dwg = svgwrite.Drawing("outputs/lec2/q5.svg", size=(width,height))

draw_mux_2(dwg,60,20, 80, inputs = ["A","B"], output = "Y")

draw_truth_table(dwg, 150, 20, 15,20, ["A","B","S"], ["Y"])

dwg.add(dwg.text(
        f"Write a SOP expression(s) for the truth table.",
        insert=(250, 20),
        text_anchor="start",
        font_size=10
    ))

dwg.add(dwg.text(
        f"Draw a circuit that encodes the SOP expression.",
        insert=(250, 80),
        text_anchor="start",
        font_size=10
    ))

draw_mux_2(dwg,60,180,100, inputs = ["A","B","C","D"], output = "Y",select_label="S[1:0]")

draw_truth_table(dwg, 150, 210, 15,20, ["S[1]", "S[0]"], ["Y"])

import random 
dwg.add(dwg.text(
        f"How many select bits do you need for an {random.randint(2,17)}-input MUX?",
        insert=(250, 210),
        text_anchor="start",
        font_size=10
    ))

dwg.save()