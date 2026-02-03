import svgwrite
import random

def draw_binary_row(dwg, num_boxes,y, box_size = 40,margin=20, text_height=20, text_label = "A", text = True):
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

import sys

if(len(sys.argv) != 4):
    print("Usage: q2.py <negative|not> <num_bits> <outfile>")

NEGATIVES = "negative" in sys.argv[1]
num_boxes = int(sys.argv[2])           
box_size = 40             
margin = 20
text_height = 20

width = margin * 2 + num_boxes * box_size
height = margin * 2 + box_size + text_height

dwg = svgwrite.Drawing(sys.argv[3], size=(width, height))

if(NEGATIVES):
    decimal = random.randint(-1*(2**(num_boxes-1)), -1)
else:
    decimal = random.randint(0,2**(num_boxes) - 1)

dwg.add(dwg.text(
        f"Write {decimal} in binary",
        insert=(width/2, margin),
        text_anchor="middle",
        font_size=14
    ))

if(NEGATIVES):
    draw_binary_row(dwg,num_boxes,y = margin + text_height, box_size=box_size,margin=margin,text_label="A[",text_height=text_height)
else:
    draw_binary_row(dwg,num_boxes,y = margin + text_height, box_size=box_size,margin=margin,text_label="2^",text_height=text_height)

dwg.save()
print("Saved as q2.svg")
