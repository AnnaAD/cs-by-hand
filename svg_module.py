import svgwrite

def draw_module(dwg,x,y,width,height,inputs,outputs,label):

    margin = 20
    dwg.add(
        dwg.rect(
            insert=(x, y),
            size=(width, height),
            fill="none",
            stroke="black"
        )
    )

    ty = margin
    for i in inputs:
        dwg.add(
            dwg.text(
                i,
                insert=(x+5, y+ty),
                text_anchor="start",
                font_size=14 
            )
        )

        dwg.add(
            dwg.line(
                start=(x-10,y+ty), end=(x, y+ty),
                stroke="black", stroke_width=2
            )
        )
        ty+=(height-margin*1.5)/max(len(inputs)-1,1)
    
    ty = margin
    for i in outputs:
        dwg.add(
            dwg.text(
                i,
                insert=(x+width-5, y+ty),
                text_anchor="end",
                font_size=14 
            )
        )

        dwg.add(
            dwg.line(
                start=(x+width,y+ty), end=(x+width+10, y+ty),
                stroke="black", stroke_width=2
            )
        )
        ty+=(height-margin*1.5)/max(len(outputs)-1,1)
    
    dwg.add(
        dwg.text(
            label,
            insert=(x+width/2, y+height/2),
            text_anchor="middle",
            font_size=14 
        )
    )


