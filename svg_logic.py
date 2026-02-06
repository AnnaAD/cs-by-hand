import svgwrite

def string_to_path(svg_string):
    commands = ["M", "V", "H", "c", "s", "z", "m", "L","C","h","l","S"]

    import re

    result = re.split(r'([MVHcszmLChlS])', svg_string)
    output = []
    i = 0
    while i < len(result):
        if(result[i] in commands):
            working = [result[i]]
            partial = re.split(r"[,\s]+",result[i+1])

            terms = []
            negate = False
            for p in partial:
                t = re.split(r"(\-)", p)
                for j in t:
                    if j == "-":
                        negate = True
                    elif j.strip():
                        terms.append(float(j) if not negate else -1*float(j))
                        negate = False
            if(terms):
                if(len(terms) > 1):
                    working.append(tuple(terms))
                else:
                    working.append(terms[0])
            output.append(tuple(working))
            i+=2
        else:
            i+=1
    return output

def draw_and(dwg,x,y, inputs = [], output = "",negate=False):
    and_path = string_to_path("M30 5V45H50.47619c11.267908 0 20-9.000045 20-20s-8.732091-20-20-20H30zm2.857143 2.857143H50.47619c9.760663 0 16.666667 7.639955 16.666667 17.142857 0 9.502902-7.382195 17.142857-17.142857 17.142857H32.857143V7.857143z")
    and_sym = dwg.path(d=and_path)
    and_sym.translate(-30,-5)
    and_sym.translate(x,y)
    dwg.add(and_sym)

    if(negate):
        not_circle = dwg.circle(center=(42,20),
                       r=3,
                       fill="none",
                       stroke="black",
                       stroke_width=3)
        not_circle.translate(x,y)
        dwg.add(not_circle)
    
    ty = 10
    for i in inputs:
        l = dwg.text(
            f"{i}",
            insert=(-15, ty),
            text_anchor="middle",
            font_size=14
        )
        l.translate(x,y)
        dwg.add(l)

        l = dwg.line(
            start=(-10,ty),
            end=(0, ty),
            stroke="black",
            stroke_width=2
        )
        l.translate(x,y)
        dwg.add(l)
        ty+=20
    
    negate_offset = 5 if negate else 0

    if output:
        l = dwg.text(
            f"{output}",
            insert=(55 + negate_offset, 22),
            text_anchor="middle",
            font_size=14
        )
        l.translate(x,y)
        dwg.add(l)

        l = dwg.line(
            start=(40 + negate_offset,20),
            end=(50 + negate_offset, 20),
            stroke="black",
            stroke_width=2
        )
        l.translate(x,y)
        dwg.add(l)

def draw_or(dwg,x,y, inputs = [], output = "", negate=False):
    or_path = string_to_path("M 7.6700216,44.5 L 9.6700216,46.9375 C 9.6700216,46.9375 15.326272,53.937549 15.326272,64.5 C 15.326272,75.062451 9.6700216,82.0625 9.6700216,82.0625 L 7.6700216,84.5 L 10.826272,84.5 L 24.826272,84.5 C 27.234348,84.500001 32.515971,84.524514 38.451272,82.09375 C 43.952029,79.840951 50.024779,75.456504 54.984922,67.238862 L 53.826272,64.5 L 54.987161,61.767184 C 44.664037,44.700133 29.409159,44.5 24.826272,44.5 L 10.826272,44.5 L 7.6700216,44.5 z M 13.545022,47.5 L 24.826272,47.5 C 29.510445,47.5 43.113122,47.369793 52.795022,64.5 C 48.028236,72.929075 42.273741,77.18391 37.076272,79.3125 C 31.715611,81.507924 27.234347,81.500001 24.826272,81.5 L 13.576272,81.5 C 15.44986,78.391566 18.326272,72.45065 18.326272,64.5 C 18.326272,56.526646 15.41774,50.599815 13.545022,47.5 z")
    or_sym = dwg.path(d=or_path)
    or_sym.translate(-10,-45)
    or_sym.translate(x,y)

    if(negate):
        not_circle = dwg.circle(center=(48,20),
                       r=3,
                       fill="none",
                       stroke="black",
                       stroke_width=3)
        not_circle.translate(x,y)
        dwg.add(not_circle)
    
    ty = 10
    for i in inputs:
        l = dwg.text(
            f"{i}",
            insert=(-10, ty),
            text_anchor="middle",
            font_size=14
        )
        l.translate(x,y)
        dwg.add(l)

        l = dwg.line(
            start=(-5,ty),
            end=(5, ty),
            stroke="black",
            stroke_width=2
        )
        l.translate(x,y)
        dwg.add(l)
        ty+=20
    
    negate_offset = 5 if negate else 0
    if output:
        l = dwg.text(
            f"{output}",
            insert=(60 + negate_offset, 22),
            text_anchor="middle",
            font_size=14
        )
        l.translate(x,y)
        dwg.add(l)

        l = dwg.line(
            start=(45+negate_offset,20),
            end=(55+negate_offset, 20),
            stroke="black",
            stroke_width=2
        )
        l.translate(x,y)
        dwg.add(l)
   
    dwg.add(or_sym)

