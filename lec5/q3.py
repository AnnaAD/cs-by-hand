from svg_beta import draw_beta_processor
from svg_logic import draw_mux_2
import svgwrite

margin = 40

width = 650
height = 750

dwg = svgwrite.Drawing("outputs/lec5/q3.svg", size=(width,height))

draw_beta_processor(dwg,margin, margin,margin,mode="opc")

dwg.save()