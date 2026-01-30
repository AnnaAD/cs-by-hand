

import svgwrite

import random

def draw_data_row(dwg,x,y,tick_width,num_ticks,row_height, clk = True):
    path_commands = []
    start_width = tick_width
    if(not clk):
        tick_width = random.randint(start_width//2, start_width*2)
    dx = 0
    high = 0        
    path_commands.append(("M", (x,y)))
    for i in range(num_ticks):
        path_commands.append(("L", (x+dx, (high*row_height)+y)))
        path_commands.append(("L", (x+dx+tick_width, (high*row_height)+y)))
        dx += tick_width
        if(not clk):
            tick_width = random.randint(start_width//2, start_width*2)

        if(x + dx > start_width * num_ticks):
            break

        high = 1 if high == 0 else 0
    print(path_commands)
    dwg.add(dwg.path(d=path_commands, fill="none", stroke="black", stroke_width = 2))

def draw_waveform_plot(dwg,x,y, width, row_height, row_margin):
    
    dwg.add(dwg.line(
        start = (x,y + row_height*4+ row_margin*4), end = (x+width, y + row_height*4+ row_margin*4),
        stroke="black", stroke_width=2
    ))
    dwg.add(dwg.line(
        start = (x,y), end = (x, y + row_height*4 + row_margin*4),
        stroke="black", stroke_width=2
    ))

    dy = row_height / 2
    for i in ["Q", "★", "D", "CLK"]:
        dwg.add(dwg.text(
            i,
            insert=(x - 5, y+ dy),
            text_anchor="end",
            font_size=14
        ))
        dy += row_height + row_margin
    
    draw_data_row(dwg,x,y+row_height*2 + row_margin*2, 40,width//40, row_height,clk = False)
    draw_data_row(dwg,x,y+row_height*3 + row_margin*3, 100,width//100, row_height,clk = True)

margin = 50
plot_width = 500
row_height = 50
row_margin = 10

width = plot_width + margin*2
height = margin*2 + row_height*4 + row_margin*4

dwg = svgwrite.Drawing("outputs/lec3/q3.svg", size=(width,height))

draw_waveform_plot(dwg, margin,margin, plot_width, row_height, row_margin)

dwg.add(dwg.text(
        f"Draw the signal waveform for Q and ★",
        insert=(width/2, margin),
        text_anchor="middle",
        font_size=14
    ))

dwg.save()
    
