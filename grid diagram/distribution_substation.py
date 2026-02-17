
import cairo

import math

import transformer


def draw_distribution_substation(context, x_offset, y_offset):
  context.translate(x_offset, y_offset)

  # Circuit breakers
  # High voltage
  context.set_source_rgb(0, 0, 0)
  context.set_line_width(6)

  context.rectangle(95, 115, 30, 30)
  context.stroke()

  context.rectangle(95, 165, 30, 30)
  context.stroke()

  context.rectangle(175, 140, 30, 30)
  context.stroke()

  # Low voltage
  context.rectangle(285, 140, 30, 30)
  context.stroke()

  context.rectangle(365, 90, 30, 30)
  context.stroke()

  context.rectangle(365, 140, 30, 30)
  context.stroke()

  context.rectangle(365, 190, 30, 30)
  context.stroke()

  # Busses
  context.move_to(150, 75)
  context.line_to(150, 230)
  context.set_line_width(14)
  context.stroke()

  context.move_to(340, 60)
  context.line_to(340, 245)
  context.set_line_width(14)
  context.stroke()

  # Transformer
  transformer.draw_transformer(context, 175, 70)

  # Connections
  # High voltage
  context.move_to(125, 180)
  context.line_to(150, 180)
  context.set_line_width(6)
  context.stroke()

  context.move_to(125, 130)
  context.line_to(150, 130)
  context.set_line_width(6)
  context.stroke()

  context.move_to(150, 155)
  context.line_to(175, 155)
  context.set_line_width(6)
  context.stroke()

  context.move_to(205, 155)
  context.line_to(230, 155)
  context.set_line_width(6)
  context.stroke()

  # Low voltage
  context.move_to(265, 155)
  context.line_to(285, 155)
  context.set_line_width(6)
  context.stroke()

  context.move_to(315, 155)
  context.line_to(340, 155)
  context.set_line_width(6)
  context.stroke()

  context.move_to(340, 105)
  context.line_to(365, 105)
  context.set_line_width(6)
  context.stroke()

  context.move_to(340, 155)
  context.line_to(365, 155)
  context.set_line_width(6)
  context.stroke()

  context.move_to(340, 205)
  context.line_to(365, 205)
  context.set_line_width(6)
  context.stroke()




