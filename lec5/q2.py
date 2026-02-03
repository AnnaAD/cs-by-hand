from svg_beta import draw_beta_processor
import svgwrite

margin = 40

width = 650
height = 500

dwg = svgwrite.Drawing("outputs/lec5/q2.svg", size=(width,height))

draw_beta_processor(dwg,margin, margin,margin)


dwg.save()