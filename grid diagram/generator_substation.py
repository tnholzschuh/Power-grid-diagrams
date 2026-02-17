
import cairo

import math

import transformer


def draw_generator_substation(context, x_offset, y_offset):
  context.translate(x_offset, y_offset)

  # Circuit breakers
  context.set_source_rgb(0, 0, 0)
  context.rectangle(95, 115, 30, 30)
  context.set_line_width(6)
  context.stroke()

  context.rectangle(95, 165, 30, 30)
  context.stroke()

  context.rectangle(45-30, 140, 30, 30)
  context.stroke()

  # Bus
  context.move_to(70, 80)
  context.line_to(70, 225)
  context.set_line_width(14)
  context.stroke()

  transformer.draw_transformer(context, -95, 70)

  # Connections
  context.move_to(70, 180)
  context.line_to(95, 180)
  context.set_line_width(6)
  context.stroke()

  context.move_to(70, 130)
  context.line_to(95, 130)
  context.set_line_width(6)
  context.stroke()

  context.move_to(45, 155)
  context.line_to(70, 155)
  context.set_line_width(6)
  context.stroke()

  context.move_to(-15, 155)
  context.line_to(15, 155)
  context.set_line_width(6)
  context.stroke()


