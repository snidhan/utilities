import numpy as np

import matplotlib as ml
import matplotlib.pyplot as plt

#from pyvtk import *

def readres(filename):

	f = open(filename,'rb')

	header = np.dtype([('dummy1','int32'),('i','int32'),\
	('j','int32'),('k','int32'),('jp','int32'),\
	('dummy2','int32')])


	my_header = np.fromfile(f,header)

	i = my_header['i'][0]
	j = my_header['j'][0]
	k = my_header['k'][0]


	f.close()

	f= open(filename,'rb')

	raw_data=[('dummy1i','int32'),\
	('data1','float64',i*j),\
        ('dummy2i','int32')]

	restart = np.dtype([('dummy1','int32'),('i','int32'),\
	('j','int32'),('k','int32'),('jp','int32'),\
	('dummy2','int32'),('my_raw_data',raw_data,k),('dummy3','int32'),('nstep','int32'),\
	('dummy4','int32'),('dummy5','int32'),('time','float64'),('dummy6','int32'),\
	('dummy7','int32'),('dtm1','float64'),('grav','float64'),('dummy8','int32')])


	my_restart = np.fromfile(f,restart)

	if my_restart['dummy7'][0] == my_restart['dummy8'][0]:
		print('Reading correct')

	else:   
		print('Reading error')
		print(my_restart['dummy1'][0],my_restart['dummy2'][0])
		print(my_restart['dummy3'][0],my_restart['dummy4'][0])
		print(my_restart['dummy5'][0],my_restart['dummy6'][0])
		print(my_restart['dummy7'][0],my_restart['dummy8'][0])

	f.close()

	return my_restart




filename = './w_00135000.res' 
#filename = './tag3d.res'


my_restart = readres(filename)

i = my_restart['i'][0]
j = my_restart['j'][0]
k = my_restart['k'][0]
jp = my_restart['jp'][0]
my_raw_data = my_restart['my_raw_data'][0]


data = np.zeros((i,j,k))

for kk in range(0,k-1):

	data[:,:,kk]=np.reshape(my_raw_data[kk][1],(i,j),order='F')


nstep = my_restart['nstep'][0]
time  = my_restart['time'][0]
dt    = my_restart['dtm1'][0]
g     = my_restart['grav'][0]





print('i,j,k,jp=', i,j,k,jp)
print('dtm=',dt)
print('grav=', g)
print('size=',data.shape)
print('data=',data[1,2,5])
print('max_data=', np.nanmax(data))
print('min_data=', np.nanmin(data))
print('nstep=',nstep)


xedges = np.linspace(-6,20,k+1) 
yedges = np.linspace(0,15,i+1)

X,Y =np.meshgrid(xedges, yedges)



print('X=',X.shape)
#print('Xend=',X[452,961])
print('Y=',Y.shape)
#print('Yend=',Y[452,961])

data_slice = data[:,2,:]

print('data_slice=',data_slice.shape)
plt.pcolormesh(X,Y, data_slice)
plt.colorbar
plt.show()

