import svgwrite


from svg_truthtable import draw_truth_table_filled

inputs = ["A","B"]
outputs = ["X"]

row_height = 30
col_width = 30
writing_section = 200
width = 400
margin = 20

height = row_height*(2**len(inputs)) + writing_section*2 + margin*3
dwg = svgwrite.Drawing("outputs/lec2/q3.svg", size=(width,height))

import random
output_vals = []
for i in outputs:
    tmp = []
    for j in range(2**(len(inputs))):
       tmp.append(random.randint(0,1)) 
    output_vals.append(tmp)

draw_truth_table_filled(dwg, width/2 - col_width*(len(inputs)+len(outputs))/2, margin, row_height,col_width, inputs, outputs, output_vals)

dwg.add(dwg.text(
        f"Write a SOP expression for the above truth table.",
        insert=(width/2, row_height*(2**len(inputs))+margin*2),
        text_anchor="middle",
        font_size=10
    ))

dwg.add(dwg.text(
        f"Draw a circuit that encodes the above SOP expression.",
        insert=(width/2, margin*2+row_height*(2**len(inputs)) + writing_section),
        text_anchor="middle",
        font_size=10
    ))

dwg.save()

