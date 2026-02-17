import cairo

import math



def draw_cell_after_equilibrium_explanation(context, x_offset, y_offset):
  context.translate(x_offset, y_offset)

  # Box
  context.set_source_rgb(1, 1, 1)
  context.rectangle(50, 50, 850, 510)
  context.fill()

  context.set_source_rgb(.7, .7, .7)
  context.rectangle(50, 50, 850, 510)
  context.set_line_width(9)
  # context.stroke()


  # Text
  context.set_source_rgb(0, 0, 0)
  context.set_font_size(80)
  context.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
  context.move_to(75, 160)
  context.show_text("Photon generates high")
  context.move_to(75, 250)
  context.show_text("energy electron, which")
  context.move_to(75, 340)
  context.show_text("is swept to the")
  context.move_to(75, 430)
  context.show_text("negative terminal by")
  context.move_to(75, 520)
  context.show_text("the electric field.")
