import cairo

import math



def draw_cell_legend(context, x_offset, y_offset):
  context.scale(1.8, 1.8)
  # Legend box 
  context.set_source_rgb(1, 1, 1)
  context.rectangle(x_offset + 50, y_offset + 50, 600, 380)
  context.fill()

  context.set_source_rgb(0, 0, 0)
  context.rectangle(x_offset + 50, y_offset + 50, 600, 380)
  context.set_line_width(3)
  context.stroke()


  # Legend text
  context.set_source_rgb(0, 0, 0)
  context.set_font_size(40)
  context.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
  context.move_to(x_offset + 125, y_offset + 130)
  context.show_text(": high energy electrons")

  context.move_to(x_offset + 125, y_offset + 215)
  context.show_text(": missing electrons")

  context.move_to(x_offset + 130, y_offset + 300)
  context.show_text(": electrons locked in place")

  context.move_to(x_offset + 75, y_offset + 380)
  context.show_text("hν : photon or light")


  # Legend symbols
  context.set_source_rgb(230.0/255, 212.0/255, 53.0/255)
  context.arc(x_offset + 95, y_offset +118, 25, 0 , 2*math.pi)
  context.fill()

  context.set_source_rgb(0, 0, 0)
  context.arc(x_offset + 95, y_offset +118, 25, 0 , 2*math.pi)
  context.set_line_width(2)
  context.stroke()


  context.set_source_rgb(1, 1, 1)
  context.arc(x_offset + 95, y_offset + 204, 25, 0 , 2*math.pi)
  context.fill()

  context.set_source_rgb(0, 0, 0)
  context.arc(x_offset + 95, y_offset + 204, 25, 0 , 2*math.pi)
  context.set_line_width(2)
  context.stroke()


  context.set_source_rgb(62.0/255, 134.0/255, 66.0/255)
  context.rectangle(x_offset + 70, y_offset + 260, 50, 50)
  context.fill()

  context.set_source_rgb(0, 0, 0)
  context.rectangle(x_offset + 70, y_offset + 260, 50, 50)
  context.set_line_width(2)
  context.stroke()
