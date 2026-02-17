import cairo
import math



def draw_fuse(context, x_offset, y_offset):
  context.set_line_width(6)
  context.set_source_rgb(0, 0, 0)

  context.move_to(x_offset+50, y_offset+50)
  context.line_to(x_offset+60, y_offset+50)
  context.line_to(x_offset+60, y_offset+48)
  context.stroke()

  context.arc(70+x_offset, 50+y_offset, 10, math.pi, 0)
  context.stroke()

  context.arc(90+x_offset, 50+y_offset, 10, 0, math.pi)
  context.stroke()

  context.move_to(x_offset+100, y_offset+52)
  context.line_to(x_offset+100, y_offset+50)
  context.line_to(x_offset+110, y_offset+50)
  context.stroke()
