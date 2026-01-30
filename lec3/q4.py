import svgwrite
import random

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
 

passcode_length = 4
margin = 30
radius = 30

passcode = f"{random.randint(0,2**passcode_length-1):0{passcode_length}b}"



width = (radius+margin*2)*(passcode_length+1)
height = 400

dwg = svgwrite.Drawing("outputs/lec3/q4.svg", size=(width,height))



dwg.add(dwg.text(
        f"Complete the State Transition Diagram",
        insert=(width/2, margin),
        text_anchor="middle",
        font_size=14
    ))

dwg.add(dwg.text(
        f"Combination Lock with Password {passcode}",
        insert=(width/2, margin*2),
        text_anchor="middle",
        font_size=14
    ))

dx = margin/2
for i in range(passcode_length+1):
    dwg.add(dwg.circle(center=(20 + dx, 20+margin*4),
                       r=radius,
                       fill="none",
                       stroke="black",
                       stroke_width=2))
    dx += width/(passcode_length+1)

inputs = ["IN"]
outputs = ["OUT"]

import math

state_bits = math.ceil(math.log(passcode_length+1,2))
for i in range(state_bits):
    inputs.append(f"S[{state_bits-i-1}]")
    outputs.append(f"S'[{state_bits-i-1}]")

draw_truth_table(dwg,(width - 30*(len(inputs)+len(outputs)))/2,20+margin*6 + radius, 15,30,inputs, outputs)

dwg.save()