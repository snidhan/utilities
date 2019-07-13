import numpy as np
import matplotlib as ml
import matplotlib.pyplot as plt


title_1 = 'defvel_cl_02_40000_46300.dat'
title_2 = 'defvel_cl_33_40000_46300.dat'
title_3 = 'defvel_cl_66_40000_46300.dat'
title_4 = 'defvel_cl_98_40000_46300.dat'

#loading:
x1, y1 = np.loadtxt(title_1, unpack=True)
x2, y2 = np.loadtxt(title_2, unpack=True)
x3, y3 = np.loadtxt(title_3, unpack=True)
x4, y4 = np.loadtxt(title_4, unpack=True)

#range:

xl = 2547  # x = 3 
xr = 0  # x = 40

y1 = 0.25*(y1+y2+y3+y4)


x1 = x1[xl-1:xr-1]
y1 = y1[xl-1:xr-1]


print(y1)


#plot:

fig=plt.loglog(x1,y1,x1,x1**(-1))
plt.axis([2,20,0.01,1.4])

plt.xlabel('x/D')
plt.title('Center line defect velocity.  Spheroid Re=$10^4$')

plt.setp(fig[0], color='tab:red', linewidth=2.0,label='$U_d \quad F=\infty$ ')
plt.setp(fig[1], color='tab:red', linewidth=1.0, linestyle='dashed',label='$\sim x^{-1}$')


plt.legend()


#saving:

#plt.savefig('defvel.png', format='png', dpi=300)

plt.show()

