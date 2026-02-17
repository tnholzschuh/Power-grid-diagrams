import cairo
import math

def draw_photon_generating_electron(context, x_offset, y_offset):
  context.translate(x_offset, y_offset)

  # Text
  context.move_to(100, 40)
  context.set_source_rgb(0, 0, 0)
  context.set_font_size(70)
  context.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
  # context.move_to(x_offset + 125, y_offset + 130)
  context.show_text("hν")

  # Electron hole pair
  context.set_source_rgb(1, 1, 1)
  context.arc(210, 155, 25, 0 , 2*math.pi)
  context.fill()

  context.set_source_rgb(230.0/255, 212.0/255, 53.0/255)
  context.arc(200, 150, 25, 0 , 2*math.pi)
  context.fill()

  # Arrow
  context.rotate(-math.pi*(1.0/8))

  context.move_to(120, 100)
  context.line_to(120, 170)
  context.set_source_rgb(0, 0, 0)
  context.set_line_width(6)
  context.stroke()

  context.move_to(120, 180)
  context.line_to(110, 160)
  context.line_to(130, 160)
  context.close_path()

  context.fill()



