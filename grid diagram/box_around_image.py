import cairo

import math



def draw_box_around_image(context, width, height):
  context.set_source_rgb(0, 0, 0)  # Black
  context.set_line_width(6)

  # Draw rectangle around the whole image
  context.rectangle(0.5, 0.5, width - 1, height - 1)
  # 0.5 offset ensures crisp edges on pixel boundaries
  context.stroke()
