import svgwrite
import random
from svg_truthtable import draw_truth_table


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