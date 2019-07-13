# READ GRID

import numpy as np

import matplotlib as ml
import matplotlib.pyplot as plt


def readgrid(filename):

	f = open(filename)

	nx = int(f.read(4))

	index,x=np.loadtxt(filename,skiprows=1,unpack=1)


#	return {'x':x, 'nx':nx ,'index':index }
  
	return  nx, index, x 




#nx,ind,x = readgrid('x1_grid.in')

nx,_,x = readgrid('x1_grid.in')

#nx,x = readgrid('x1_grid.in')


#print('n=',n[0])

print (x)

#print(2*nx)

#x=np.loadtxt('x1_grid.in',skiprows=1,usecols=range(n,2))



#print(x)
