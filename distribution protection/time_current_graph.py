import cairo

import math



def draw_time_current_graph(context, x_offset, y_offset):
  context.translate(x_offset, y_offset)
  context.set_source_rgb(0, 0, 0)
  context.set_line_width(6)

  # Bars
  for i in range(0, 4):
    context.rectangle(155+180*i, 50+i*320.0/5, 65, 320-i*320.0/5+2)
    context.fill()

  # Axes
  context.move_to(50, 375)
  context.line_to(925, 375)
  context.stroke()

  context.move_to(925, 375)
  context.line_to(925, 360)
  context.line_to(955, 375)
  context.line_to(925, 390)
  context.line_to(925, 375)
  context.close_path()
  context.fill()

  context.move_to(50, 375)
  context.line_to(50, 0)
  context.stroke()

  context.move_to(50, 0)
  context.line_to(35, 0)
  context.line_to(50, -30)
  context.line_to(65, 0)
  context.line_to(50, 0)
  context.close_path()
  context.fill()

  # Labels
  context.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
  context.set_font_size(50)
  context.move_to(-100, 195)
  context.show_text("Time")

  context.move_to(150, 450)
  context.show_text("CB")

  context.move_to(345, 450)
  context.show_text("R\u2081")

  context.move_to(525, 450)
  context.show_text("R\u2082")

  context.move_to(705, 450)
  context.show_text("R\u2083")
