import numpy as np

import matplotlib as ml
import matplotlib.pyplot as plt



from pyvtk import *


def readpln(filename):

	f = open(filename,'rb')

	header = np.dtype([('dummy1','int32'),('nstep','int32'),\
	('time','float64'),('dt','float64'),('g','float64'),\
	('dens_0','float64'),('Re','float64'),('Pr','float64'),\
	('dummy2','int32'),('dummy3','int32'),('norm','int32'),\
	('index','int32'),('iu','int32'),('iv','int32'),('iw','int32'),\
	('dummy4','int32'),('dummy5','int32'),('cloc','float64'),\
	('eloc','float64'),('dummy6','int32'),('dummy7','int32'),\
	('np1','int32'),('np2','int32'),\
	('dummy8','int32'),('dummy9','int32')])


	my_header = np.fromfile(f,header)

	np1 = my_header['np1'][0]
	np2 = my_header['np2'][0]

	f.close()

	f= open(filename,'rb')

	plane = np.dtype([('dummy1','int32'),('nstep','int32'),\
	('time','float64'),('dt','float64'),('g','float64'),\
	('dens_0','float64'),('Re','float64'),('Pr','float64'),\
	('dummy2','int32'),('dummy3','int32'),('norm','int32'),\
	('index','int32'),('iu','int32'),('iv','int32'),('iw','int32'),\
	('dummy4','int32'),('dummy5','int32'),('cloc','float64'),\
	('eloc','float64'),('dummy6','int32'),('dummy7','int32'),\
	('np1','int32'),('np2','int32'),\
	('dummy8','int32'),('dummy9','int32'),\
	('gc1','float64',np1),('ge1','float64',np1),\
	('dummy10','int32'),('dummy11','int32'),\
        ('gc2','float64',np2),('ge2','float64',np2),\
        ('dummy12','int32'),('dummy13','int32'),\
	('data','float32',np1*np2),('dummy14','int32')])


	my_plane = np.fromfile(f,plane)
 
	if my_plane['dummy13'][0] == my_plane['dummy14'][0]:
		print('Reading correct')
	else:
		print('Reading error')
		print(my_plane['dummy1'][0],my_plane['dummy2'][0],my_plane['dummy3'][0])
		print(my_plane['dummy4'][0],my_plane['dummy5'][0],my_plane['dummy6'][0])
		print(my_plane['dummy7'][0],my_plane['dummy8'][0],my_plane['dummy9'][0])
		print(my_plane['dummy10'][0],my_plane['dummy11'][0],my_plane['dummy12'][0])
		print(my_plane['dummy13'][0],my_plane['dummy14'][0])

	f.close()

	return my_plane



#filename = './WS_j0065_n00000001.pln'
filename  = './U0_j0033_n00048500.pln'

#filename = './W0_j0065_n00125500.pln' 
#filename = './dens_j0098_n00008900.pln'
#filename = './U0_k0791_n00092107.pln'
#filename = './W0_k0148_n00000010.pln'

my_plane = readpln(filename)

#header
nstep = my_plane['nstep'][0];    time = my_plane['time'][0]
dt    = my_plane['dt'][0];       g    = my_plane['g'][0]
dens_0 = my_plane['dens_0'][0];  Re   = my_plane['Re'][0]
Pr = my_plane['Pr'][0];          norm = my_plane['norm'][0]
index = my_plane['index'][0];    iu   = my_plane['iu'][0]
iv = my_plane['iv'][0];          iw   = my_plane['iw'][0]
cloc = my_plane['cloc'][0];      eloc = my_plane['eloc'][0]
np1 = my_plane['np1'][0];        np2  = my_plane['np2'][0]

#grid
gc1 = my_plane['gc1'][0];        ge1 = my_plane['ge1'][0]
gc2 = my_plane['gc2'][0];        ge2 = my_plane['ge2'][0]

#data
raw_data = my_plane['data'][0];
data = np.reshape(raw_data,(np1,np2),order='F')


print('nstep =',nstep)
print('dt=',dt)
print('time =',time)
print('Re =', Re)
print('Pr =', Pr)
print('norm = ',norm)
print('index =',index)
print('iu=',iu)
print('iv=',iv)
print('iw=',iw)
print('cloc =',cloc)
print('eloc =',eloc)
print('np1 =',np1)
print('np2 =',np2)
print('x1c =',gc1[0],gc1[1],gc1[-2],gc1[-1])
print('x2c=',gc2[0],gc2[1],gc2[-2],gc2[-1])
print('x1e =',ge1[0],ge1[1],ge1[-2],ge1[-1])
print('x2e=',ge2[0],ge2[1],ge2[-2],ge2[-1])
print('raw data length =',len(raw_data))

print('data length =',data.shape)


#yedges = gc2[1:]
#xedges = gc1[1:-1]
#data_ng = data[1:-1,1:] 


yedges = gc1
xedges = gc2
data_ng = data


print('xedges,yedges,data_ng length =',xedges.shape,yedges.shape,data_ng.shape)


print('data_ng[153,101]',data_ng[148,129])

X,Y =np.meshgrid(xedges, yedges)

#plt.subplot(111,projection='polar')


plt.pcolormesh(X, Y, data_ng)
plt.colorbar()
plt.show()














#if norm == 1:
#	vtk = VtkData(RectilinearGrid(1,gc1,gc2),PointData(Scalars(data,name="test")))
#	vtk.tofile('test.vtk','binary')
#
#elif norm == 2:
#
#	vtk = VtkData(RectilinearGrid(gc1,1,gc2),PointData(Scalars(data,name="test")))
#	vtk.tofile('test.vtk','binary')
#
#elif norm == 3:
#
#	vtk = VtkData(RectilinearGrid(gc1,gc2,1),PointData(Scalars(data,name="test")))
#	vtk.tofile('test.vtk','binary')
