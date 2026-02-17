import cairo

import math


#2300 by 850
def draw_cell_after_equilibrium(context, x_offset, y_offset):
  # Green box
  context.set_source_rgb(62.0/255, 134.0/255, 66.0/255)
  context.rectangle(x_offset + 250, y_offset + 100, 1800, 600)
  context.fill()

  # Top current collector
  context.set_source_rgb(0, 0, 0)
  context.rectangle(x_offset + 900, y_offset + 90, 500, 20)
  context.fill()

  # Top current collector
  context.set_source_rgb(0, 0, 0)
  context.rectangle(x_offset + 240, y_offset + 690, 1820, 20)
  context.fill()

  # n region
  for i in range(0, 4):
    context.set_source_rgb(230.0/255, 212.0/255, 53.0/255)
    context.arc(x_offset + 400 + 510*i, y_offset + 160, 25, 0 , 2*math.pi)
    context.fill()

  # p region
  for i in range(0, 6):
    context.set_source_rgb(1, 1, 1)
    context.arc(x_offset + 340 + 310*i, y_offset + 640, 25, 0 , 2*math.pi)
    context.fill()

  # Top terminal
  context.set_source_rgb(0, 0, 0)
  context.rectangle(x_offset + 1130, y_offset + 50, 40, 40)
  context.fill()

  context.set_source_rgb(0, 0, 0)
  context.set_font_size(170)
  context.move_to(x_offset + 1180, y_offset + 75)
  context.show_text("-")

  # Bottom terminal
  context.set_source_rgb(0, 0, 0)
  context.rectangle(x_offset + 1130, y_offset + 710, 40, 40)
  context.fill()

  context.set_source_rgb(0, 0, 0)
  context.set_font_size(100)
  context.move_to(x_offset + 1180, y_offset + 800)
  context.show_text("+")

