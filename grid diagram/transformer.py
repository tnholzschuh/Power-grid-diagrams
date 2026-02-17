import cairo
import math



def draw_transformer(context, x_offset, y_offset):
  context.set_line_width(6)
  context.set_source_rgb(0, 0, 0)

  for i in range (0, 4):
    context.arc(50+x_offset, 49+24*i+y_offset, 12, -math.pi/2, math.pi/2)
    context.stroke()

  for i in range (0, 4):
    context.arc(90+x_offset, 49+24*i+y_offset, 12, math.pi/2, -math.pi/2)
    context.stroke()