def draw_xor(dwg,x,y, inputs = [], output = "",negate = False):
    xor_path1 = string_to_path("M24.25 42C22.65263 44.6444 22 45 22 45h-3.65625l2-2.4375S26 35.56245 26 25 20.34375 7.4375 20.34375 7.4375l-2-2.4375H22c.78125 .9375 1.42188 1.65625 2.21875 3C26.09147 11.09981 29 17.02665 29 25c0 7.95065-2.8967 13.87942-4.75 17z")
    xor_path2 = string_to_path("M24.09375 5l2 2.4375S31.75 14.43755 31.75 25s-5.65625 17.5625-5.65625 17.5625l-2 2.4375H41.25c2.40808 0 7.6897 .02451 13.625-2.40625s12.53654-7.34327 17.6875-16.875L71.25 25l1.3125-.71875C62.25939 5.21559 46.00657 5 41.25 5H24.09375zm5.875 3H41.25c4.68417 0 18.28685-.1302 27.96875 17C64.45196 33.42907 58.69747 37.68391 53.5 39.8125 48.13934 42.00792 43.65808 42 41.25 42H30c1.87359-3.10843 4.75-9.04935 4.75-17 0-7.97335-2.90853-13.90019-4.78125-17z")

    for path in [xor_path1, xor_path2]:
        xor_sym = dwg.path(d=path)
        xor_sym.translate(-30,-5)
        xor_sym.translate(x,y)
        dwg.add(xor_sym)
    
    if(negate):
        not_circle = dwg.circle(center=(42,20),
                       r=3,
                       fill="none",
                       stroke="black",
                       stroke_width=3)
        not_circle.translate(x,y)
        dwg.add(not_circle)
    
    ty = 10
    for i in inputs:
        l = dwg.text(
            f"{i}",
            insert=(-20, ty),
            text_anchor="middle",
            font_size=14
        )
        l.translate(x,y)
        dwg.add(l)

        l = dwg.line(
            start=(-15,ty),
            end=(-5, ty),
            stroke="black",
            stroke_width=2
        )
        l.translate(x,y)
        dwg.add(l)
        ty+=20
    
    negate_offset = 5 if negate else 0
    if output:
        l = dwg.text(
            f"{output}",
            insert=(55+negate_offset, 22),
            text_anchor="middle",
            font_size=14
        )
        l.translate(x,y)
        dwg.add(l)

        l = dwg.line(
            start=(40+negate_offset,20),
            end=(50 + negate_offset, 20),
            stroke="black",
            stroke_width=2
        )
        l.translate(x,y)
        dwg.add(l)

    
def draw_buffer(dwg,x,y, negate=False):
    buffer_path = string_to_path("M 38,2.59375 L 38,5 L 38,45 L 38,47.40625 L 40.109024,46.34375 L 79.184573,26.87052 L 78.840667,22.958095 L 40.109024,3.65625 L 38,2.59375 z M 41.109024,7.40625 L 76.268082,25 L 41.109024,42.59375 L 41.109024,7.40625 z")
    buf_sym = dwg.path(d=buffer_path)
    buf_sym.translate(-40,-5)
    buf_sym.translate(x,y)
    dwg.add(buf_sym)

    if(negate):
        not_circle = dwg.circle(center=(40,20),
                       r=3,
                       fill="none",
                       stroke="black",
                       stroke_width=3)
        not_circle.translate(x,y)
        dwg.add(not_circle)

