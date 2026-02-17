import cairo

import math

import transformer
import fuse


def draw_secondary_distribution_system(context, x_offset, y_offset):
  context.translate(x_offset, y_offset)
  context.set_source_rgb(0, 0, 0)
  context.set_line_width(6)

  # Voltage text
  context.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
  context.set_font_size(50)
  context.move_to(485, 460)
  context.show_text("±120 V")
  context.stroke()

  # Fuses
  fuse.draw_fuse(context, 255, 335)
  fuse.draw_fuse(context, 255, 460)

  # Distribution transformer
  transformer.draw_transformer(context, 315, 300)
  transformer.draw_transformer(context, 315, 425)


  # Secondary lines
  context.move_to(400, 385)
  context.line_to(455, 385)
  context.stroke()

  context.move_to(400, 510)
  context.line_to(455, 510)
  context.stroke()

