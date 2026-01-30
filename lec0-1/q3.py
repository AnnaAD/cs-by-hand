import svgwrite

def draw_binary_row(dwg, num_boxes,y, box_size = 40,margin=20, text_height=20, fill_text = {}, text_label = "A", text = True):
    for i in range(num_boxes):
        x = margin + i * box_size

        dwg.add(dwg.rect(
            insert=(x, y),
            size=(box_size, box_size),
            fill="none",
            stroke="black"
        ))

        if(text):
            dwg.add(dwg.text(
                f"{text_label}[{num_boxes-i-1}]",
                insert=(x + box_size / 2, y - 5),
                text_anchor="middle",
                font_size=14
            ))
        
        if(num_boxes-i-1 in fill_text):
            dwg.add(dwg.text(
                f"{fill_text[num_boxes-i-1]}",
                insert=(x + box_size / 2, y + box_size / 2),
                text_anchor="middle",
                font_size=14
            ))

num_boxes = 4           
box_size = 40             
margin = 20
text_height = 20

width = margin * 2 + num_boxes * box_size
height = margin * 3 + box_size*4 + text_height*4

dwg = svgwrite.Drawing("outputs/lec0-1/q3.svg", size=(width, height))

import random
decimal1 = random.randint(-1*(2**(num_boxes-1)),2**(num_boxes - 1) - 1)
decimal2 = random.randint(-1*(2**(num_boxes-1)),2**(num_boxes - 1) - 1)

op = "+"

dwg.add(dwg.text(
        f"Represent {decimal1}{op}{decimal2}",
        insert=(width/2, margin),
        text_anchor="middle",
        font_size=14
    ))

draw_binary_row(dwg,num_boxes,y = margin + text_height, box_size=box_size,margin=margin,text_height=text_height, fill_text = {0:0}, text_label="Cin")
draw_binary_row(dwg,num_boxes,y = (margin + text_height*2) + box_size, box_size=box_size,margin=margin,text_label="A",text_height=text_height)
draw_binary_row(dwg,num_boxes,y = (margin + text_height*3) + box_size*2, box_size=box_size,margin=margin,text_label="B",text_height=text_height)

dwg.add(dwg.text(
        f"+",
        insert=(margin/2, (margin + text_height*3) + box_size*2),
        text_anchor="middle",
        font_size=20
    ))

dwg.add(dwg.line(start=(20,(margin + text_height*4) + box_size*3),
                         end=(width-20,(margin + text_height*4) + box_size*3),
                         stroke="black",
                         stroke_width=1))

draw_binary_row(dwg,num_boxes,y = (margin + text_height*4) + box_size*3 + 20, box_size=box_size,margin=margin,text_label="S",text_height=text_height)

dwg.save()
print("Saved as q3.svg")
