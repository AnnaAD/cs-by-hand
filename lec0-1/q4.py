import svgwrite

def draw_column_boxes(dwg, num_boxes,x, box_size = 40,margin=20, text_height=20, text_label = "A", text = True):
    for i in range(num_boxes):
        y = margin + text_height + text_height/2 + i * box_size

        dwg.add(dwg.rect(
            insert=(x, y),
            size=(box_size*2, box_size),
            fill="none",
            stroke="black"
        ))

        if(text):
            dwg.add(dwg.text(
                f"{hex(i)}",
                insert=(x + box_size, y + box_size/2),
                text_anchor="middle",
                font_size=14
            ))


num_boxes = 16           
box_size = 40             
margin = 20
text_height = 20

width = margin * 2 + 3 * (box_size*2)
height = margin * 3 + box_size*num_boxes + text_height*2

dwg = svgwrite.Drawing("outputs/lec0-1/q4.svg", size=(width, height))


dwg.add(dwg.text(
        f"Complete the Table",
        insert=(width/2, margin),
        text_anchor="middle",
        font_size=14
    ))

dwg.add(dwg.text(
        f"Dec",
        insert=(margin+box_size, margin+text_height),
        text_anchor="middle",
        font_size=14
    ))

dwg.add(dwg.text(
        f"Bin",
        insert=(margin+box_size*2+box_size, margin+text_height),
        text_anchor="middle",
        font_size=14
    ))

dwg.add(dwg.text(
        f"Hex",
        insert=(margin+box_size*4+box_size, margin+text_height),
        text_anchor="middle",
        font_size=14
    ))

draw_column_boxes(dwg,num_boxes, x = margin, box_size=box_size,margin=margin,text_height=text_height, text=False)
draw_column_boxes(dwg,num_boxes, x = margin+box_size*2, box_size=box_size,margin=margin,text_height=text_height, text=False)
draw_column_boxes(dwg,num_boxes, x = margin+box_size*4, box_size=box_size,margin=margin,text_height=text_height)

dwg.save()
print("Saved as q4.svg")