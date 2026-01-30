import math
import svgwrite

def draw_labeled_circle(N,bits,size = 600):
    # SVG canvas
    center = size // 2
    radius = 200
    label_radius = radius + 20
    line_length = 50

    
    # Draw outer circle
    dwg.add(dwg.circle(center=(center, center),
                       r=radius,
                       fill="none",
                       stroke="black",
                       stroke_width=2))

    total_segments = 2 * N
    angle_step = 2 * math.pi / total_segments

    for i in range(total_segments):
        angle = i * angle_step - math.pi/2


        lx = center + label_radius * math.cos(angle)
        ly = center + label_radius * math.sin(angle)

        if( i < total_segments / 2):
            line_start = (lx + 10*bits, ly)
            line_end = (lx + line_length + 10*bits, ly)
            label_value = i
        else:
            line_start = (lx - 10*bits, ly)
            line_end = (lx - line_length - 10*bits, ly)
            label_value = i - N*2
        dwg.add(dwg.line(start=line_start,
                         end=line_end,
                         stroke="black",
                         stroke_width=1))

        print()
        dwg.add(dwg.text(
            f"{i:0{bits}b}",
            insert=(lx, ly),
            font_size=16,
            text_anchor="start" if i < total_segments / 2 else "end"
        ))

   
size = 600
dwg = svgwrite.Drawing("outputs/lec0-1/q1.svg", size=(size, size))

bits = 4
draw_labeled_circle(N=2**(bits-1),bits=bits,size = size)
dwg.save()

print(f"Saved as q1.svg")