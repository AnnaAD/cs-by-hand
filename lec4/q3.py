import svgwrite
from svg_module import draw_module 


margin = 40
input_height_area = 100
rca_height = 180

width = 600
height = rca_height+margin*4+input_height_area

dwg = svgwrite.Drawing("outputs/lec4/q3.svg", size=(width,height))

inputs = ["Cin"]
for i in range(4):
    inputs.append(f"A[{i}]")
for i in range(4):
    inputs.append(f"B[{i}]")

outputs = ["Cout"]
for i in range(4):
    outputs.append(f"S[{i}]")


draw_module(dwg,width/2 - 140/2,margin*2+input_height_area,140,rca_height,inputs,outputs,"4-bit Adder")



draw_module(dwg,margin+200,rca_height+margin*3+input_height_area,30,30,[""],[],f"V")
draw_module(dwg,margin+250,rca_height+margin*3+input_height_area,30,30,[""],[],f"Z")
draw_module(dwg,margin+300,rca_height+margin*3+input_height_area,30,30,[""],[],f"N")



dx=margin*3
for i in range(4):
    draw_module(dwg,margin+dx,margin*2,30,30,[],[""],f"A[{i}]")
    dx += 50 + margin

dx=margin*3
for i in range(4):
    draw_module(dwg,margin+dx,margin*3,30,30,[],[""],f"B[{i}]")
    dx += 50 + margin

draw_module(dwg,margin,margin*2.5,60,30,[],[""],f"ALUFN")


dwg.add(dwg.text(
        f"Complete the 4-Bit Arith Module by adding logic gates (AND,OR,NOT,XOR), muxes, and wires",
        insert=(width/2, margin),
        text_anchor="middle",
        font_size=14
    ))

dwg.save()