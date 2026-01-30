

import svgwrite
from svg_module import draw_module
from svg_logic import draw_mux

def draw_truth_table(dwg,x,y,row_height, col_width, inputs, outputs):

    width = (len(inputs)+len(outputs))*col_width
    height = 2**(len(inputs))*row_height

    dwg.add(dwg.rect(
            insert=(x, y),
            size=(width, height),
            fill="none",
            stroke="black"
    ))

    for i in range(len(inputs)):
        tx = x + i * col_width
        dwg.add(dwg.text(
            f"{inputs[i]}",
            insert=(tx + col_width/2, y),
            text_anchor="middle",
            font_size=14
        ))
        dwg.add(dwg.line(start=(tx+col_width,y),
            end=(tx+col_width,y+height),
            stroke="black",
            stroke_width=2 if i == len(inputs)-1 else 1))
    
    for i in range(len(outputs)):
        tx = x + (i+len(inputs)) * col_width
        dwg.add(dwg.text(
            f"{outputs[i]}",
            insert=(tx + col_width/2, y),
            text_anchor="middle",
            font_size=14
        ))
        dwg.add(dwg.line(start=(tx+col_width,y),
            end=(tx+col_width,y+height),
            stroke="black",
            stroke_width=1))

    for i in range(2**(len(inputs))):
        ty = y + i*row_height
        dwg.add(dwg.line(start=(x,ty),
            end=(x+width,ty),
            stroke="black",
            stroke_width=1))
 

margin = 50

width = 400
height = 250

dwg = svgwrite.Drawing("outputs/lec3/q2.svg", size=(width,height))

draw_module(dwg,margin,margin,80,100,["D","WE"],["Q"],"D-latch")

draw_mux(dwg,margin*2 + 100,margin,["Q\'","D"], "Q")

draw_truth_table(dwg, margin*2 + 80 + 100, margin,20,20,["D","WE","Q\'"],["Q"])

dwg.add(dwg.text(
        f"Complete the Truth Table",
        insert=(width/2, margin/2),
        text_anchor="middle",
        font_size=14
    ))

dwg.save()