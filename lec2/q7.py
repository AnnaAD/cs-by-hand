import svgwrite
from svg_module import draw_module 


margin = 40
input_height_area = 100
fa_height = 80

width = 600
height = fa_height+margin*4+input_height_area

dwg = svgwrite.Drawing("outputs/lec2/q7.svg", size=(width,height))


dx = 0
for i in range(2):
    draw_module(dwg,margin+dx,margin*2+input_height_area,60,fa_height,["A","B","Cin"],["Cout", "S"],"FA")
    dx += 80 + margin

dx=width/2
for i in range(4):
    draw_module(dwg,margin+dx,fa_height+margin*3+input_height_area,30,30,[""],[],f"S[{i}]")
    dx += 20 + margin

dx=margin*2
for i in range(4):
    draw_module(dwg,margin+dx,margin*2,30,30,[],[""],f"A[{i}]")
    dx += 50 + margin

dx=margin*2
for i in range(4):
    draw_module(dwg,margin+dx,margin*3,30,30,[],[""],f"B[{i}]")
    dx += 50 + margin

draw_module(dwg,margin,margin*2.5,30,30,[],[""],f"Cin")


dwg.add(dwg.text(
        f"Complete the 4-Bit Ripple Carry Adder by adding FA modules and wires",
        insert=(width/2, margin),
        text_anchor="middle",
        font_size=14
    ))

dwg.save()