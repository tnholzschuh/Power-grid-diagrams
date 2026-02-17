import cairo

import math



def draw_cell_before_equilibrium_explanation(context, x_offset, y_offset):
  context.translate(x_offset, y_offset)

  # Box
  context.set_source_rgb(1, 1, 1)
  context.rectangle(50, 50, 850, 250)
  context.fill()

  context.set_source_rgb(.7, .7, .7)
  context.rectangle(50, 50, 850, 250)
  context.set_line_width(9)
  # context.stroke()


  # Text
  context.set_source_rgb(0, 0, 0)
  context.set_font_size(80)
  context.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
  context.move_to(75, 160)
  context.show_text("As constructed, before")
  context.move_to(75, 250)
  context.show_text("diffusion")
