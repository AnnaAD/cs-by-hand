from svg_module import draw_module
from svg_logic import draw_wire, draw_mux, draw_mux_2

def draw_beta_processor(dwg,x,y,margin, mode=""):
    
    draw_module(dwg, x,y,100,30, ["IN",">"],["OUT"] ,"PC")
    draw_module(dwg, x,y+50,30,30, [""],[""] ,"+4")

    instr = draw_module(dwg, x+margin+100,y, 100,100 ,["A"], ["D"], "Inst. Memory")

    signals = ["ALUFN", "WERF"]
    if "opc" in mode:
        signals.append("BSEL")
    draw_module(dwg, x+margin*3+200,y, 200,100 ,["OPCODE"],signals , "Control Logic")


    draw_module(dwg,x+margin*2+200,y+150+margin*2,140,140,["RA1","RA2", "WA","WE","WD",">"],["RD1", "RD2"],"Register File")

    draw_module(dwg, x+margin*3+100,y+150*2+margin*3,100,100, ["A","B", "ALUFN"],["D"] ,"ALU")
    draw_module(dwg, x+margin*3+100,y+150*2+100+margin*4, 100,100,["WD", "A","R/W"], ["RD"], "Data Memory")

    print(instr)
    draw_wire(dwg,instr["outputs"][0], (x+15*16+50,y+margin+100))

    dx = 0
    box_size = 15
    for i in range(32):
        dwg.add(dwg.rect(
                insert=(x+dx, y+margin + 100),
                size=(box_size, box_size),
                fill="none",
                stroke="black",
                stroke_width=2
        ))
        dx += box_size
    
    if("opc" in mode):
        #draw BSEL mux
        draw_mux_2(dwg, x+margin*2,y+150*2+margin*3,80,["",""]," ",rotate=90)
        pass
    
