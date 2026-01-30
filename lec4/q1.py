import svgwrite
from svg_module import draw_module 
from svg_logic import draw_mux


margin = 40
input_height_area = 100

width = 700
height = margin*4+input_height_area + 600

dwg = svgwrite.Drawing("outputs/lec4/q1.svg", size=(width,height))

draw_mux(dwg, margin*2+width/2+40, margin*2 + input_height_area, [" "," "]," ")
draw_mux(dwg, margin*2+40, margin*2 + input_height_area, [" "," "]," ")


draw_module(dwg,margin*2+width/2,margin*2 + input_height_area + 200,80,60,["A","B"],["Y"],"+")

draw_module(dwg,margin*2,margin*2+ input_height_area + 200,80,60,["A","B"],["Y"],"*")

draw_module(dwg,margin*2+width/2,margin*2+100 + input_height_area+200,80,30,["A"],["Z"],"=0?")


draw_module(dwg,width/2-200/2 + 80+45,margin*2,30,30,[],[""],f"N")
draw_module(dwg,width/2-200/2,margin*2,80,30,[],[""],f"CLK")

draw_module(dwg,width/2 - 200/2,margin*2+100 + input_height_area+300,200,200,[" "]*5,[" "]*5,"Control Logic FSM", align_label="top")

dwg.add(dwg.text(
        f"Complete the circuit so that it computes N! = N*(N-1)*(N-2)*...*3*2*1",
        insert=(width/2, margin),
        text_anchor="middle",
        font_size=14
    ))

dwg.save()