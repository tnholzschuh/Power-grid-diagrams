import cairo

import box_around_image
import diagram_title
import cell_after_equilibrium
import photon_generating_electron
import force_arrow
import diffusion_arrow
import cell_after_equilibrium_explanation
import cell_before_equilibrium
import cell_before_equilibrium_explanation
import cell_legend

surface = cairo.SVGSurface("Solar cell diagram.svg", 3400, 3400)

painting_context = cairo.Context(surface)
painting_context.set_source_rgb(1,1,1)
painting_context.paint()

box_around_image.draw_box_around_image(cairo.Context(surface), 3400, 3400)

cell_after_equilibrium.draw_cell_after_equilibrium(cairo.Context(surface), 1000, 500)
cell_before_equilibrium.draw_cell_before_equilibrium(cairo.Context(surface), 1140, 1500)

# cell_legend.draw_cell_legend(cairo.Context(surface), 1800, 2400)
cell_legend.draw_cell_legend(cairo.Context(surface), 610, 1325)


force_arrow.draw_force_arrow(cairo.Context(surface), 3000, 625)
diffusion_arrow.draw_diffusion_arrow(cairo.Context(surface), 930, 505)


photon_generating_electron.draw_photon_generating_electron(cairo.Context(surface), 1500, 700)

diagram_title.draw_diagram_title(cairo.Context(surface), 1200, 100)

cell_after_equilibrium_explanation.draw_cell_after_equilibrium_explanation(cairo.Context(surface), 50, 600)

cell_before_equilibrium_explanation.draw_cell_before_equilibrium_explanation(cairo.Context(surface), 50, 1720)

surface.finish()
