
import cairo

import math



def draw_natural_gas_generator(context, x_offset, y_offset):
  context.translate(x_offset, y_offset)

  context.set_source_rgb(0, 0, 0)
  context.set_line_width(6)
  # Smokestack
  context.move_to(200, 200)
  context.line_to(205, 100)
  context.line_to(225, 100)
  context.line_to(230, 200)
  context.line_to(200, 200)
  context.line_to(205, 100)
  context.stroke()

  context.line_to(207, 100)
  context.line_to(207, 90)
  context.line_to(223, 90)
  context.line_to(223, 100)
  context.line_to(207, 100)
  context.line_to(207, 90)
  context.stroke()

  # Base
  context.move_to(200, 200)
  context.line_to(350, 200)
  context.stroke()

  # Building
  context.move_to(260, 200)
  context.line_to(260, 140)

  context.line_to(260+90.0/3, 120)
  context.line_to(260+2*90.0/3, 140)

  context.line_to(350, 120)
  context.line_to(350, 200)
  context.close_path()
  context.stroke()

  context.rectangle(260+90/4.0-3, 155, 90.0/6, 90.0/6)
  context.stroke()

  context.rectangle(260+5*90/8.0-3, 155, 90.0/6, 90.0/6)
  context.stroke()

  # Connection
  context.move_to(350, 155)
  context.line_to(405, 155)
  context.stroke()


