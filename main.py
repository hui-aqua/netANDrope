import scr.saveVtk as sv
import scr.geo as geo
import numpy as np

# sv.write_point_vtk("net",geo.node_position)
sv.write_line_vtk("net",point=geo.node_position,line=geo.all_line)
print("number of node: "+str(len(geo.node_position)))
print("number of line: "+str(len(geo.all_line)))