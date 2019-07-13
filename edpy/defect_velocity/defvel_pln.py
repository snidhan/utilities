import numpy as np
import matplotlib as ml
import matplotlib.pyplot as plt

from ioeddy import readgrid
from ioeddy import readres
from ioeddy import center
from ioeddy import readpln

# ...... inputs .......

##Unstratified

path         = '/work/planes_FINF/' 
file_start   = 40000
file_end     = 46300
title = 'defvel_cl_02_40000_46300.dat'

##Stratified

#path         = '/home/jose/Desktop/restart_strat/' 
#file_start   = 38000
#file_end     = 38100
#title = 'defvel_F3.dat'


stride       = 100
file_header  = 'W0_j0002_n'




# ...... .......

nit  =  int((file_end-file_start)/stride + 1)
time_all =  np.zeros(nit)

print('nit=',nit)



for it in range(0,nit):


	print('it=',it)

	file_number =  file_start + it*stride 
	file_name   =  path + file_header + '%08d'%file_number + '.pln' 

          
	print('Reading file:', file_name)
	my_plane = readpln(file_name)

	time   = my_plane['time'][0]
	i  = my_plane['np1'][0]  #vertical
	k  = my_plane['np2'][0]  #horizontal
	xc = my_plane['gc2'][0]; #horizontal grid


        #data
	raw_data = my_plane['data'][0];
	data = np.reshape(raw_data,(i,k),order='F')

         
	if it==0:
		defvel_all = np.zeros((k,nit)); defvel_all_mean = np.zeros((k,nit-1)); defvel_mean = np.zeros(k);
 
		defvel_cl_all = np.zeros((k,nit)); defvel_cl_all_mean = np.zeros((k,nit-1)); defvel_cl_mean = np.zeros(k); 
		time_start = my_plane['time'][0]

	if it==nit-1:
		time_end  = my_plane['time'][0]
		time_span = time_end - time_start 

	# ...... defect velocity ......


	defvel = np.zeros(k)
	defvel_cl = np.zeros(k)

	for kk in range(0,k):

		defvel[kk] = 1-np.mean(data[1:i,kk])
		defvel_cl[kk] = 1 - data[2,kk]     
 
	defvel_all[:,it] = defvel
	defvel_cl_all[:,it] = defvel_cl     
 
	time_all[it] = time
  

## ...... time averaging ......

time_diff = np.diff(time_all)

#print(it)

for it in range(1,nit):

	defvel_all_mean[:,it-1]= 0.5*(defvel_all[:,it-1]+defvel_all[:,it])
	defvel_cl_all_mean[:,it-1]= 0.5*(defvel_cl_all[:,it-1]+defvel_cl_all[:,it])

defvel_mean= np.average(defvel_all_mean,1,time_diff)

defvel_cl_mean= np.average(defvel_cl_all_mean,1,time_diff)


## ...... saving ......
#
export = np.array([xc, defvel_cl_mean]).T
np.savetxt(title,export)


print('T0=',time_all[0],'Tend=',time_all[-1])




fig=plt.loglog(xc[2547:-1],defvel_cl_mean[2547:-1],xc[2547:-1],xc[2547:-1]**(-1.4))
#fig=plt.loglog(xc[2547:-1],defvel_mean[2547:-1],xc[2547:-1],xc[2547:-1]**(-1),xc[2547:-1],xc[2547:-1]**(-2/3))
#plt.axis([0.01,100,0.01,1])
#
plt.xlabel('x/D')
plt.title('Centerline defect velocity.  Spheroid Re=$10^4$ Fr=INF')
#
plt.setp(fig[0], color='tab:red', linewidth=2.0,label='Ud')
plt.setp(fig[1], color='tab:blue', linewidth=2.0,label='x^{-1}')
#plt.setp(fig[2], color='tab:red',linewidth=1.0, linestyle='dashed',label='x^{-2/3}')
#
#
plt.legend()
plt.show()



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


