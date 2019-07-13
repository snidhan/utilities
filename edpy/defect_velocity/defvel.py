import numpy as np
import matplotlib as ml
import matplotlib.pyplot as plt

from ioeddy import readgrid
from ioeddy import readres
from ioeddy import center

# ...... inputs .......

##Unstratified

path         = '/home/jose/Desktop/restart_unstrat/' 
file_start   = 30000
file_end     = 31300
title = 'defvel_FINF.dat'

##Stratified

#path         = '/home/jose/Desktop/restart_strat/' 
#file_start   = 38000
#file_end     = 38100
#title = 'defvel_F3.dat'


stride       = 100
file_header  = 'w_000'



nx,_,_,xe,xc = readgrid(path + 'x3_grid.in')
ny,_,_,ye,yc = readgrid(path + 'x1_grid.in')

# ...... .......

nit  =  int((file_end-file_start)/stride + 1)
var  =  file_header[0]
time_all =  np.zeros(nit)

print('nit=',nit)



for it in range(0,nit):


	print('it=',it)

	file_number =  file_start + it*stride 
	file_name   =  path + file_header + '%0*d'%(0,file_number) + '.res' 

          
	print('Reading file:', file_name)
	my_restart,data = readres(file_name)


	i    = my_restart['i'][0]
	j    = my_restart['j'][0]
	k    = my_restart['k'][0]
	time   = my_restart['time'][0]
         
	if it==0:
		defvel_all = np.zeros((k,nit)); defvel_all_mean = np.zeros((k,nit-1)); defvel_mean = np.zeros(k); 
		time_start = my_restart['time'][0]

	if it==nit-1:
		time_end  = my_restart['time'][0]
		time_span = time_end - time_start 

	# ...... defect velocity ......

	data_c = center(var,data,i,j,k)

	defvel = np.zeros(k)


	for kk in range(0,k):

		defvel[kk] = 1-np.mean(data[1:i-4,:,kk])
	      
	defvel_all[:,it] = defvel
       
	time_all[it] = time
  

# ...... time averaging ......

time_diff = np.diff(time_all)

print(it)

for it in range(1,nit):

	defvel_all_mean[:,it-1]= 0.5*(defvel_all[:,it-1]+defvel_all[:,it])


defvel_mean= np.average(defvel_all_mean,1,time_diff)



# ...... saving ......

export = np.array([xc, defvel_mean]).T
np.savetxt(title,export)









#fig=plt.loglog(xc,defvel_mean,xc,xc**(-1),xc,xc**(-2/3))
#plt.axis([0.01,100,0.01,1])
#
#plt.xlabel('x/D')
#plt.title('Defect velocity.  Spheroid Re=$10^4$ Fr=3')
#
#plt.setp(fig[0], color='tab:red', linewidth=2.0,label='Ud')
#plt.setp(fig[1], color='tab:blue', linewidth=2.0,label='x^{-1}')
#plt.setp(fig[2], color='tab:red',linewidth=1.0, linestyle='dashed',label='x^{-2/3}')
#
#
#plt.legend()
#plt.show()



# ------------------------------------------------------------------------------------------------


# ......  SLICE PLOT ......

#	if   var == 'u':
#		ycr = yc[::-1]						 # reverse the yc coordinates
#		X,Y =np.meshgrid(xc,[-yer,ye])                           # generate a mesh to plot 
#
#	elif var == 'v' or var == 'd':
#		ycr = yc[::-1]                                            
#		X,Y =np.meshgrid(xc,[-ycr,yc])                              
#
#	elif var == 'w':
#		ycr = yc[::-1]                                           
#		X,Y =np.meshgrid(xe,[-ycr,yc])                               
#
#
#	data_slice_u   = data[:,9,:]                             # extract the upper and lower halfs     
#	data_slice_l   = np.flipud(data[:,26,:]) 
#
#	data_slice = np.vstack((data_slice_l,data_slice_u))      # combine the two halfs
#
#	plt.axes().set_aspect('equal', 'datalim')
#
#	plt.figure(it)
#	plt.pcolormesh(X,Y, data_slice)
#	plt.colorbar
#	plt.show()


