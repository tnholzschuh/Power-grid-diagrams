import cairo

import math



def draw_feeder(context, x_offset, y_offset):
  context.translate(x_offset, y_offset)
  context.set_source_rgb(0, 0, 0)
  context.set_line_width(14)

  # Bus
  context.set_line_width(14)
  context.move_to(250, 70)
  context.line_to(250, 190)
  context.stroke()

  # Line
  context.set_line_width(6)
  context.move_to(250, 130)
  context.line_to(275, 130)
  context.stroke()

  context.move_to(305, 130)
  context.line_to(455, 130)
  context.stroke()

  context.move_to(485, 130)
  context.line_to(635, 130)
  context.stroke()

  context.move_to(665, 130)
  context.line_to(815, 130)
  context.stroke()

  context.move_to(845, 130)
  context.line_to(995, 130)
  context.stroke()

  # Circuit breakers
  context.rectangle(275, 115, 30, 30)
  context.stroke()

  context.rectangle(455, 115, 30, 30)
  context.stroke()

  context.rectangle(635, 115, 30, 30)
  context.stroke()

  context.rectangle(815, 115, 30, 30)
  context.stroke()

  # Labels
  context.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
  context.set_font_size(50)
  context.move_to(250, 50)
  context.show_text("CB")

  context.move_to(445, 50)
  context.show_text("R\u2081")

  context.move_to(625, 50)
  context.show_text("R\u2082")

  context.move_to(805, 50)
  context.show_text("R\u2083")

