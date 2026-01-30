import svgwrite
from svg_truthtable import draw_truth_table

        

width = 600
height = 200
dwg = svgwrite.Drawing("outputs/lec2/q6.svg", size=(width,height))


draw_truth_table(dwg, 20,20, 15,20, ["Cin","A", "B"], ["S", "Cout"])

dwg.add(dwg.text(
        f"Write a SOP expression(s) for the truth table.",
        insert=(150, 20),
        text_anchor="start",
        font_size=10
    ))

dwg.add(dwg.text(
        f"Draw a circuit that encodes the SOP expression.",
        insert=(150, 80),
        text_anchor="start",
        font_size=10
    ))

dwg.save()