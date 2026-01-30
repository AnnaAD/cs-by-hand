import svgwrite


def draw_truth_table(dwg,x,y,row_height, col_width, inputs, outputs, output_vals):
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
    
    bin = 0
    for j in range(2**(len(inputs))):
        ty = y + j*row_height
        for i in range(len(inputs)):
            tx = x + i * col_width
            width = len(inputs)
            test_str = f"{bin:0{width}b}"
            dwg.add(dwg.text(
                test_str[i],
                insert=(tx + col_width/2, ty + row_height/2),
                text_anchor="middle",
                font_size=14
            ))
        bin += 1
    
    for j in range(2**(len(inputs))):
        ty = y + j*row_height
        for i in range(len(outputs)):
            tx = x + (i+len(inputs)) * col_width
            dwg.add(dwg.text(
                output_vals[i][j],
                insert=(tx + col_width/2, ty + row_height/2),
                text_anchor="middle",
                font_size=14
            ))

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

draw_truth_table(dwg, width/2 - col_width*(len(inputs)+len(outputs))/2, margin, row_height,col_width, inputs, outputs, output_vals)

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

