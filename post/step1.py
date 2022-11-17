import json
import numpy as np
import matplotlib.pyplot as plt
run_time=20
dt = 1.0e-2     # Time steps, unit [s]
num_sub_step=[5,15]
i=0
time_list=[]
while round(dt*i,2)<run_time:
    time_list.append(round(dt*i,2))
    i+=4


for w in num_sub_step:
    f=open("ami1/New_dt"+str(dt)+"sub_"+str(w) +"results.json")
    resu=json.load(f)
    f.close()
    # print(resu.keys())
    print("read finish")
    v_max_mean_min_std=[]

    for item in time_list:
        v_node=np.linalg.norm(np.array(resu["velocity"+str(item)]),axis=1)
        v_max_mean_min_std.append([np.max(v_node),np.mean(v_node),np.min(v_node),np.std(v_node)])
    np.savetxt("post/velocity_sta_dt"+str(dt)+"sub_"+str(w)+".txt",np.array(v_max_mean_min_std))
    print("save finish")

plt.figure()
plt.plot(time_list,np.array(v_max_mean_min_std))
plt.yscale('log')
plt.show()