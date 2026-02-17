import cairo

import math



def draw_diagram_title(context, x_offset, y_offset):
  # Box
  context.set_source_rgb(1, 1, 1)
  context.rectangle(x_offset + 50, y_offset + 50, 850, 210)
  context.fill()

  context.set_source_rgb(.7, .7, .7)
  context.rectangle(x_offset + 50, y_offset + 50, 850, 210)
  context.set_line_width(9)
  # context.stroke()


  # Text
  context.set_source_rgb(0, 0, 0)
  context.set_font_size(150)
  context.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
  context.move_to(x_offset + 165, y_offset + 200)
  context.show_text("Solar cell")