def draw_mux(dwg,x,y, inputs = [], output = "", negate=False):
    buffer_path = string_to_path("m 28,81 0,-95 32.5,17.5 0,60 -32.5,17.5 z")
    buf_sym = dwg.path(d=buffer_path, fill="none", stroke="black", stroke_width = 2)
    buf_sym.translate(-50,25)
    buf_sym.translate(x,y)
    dwg.add(buf_sym)

    l = dwg.text(
            f"S",
            insert=(-10, 125),
            text_anchor="middle",
            font_size=14
    )
    l.translate(x,y)
    dwg.add(l)

    l = dwg.line(
        start=(-5,95),
        end=(-5, 110),
        stroke="black",
        stroke_width=2
    )
    l.translate(x,y)
    dwg.add(l)


    ty = 30
    for i in inputs:
        l = dwg.text(
            f"{i}",
            insert=(-35, ty),
            text_anchor="middle",
            font_size=14
        )
        l.translate(x,y)
        dwg.add(l)

        l = dwg.line(
            start=(-20,ty),
            end=(-30, ty),
            stroke="black",
            stroke_width=2
        )
        l.translate(x,y)
        dwg.add(l)
        ty+=60/(len(inputs)-1)
    
    if output:
        l = dwg.text(
            f"{output}",
            insert=(30, 55),
            text_anchor="middle",
            font_size=14
        )
        l.translate(x,y)
        dwg.add(l)

        l = dwg.line(
            start=(10,55),
            end=(25, 55),
            stroke="black",
            stroke_width=2
        )
        l.translate(x,y)
        dwg.add(l)

def draw_wire(dwg, start, end, draw_dot = False):
    sx, sy = start
    ex, ey = end
    mx = (sx + ex) / 2

    dwg.add(dwg.line( start=(sx, sy), end=(mx, sy),
        stroke="black", stroke_width=2
    ))

    dwg.add(dwg.line(start=(mx, sy), end=(mx, ey),
        stroke="black", stroke_width=2
    ))

    dwg.add(dwg.line(start=(mx, ey), end=(ex, ey),
        stroke="black", stroke_width=2
    ))

    if draw_dot:
        dwg.add(dwg.circle(
            center=(mx, sy),
            r=3,
            fill="black"
        ))

def draw_mux_2(dwg,x,y,width,inputs = [], output = "", rotate=0):
    up_mux_path = [("M",(x,y)),("L", (x+10,y+10)), ("L",(x+width-10, y+10)),("L", (x+width, y)),("z")]
    right_mux_path = [("M",(x,y)),("L", (x+10,y+10)), ("L",(x+10, y+width-10)),("L", (x, y+width)),("z")]
    path = dwg.path(d=right_mux_path if rotate == 0 else up_mux_path, fill="none", stroke="black", stroke_width=2)
    dwg.add(
        path
    )
    dwg.add(
        dwg.text(
            f"S",
            insert= (x-15, y+5) if rotate else (x+5,y+width+20),
            text_anchor="middle",font_size=14
        )
    )

    dwg.add(
        dwg.line(
            start= (x+5,y+5) if rotate else (x+5,y+width-5) ,
            end=   (x-12, y+5) if rotate else (x+5,y+width+10),
            stroke="black",stroke_width=2
        )
    )

    input_coord = []

    delta = 20
    for i in inputs:
        dwg.add(dwg.text(
            f"{i}",
            insert=(x+delta, y-15) if rotate else (x-15,y+delta),
            text_anchor="middle", font_size=14
        ))

        dwg.add(dwg.line(
            start=(x+delta,y) if rotate else (x,y+delta),
            end=(x+delta, y-10) if rotate else (x-10,y+delta),
            stroke="black",stroke_width=2
        ))
        input_coord.append((x+delta, y-10) if rotate else (x-10,y+delta))
        delta+=(width-40)/(len(inputs)-1)
    
    if output:
        dwg.add(dwg.text(
            f"{output}",
            insert=(x + width/2, y+35) if rotate else (x+27, y+width/2+5),
            text_anchor="middle",font_size=14
        ))
        dwg.add(dwg.line(
            start= (x + width/2, y+10) if rotate else (x+10, y+width/2),
            end=(x + width/2, y+20) if rotate else (x+20, y+width/2),
            stroke="black",stroke_width=2
        ))
    
    return {
        "inputs": input_coord,
        "output": (x + width/2, y+20) if rotate else (x+20, y+width/2),
        "select": (x-12, y+5) if rotate else (x+5,y+width+10)
    }