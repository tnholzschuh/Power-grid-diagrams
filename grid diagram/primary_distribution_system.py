import cairo

import math



def draw_primary_distribution_system(context, x_offset, y_offset):
  context.translate(x_offset, y_offset)
  context.set_source_rgb(0, 0, 0)
  context.set_line_width(6)

  # Voltage text
  context.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
  context.set_font_size(50)
  context.move_to(10, 385)
  context.show_text("12 kV")
  context.stroke()

  # Top line
  context.arc(125, 400, 50, 0, math.pi/2)
  context.stroke()

  # Middle line
  context.move_to(125, 500)
  context.line_to(325, 500)
  context.stroke()

  context.arc(325, 550, 50, -math.pi/2, 0)
  context.stroke()

  context.rectangle(375-15, 550, 30, 30)
  context.stroke()

  context.move_to(375, 580)
  context.line_to(375, 845)
  context.stroke()


  # Bottom line
  context.arc(125, 600, 50, -math.pi/2, 0)
  context.stroke()

  context.move_to(175, 600)
  context.line_to(175, 700)
  context.stroke()

  context.rectangle(160, 700, 30, 30)
  context.stroke()

  context.move_to(175, 730)
  context.line_to(175, 845)
  context.stroke()



