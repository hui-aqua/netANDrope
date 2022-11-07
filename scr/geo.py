import numpy as np

# net panel is on Y-O-Z plane
# HHH
seg_num=500
x=np.linspace(-10,10,seg_num+1)
node_position=[]
for i in x:
    for j in x:
        node_position.append([0,i,j])
vline=[]
for i in range(seg_num+1):
    for j in range(seg_num):
        vline.append([j+i*(seg_num+1),j+1+i*(seg_num+1)])
hline=[]        
for i in range(seg_num+1):
    for j in range(seg_num):
        hline.append([j*(seg_num+1)+i,(j+1)*(seg_num+1)+i])
all_line=vline+hline

# XXX
seg_num=500
x=np.linspace(-10,10,seg_num+1)
node_position=[]
for i in x:
    for j in x:
        node_position.append([0,i,j])
vline=[]
for i in range(seg_num+1):
    for j in range(seg_num):
        vline.append([j+i*(seg_num+1),j+1+i*(seg_num+1)])
hline=[]        
for i in range(seg_num+1):
    for j in range(seg_num):
        hline.append([j*(seg_num+1)+i,(j+1)*(seg_num+1)+i])
all_line=vline+hline
