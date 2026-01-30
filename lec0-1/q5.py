import svgwrite
import random

def draw_binary_row(dwg, num_boxes,y, box_size = 40,margin=20, text_height=20, text_label = "A", text = True, fill_random_digit = False):
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
                f"{text_label}{num_boxes-1-i}{"]" if "[" in text_label else ""}",
                insert=(x + box_size / 2, y - 5),
                text_anchor="middle",
                font_size=14
            ))
        
        if fill_random_digit:
            dwg.add(dwg.text(
                f"{random.randint(0,1)}",
                insert=(x + box_size / 2, y + box_size/2),
                text_anchor="middle",
                font_size=14
            ))

def draw_hex_row(dwg, num_boxes,y, box_size = 40,margin=20, fill_random_digit = False):
    import math

    for i in range(math.ceil(num_boxes / 4)):
        x = margin + i * (box_size*4)

        dwg.add(dwg.rect(
            insert=(x, y),
            size=(box_size*4, box_size),
            fill="none",
            stroke="black"
        ))

        if fill_random_digit:
            dwg.add(dwg.text(
                f"{hex(random.randint(0,15))}",
                insert=(x + box_size * 2, y + box_size/2),
                text_anchor="middle",
                font_size=14
            ))

HEX_TO_BIN = True
num_boxes = 16            
box_size = 40             
margin = 20
text_height = 20

width = margin * 2 + num_boxes * box_size
height = margin * 2 + box_size*2 + text_height

dwg = svgwrite.Drawing("outputs/lec0-1/q5.svg", size=(width, height))

dwg.add(dwg.text(
        f"Fill in the {"Binary" if HEX_TO_BIN else "Hexidecimal"}",
        insert=(width/2, margin),
        text_anchor="middle",
        font_size=14
    ))


draw_binary_row(dwg,num_boxes,y = margin + text_height, box_size=box_size,margin=margin,text_label="A[",text_height=text_height, fill_random_digit = not HEX_TO_BIN)

draw_hex_row(dwg,num_boxes,y=margin+text_height+box_size,box_size=box_size,margin=margin, fill_random_digit = HEX_TO_BIN)

dwg.save()
print("Saved as q5.svg")
