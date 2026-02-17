import cairo

import box_around_image

import solar_generator
import natural_gas_generator

import transmission_system
import primary_distribution_system
import secondary_distribution_system

import generator_substation
import distribution_substation

global_x_offset = -450
global_y_offset = -710

width = 1960
height = 635

surface = cairo.SVGSurface("Electric grid diagram.svg", width, height)

painting_context = cairo.Context(surface)
painting_context.set_source_rgb(1,1,1)
painting_context.paint()

box_around_image.draw_box_around_image(cairo.Context(surface), width, height)

solar_generator.draw_solar_generator(cairo.Context(surface), global_x_offset+355, global_y_offset+990)
natural_gas_generator.draw_natural_gas_generator(cairo.Context(surface), global_x_offset+300, global_y_offset+750)

transmission_system.draw_transmission_system(cairo.Context(surface), global_x_offset+750, global_y_offset+750)
primary_distribution_system.draw_primary_distribution_system(cairo.Context(surface), global_x_offset+1650, global_y_offset+405)

secondary_distribution_system.draw_secondary_distribution_system(cairo.Context(surface), global_x_offset+1720, global_y_offset+675)

generator_substation.draw_generator_substation(cairo.Context(surface), global_x_offset+750, global_y_offset+750)
generator_substation.draw_generator_substation(cairo.Context(surface), global_x_offset+750, global_y_offset+1070)
distribution_substation.draw_distribution_substation(cairo.Context(surface), global_x_offset+1380, global_y_offset+750)







surface.finish()
