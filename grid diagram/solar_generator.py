
import cairo

import math



def draw_solar_generator(context, x_offset, y_offset):
  context.translate(x_offset, y_offset)

  context.set_source_rgb(0, 0, 0)
  context.set_line_width(6)

  # Panels
  for i in range(0, 4):
    context.move_to(200 + 35*i, 200)
    context.line_to(180 + 35*i, 270)
    context.stroke()

  for i in range(0, 3):
    context.move_to(200-10*i, 200 + 35*i)
    context.line_to(305-10*i, 200 + 35*i)
    context.stroke()

  # Panel outline
  context.move_to(200, 200)
  context.line_to(305, 200)
  context.line_to(285, 270)
  context.line_to(180, 270)
  context.line_to(200, 200)
  context.line_to(305, 200)
  context.stroke()

  # Sun
  context.arc(200, 200, 25, math.pi/180*(100), 0)
  context.stroke()

  # Connection
  context.move_to(295, 235)
  context.line_to(350, 235)
  context.stroke()
