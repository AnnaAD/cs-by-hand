import svgwrite
from svg_module import draw_module 
from svg_logic import draw_mux


margin = 40
input_height_area = 100

width = 700
height = 550

dwg = svgwrite.Drawing("outputs/lec4/q2.svg", size=(width,height))

draw_mux(dwg, margin*2+400, margin*2+100, [" "," "]," ")


draw_module(dwg,margin*2,margin*2,200,200,["PC"],["I[4:0]"],"Inst. Mem.")

draw_module(dwg,margin*2+440,margin*2,100,60,[">","IN"],["OUT"],"reg")
draw_module(dwg,width/2-140/2,margin*2+300,140,140,["A[3:0]","B[3:0]", "Cin"],["S[3:0]","Cout"],"4-bit Adder")


draw_module(dwg,margin*2+250,margin*2,80,30,[],[""],f"CLK")

dx = 0
box_size = 30
for i in range(5):
    dwg.add(dwg.rect(
            insert=(margin*2+225+dx, margin*2 + 50),
            size=(box_size, box_size),
            fill="none",
            stroke="black",
            stroke_width=2
    ))
    dx += box_size


dwg.add(dwg.text(
        f"Complete the ADD/Zero Processor",
        insert=(width/2, margin),
        text_anchor="middle",
        font_size=14
    ))

dwg.save()