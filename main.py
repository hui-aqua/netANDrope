import sys
import numpy as np
import json
import scr.saveVtk as sv
import scr.geo as geo
import scr.line as le

sv.write_line_vtk("rope",point=geo.node_position,line=geo.all_rope)
sv.write_vtk("net",point=geo.node_position,line=geo.twine,face=geo.net)
print("number of node: "+str(len(geo.node_position)))
print("number of line: "+str(len(geo.all_rope)))


run_time=20  #s [5,25,50,75,100,150,200,250,300]       # Total simulation run time, unit [s]   
dt = 1.0e-3     # Time steps, unit [s]
num_sub_step=sys.argv[1]
# material 
net_length=20.0

seg_length=net_length/geo.seg_num
k_rope=1.25e11*0.25*pow(0.010,2)/seg_length
k_twine=1.03e11*0.25*pow(0.004,2)/(seg_length*np.sqrt(2))

rope=le.lines(geo.all_rope,k_rope,0.01)   
twine=le.lines(geo.twine,k_twine,0.004)


gravity=np.array([0,0,-9.81])

## initialization 
position=np.array(geo.node_position)
velocity=np.zeros_like(position)
rope.assign_length(position)
twine.assign_length(position)
fixed_point=geo.fixed_node
results={}

f_current=40000#N
f_c_per_node=40000/len(position)

i=0
while round(dt*i,2)<run_time:
# for i in range(int(run_time/dt)):       
    if i % round(float(0.04)/float(dt)) == 0:                # Write vtk result per 0.04s, 25fps
        print("save results at {:.2f} s".format(round(dt*i,2)))
        sv.write_vtk("ami2/net_dt"+str(dt)+"sub_"+str(num_sub_step)+"_"+str(i),point=position.tolist(),line=geo.twine,face=geo.net)
        results["position"+str(round(dt*i,2))]=position.tolist()
        results["velocity"+str(round(dt*i,2))]=velocity.tolist()


    ### Forward Euler (Explicit)
    ## External loads
    pre_position=position.copy()
    
    # Gravity force
    velocity += dt*gravity
    velocity += dt*f_c_per_node*min(float(i/1e4),1)/geo.mass
    
    ## boundary condition
    velocity[fixed_point] *= 0.0  # velocity restriction
    position += dt*velocity
    position[fixed_point]=np.array(geo.node_position)[fixed_point]
    for w in range(int(num_sub_step)):
        ### constraint function 
        position+=rope.pbd_edge_constraint(position,geo.mass,dt)
        position+=twine.pbd_edge_constraint(position,geo.mass,dt)
    
    ### velocity correction
    velocity=(position-pre_position)/dt 
    i+=1
    
json=json.dumps(results)    
# open file for writing, "w" 
f = open("ami1/New_dt"+str(dt)+"sub_"+str(num_sub_step) +"results.json","w")
# write json object to file
f.write(json)
# close file
f.close()
