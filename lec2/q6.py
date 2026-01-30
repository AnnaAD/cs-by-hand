import svgwrite

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