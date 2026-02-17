import cairo

import math



def draw_transmission_system(context, x_offset, y_offset):
  context.translate(x_offset, y_offset)
  context.set_source_rgb(0, 0, 0)

  # Voltage text
  context.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
  context.set_font_size(50)
  context.move_to(00, 40)
  context.show_text("115 kV")

  context.move_to(700, 40)
  context.show_text("115 kV")

  # Top line

  context.move_to(125, 130)
  context.line_to(725, 130)
  context.set_line_width(6)
  context.stroke()

  # Left line
  context.arc(125, 230, 50, -math.pi/2, 0)
  context.stroke()

  context.move_to(175, 230)
  context.line_to(175, 400)
  context.stroke()

  context.arc(125, 400, 50, 0, math.pi/2)
  context.stroke()

  # Bottom line
  context.move_to(125, 500)
  context.line_to(475, 500)
  context.stroke()

  context.arc(475, 450, 50, 0, math.pi/2)
  context.stroke()

  context.move_to(525, 450)
  context.line_to(525, 230)
  context.stroke()

  context.arc(575, 230, 50, math.pi, 3*math.pi/2)
  context.stroke()

  context.move_to(575, 180)
  context.line_to(725, 180)
  context.stroke()
