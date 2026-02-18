import cairo

import box_around_image

import feeder
import time_current_graph

global_x_offset = -450
global_y_offset = -460

width = 1170
height = 840

surface = cairo.SVGSurface("Distribution protection diagram.svg", width, height)

painting_context = cairo.Context(surface)
painting_context.set_source_rgb(1,1,1)
painting_context.paint()

box_around_image.draw_box_around_image(cairo.Context(surface), width, height)

feeder.draw_feeder(cairo.Context(surface),500+global_x_offset, 500+global_y_offset)
time_current_graph.draw_time_current_graph(cairo.Context(surface), 600+global_x_offset, 800+global_y_offset)


surface.finish()
