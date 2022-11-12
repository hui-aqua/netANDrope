import numpy as np

# net panel is on Y-O-Z plane
# # HHH
# seg_num=500
# x=np.linspace(-10,10,seg_num+1)
# node_position=[]
# for i in x:
#     for j in x:
#         node_position.append([0,i,j])
# vline=[]
# for i in range(seg_num+1):
#     for j in range(seg_num):
#         vline.append([j+i*(seg_num+1),j+1+i*(seg_num+1)])
# hline=[]        
# for i in range(seg_num+1):
#     for j in range(seg_num):
#         hline.append([j*(seg_num+1)+i,(j+1)*(seg_num+1)+i])
# all_line=vline+hline

# xxx
seg_num=80 # must be 20x 2x
x=np.linspace(-10,10,seg_num+1)
node_position=[]
for i in x:
    for j in x:
        node_position.append([0,i,j])

fixed_node=[]
for i in range(seg_num+1):
    fixed_node.append(i)
    fixed_node.append(i+seg_num*(seg_num+1))
    fixed_node.append(i*(seg_num+1))
    fixed_node.append(seg_num+i*(seg_num+1))
fixed_node=list(set(fixed_node))

# for rope
vrope=[]
for i in range(0,seg_num+1,int(seg_num/20)):
    for j in range(seg_num):
        vrope.append([j+i*(seg_num+1),j+1+i*(seg_num+1)])
hrope=[]        
for i in range(0,seg_num+1,int(seg_num/20)):
    for j in range(seg_num):
        hrope.append([j*(seg_num+1)+i,(j+1)*(seg_num+1)+i])
all_rope=vrope+hrope

# for net
twine=[]
# //
for j in range(0,seg_num,1):
    for i in range(seg_num-j):
        twine.append([i*(seg_num+2)+j,
                  (i+1)*(seg_num+2)+j])
        twine.append([i*(seg_num+2)+j*(seg_num+1),
                  (i+1)*(seg_num+2)+j*(seg_num+1)])
# \\
for j in range(0,seg_num,1):
    for i in range(1,seg_num+1-j):
        twine.append([i*seg_num-j,
                  (i+1)*seg_num-j])
        twine.append([i*seg_num+j*(seg_num+1),
                  (i+1)*seg_num+j*(seg_num+1)])

# for screen model
net=[]
for j in range(seg_num):
    for i in range(seg_num):
        net.append([i+j*(seg_num+1),i+1+j*(seg_num+1),
                    i+(j+1)*(seg_num+1),i+1+(j+1)*(seg_num+1)])



# mass
net_total_mass=2151.6     #kg
rope_total_mass=1.52*11*2 #kg
mass=np.ones((len(node_position),1))
mass*=net_total_mass/len(node_position)
_all_rope=np.array(all_rope).flatten()
mass[_all_rope]+=rope_total_mass/len(_all_rope)
# print(net_total_mass/len(node_position))
# print(rope_total_mass/len(_all_rope))
# print(mass)