import numpy as np
import matplotlib as ml
import matplotlib.pyplot as plt



data_mke_cl=np.loadtxt('./ke_plots/MKE_cl.dat')

x    = data_mke_cl[:,0]
mke  = data_mke_cl[:,1]


data_tke_cl=np.loadtxt('./ke_plots/TKE_cl.dat')


x    = data_tke_cl[:,0]
tke  = data_tke_cl[:,1]


data_mke_cl_Karu=np.loadtxt('./ke_plots/MKE_cl_Karu.dat')


x_Karu    = data_mke_cl_Karu[1:115,0]
mke_Karu  = data_mke_cl_Karu[1:115,1]


data_tke_cl_Karu=np.loadtxt('./ke_plots/TKE_cl_Karu.dat')


x_Karu    = data_tke_cl_Karu[1:115,0]
tke_Karu  = data_tke_cl_Karu[1:115,1]




plt.figure(figsize=(10,7))
fig=plt.loglog(x,mke,x,tke,x_Karu,mke_Karu,x_Karu,tke_Karu)
plt.axis([0.6, 20,0.0007,1])
plt.setp(fig[0], color='tab:red', linewidth=2.0,label='MKE Actual grid')
plt.setp(fig[1], color='tab:blue', linewidth=2.0,label='TKE Actual grid')
plt.setp(fig[2], color='tab:red',linewidth=1.0, linestyle='dashed',label='MKE High resolution grid')
plt.setp(fig[3], color='tab:blue',linewidth=1.0, linestyle='dashed',label='TKE High resolution grid')
#plt.ylabel('')
plt.xlabel('x/D')
plt.title('Energy in the centerline.  Sphere Re=$10^4$ Fr=3')
plt.legend()

plt.savefig('test.svg', format='svg', dpi=1000)






plt.show()
