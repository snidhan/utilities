import numpy as np

from pyvtk import *

def readres(filename):

	f = open(filename,'rb')

	header = np.dtype([('dummy1','int32'),('i','int32'),\
	('j','int32'),('k','int32'),('jp','int32'),\
	('dummy8','int32'),('dummy9','int32')])


	my_header = np.fromfile(f,header)

	i = my_header['i'][0]
	j = my_header['j'][0]
	k = my_header['k'][0]


	f.close()

	f= open(filename,'rb')

	restart = np.dtype([('dummy1','int32'),('i','int32'),\
	('j','int32'),('k','int32'),('jp','int32'),\
	('dummy2','int32'),('dummy3','int32'),\
	('data','float32',i*j*k),\
	('dummy4','int32'),('dummy5','int32'),('nstep','float64'),\
	('time','float64'),('dummy6','int32'),('dummy7','int32'),\
	('dtm1','float64'),('grav','float64'),('dummy8','int32')])


	my_restart = np.fromfile(f,restart)
 
#	if my_restart['dummy1'] == my_restart['dummy8']:
#		print('Reading correct')
#	else:
#		print('Reading error')
#

	return my_restart

filename = './w_00135000.res' 

my_restart = readres(filename)


#header
i = my_restart['i'][0] 
j = my_restart['j'][0] 
k = my_restart['k'][0] 
data = my_restart['data'][0];

x1 = np.linspace(0,15,451)
x2 = np.linspace(0,2*np.pi,65)
x3 = np.linspace(-6,20,961)


n = -1;

points=np.zeros([i*j*k,3]) 


for kk in range(0,k-1):
	for jj in range(0,j-1):
		for ii in range(0,i-1):

			n = n + 1
			points[n]=[ x1[ii]*np.cos(x2[jj]), x1[ii]*np.sin(x2[jj]), x3[kk]]
	
  
#			x1_cart[i] = x1[i]*np.cos(x2[j])
#			x2_cart[j] = x1[i]*np.sin(x2[j])
#			x3_cart[k] = x3[k]



print('i =',i)
print('j =',j)
print('k =',k)
print('shape=',points.shape)
print('data length =',len(data))
print('data[20000]=',data[20000])
#
#
#if norm == 1:


#vtk = VtkData(UnstructuredGrid(x1_cart,x2_cart,x3_cart),PointData(Scalars(data,name="restart"))
#vtk.tofile('restart.vtk','binary')

vtk = VtkData(UnstructuredGrid(points),PointData(Scalars(data,name="restart")))
vtk.tofile('restart.vtk','binary')



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
