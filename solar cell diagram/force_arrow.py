import cairo
import math

def draw_force_arrow(context, x_offset, y_offset):
  context.translate(x_offset, y_offset)

  # Arrow
  context.move_to(100, 120)
  context.line_to(100, 450)
  context.set_source_rgb(230.0/255, 212.0/255, 53.0/255)
  context.set_line_width(24)
  context.stroke()

  context.move_to(100, 100)
  context.line_to(130, 150)
  context.line_to(70, 150)
  context.close_path()
  context.fill()


  # Text
  context.move_to(150, 30)
  context.rotate(math.pi/2)
  context.set_source_rgb(0, 0, 0)
  context.set_font_size(70)
  context.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
  # context.move_to(x_offset + 125, y_offset + 130)
  context.show_text("Force from field")
