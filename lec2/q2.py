# https://stackoverflow.com/questions/79849486/how-to-draw-proper-logic-gate-curves-or-nor-shapes-using-quadratic-bezier-curv
# use svg path 



import svgwrite
from svg_logic import draw_and, draw_xor,draw_or, draw_buffer
from svg_truthtable import draw_truth_table



width = 600
height = 240
dwg = svgwrite.Drawing("outputs/lec2/q2.svg", size=(width,height))


x = 20
for func in [draw_and,draw_or, draw_xor]:
    func(dwg,x,20,inputs = ["x","y"], output = "z", negate=False)
    draw_truth_table(dwg, x+80,20, 15,20, ["x","y"], ["z"])

    x+=200

x = 20
for func in [draw_and,draw_or, draw_xor]:
    func(dwg,x,100,inputs = ["x","y"], output = "z", negate=True)
    draw_truth_table(dwg, x+80,100, 15,20, ["x","y"], ["z"])

    x+=200

x = 20 + 200* 1
for func in [draw_buffer]:
    func(dwg,x,180,negate=True)
    draw_truth_table(dwg, x+80,180, 15,20, ["x"], ["z"])

    x+=200


dwg.save()