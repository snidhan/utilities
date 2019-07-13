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


def readgrid(filename):

	f = open(filename)

	nx = int(f.read(4))

	index,x=np.loadtxt(filename,skiprows=1,unpack=1)
  
	return nx,index,x


def center(var,data,i,j,k):

# Center velocity
	if var == 'u':

		for ii in range(1,i-2): #ii 2 to i-1
			for jj in range(1,j-2):
				for kk in range (1,k-2):
	    
					data[ii,jj,kk] = 0.5 * (data[ii,jj,kk] + data[ii-1,jj,kk])	
	if var == 'v':

		for ii in range(1,i-2): #ii 2 to i-1
			for jj in range(1,j-2):
				for kk in range (1,k-2):
	    
					data[ii,jj,kk] = 0.5 * (data[ii,jj,kk] + data[ii,jj-1,kk])	
		


	if var == 'w':

		for ii in range(1,i-2): #ii 2 to i-1
			for jj in range(1,j-2):
				for kk in range (1,k-2):
	    
					data[ii,jj,kk] = 0.5 * (data[ii,jj,kk] + data[ii,jj,kk-1])	
			

	return data






##############################################################################################


filename = './w_00135000.res' 
var = 'w'

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


#################################################################################################

# SLICE

print('i,j,k,jp=', i,j,k,jp)
print('dtm=',dt)
print('grav=', g)
print('size=',data.shape)
print('data=',data[1,2,5])
print('max_data=', np.nanmax(data))
print('min_data=', np.nanmin(data))
print('nstep=',nstep)


# GRID

nx,_,x   =  readgrid('x3_grid.in')
nr,_,r   =  readgrid('x1_grid.in')
nth,_,th =  readgrid('x2_grid.in')

# Streamwise
xe = np.zeros(nx+1)
xc = np.zeros(nx+1)

xe[:len(x)]=x[:]; xe[-1]=xe[-2] + (xe[-2]-xe[-3]); #only required for consistency of the allocation

for ii in range(1, nx+1):

	xc[ii] = (xe[ii] + xe[ii-1]) * 0.5

xc[0] = xe[0] - (xc[1]-xe[0])

# Radial
re = np.zeros(nr+1)
rc = np.zeros(nr+1)

re[:len(r)]=r[:]; re[-1]=re[-2] + (re[-2]-re[-3]); #only required for consistency of the allocation

for ii in range(1, nr+1):

	rc[ii] = (re[ii] + re[ii-1]) * 0.5

rc[0] = re[0] - (rc[1]-re[0])

# Azimuthal 
the = np.zeros(nth+1)
thc = np.zeros(nth+1)

the[:len(th)]=th[:]; the[-1]=the[-2] + (the[-2]-the[-3]); #only required for consistency of the allocation

for ii in range(1, nth+1):

	thc[ii] = (the[ii] + the[ii-1]) * 0.5

thc[0] = the[0] - (thc[1]-the[0])



    # Change of coordinates 

#for ii in range(0,nth)

#X(ii,jj) = 



data = center(var,data,i,j,k)


# PLOT

print('xe=',xe.shape)
print('rc=',rc.shape)

#xedges = np.linspace(-6,20,k) 
#yedges = np.linspace(0,15,i)


#print (xe)
#print (xedges)
#print('xedges=',xedges.shape)


xedges = thc[1:]
yedges = rc[1:-1]
X,Y =np.meshgrid(xedges, yedges)


print('X=',X.shape)
#print('Xend=',X[452,961])
print('Y=',Y.shape)
#print('Yend=',Y[452,961])


data_ng = data[1:-1,1:,1:-1]
data_slice = data_ng[:,:,361]


#print(X[125,32],Y[125,32],data_slice[125,32])

#print('thc[0],thc[1],thc[64],thc[65])',thc[0],thc[1],thc[64],thc[65])
#print('the[0],the[1],the[64],the[65])',the[0],the[1],the[64],the[65])
#
#print('X[125,65],Y[125,65],data_slice[125,65]',X[125,65],Y[125,65],data_slice[125,65])
#
#print('X[125,64],Y[125,64],data_slice[125,64]',X[125,64],Y[125,64],data_slice[125,64])
#
#print('X[125,0],Y[125,0],data_slice[125,0]',X[125,0],Y[125,0],data_slice[125,0])
#
#print('X[125,1],Y[125,1],data_slice[125,1]',X[125,1],Y[125,1],data_slice[125,1])
#
#



print('data_slice=',data_slice.shape)
#plt.pcolormesh(X,Y, data_slice)
#plt.colorbar
#plt.show()
plt.subplot(111,projection='polar')

#fig=plt.figure()
#ax=fig.add_subplot(111, projection='polar')
#ax.
plt.pcolormesh(X, Y, data_slice)
plt.colorbar()
plt.show()









