# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 15:03:08 2020

@author: Lani Chastain
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt(r"C:\Users\14238\Documents\05-COSMOLOGY\COSMOLOGY_INPUTS\lcparam_DES+LOWz.txt")

redshift = data[:,2]
app_mag = data[:,4] 
estimated_errors = data[:,5]

# DES data is in magnitudes so we must convert to distance modulus
log_dist = app_mag + 19.3

# log_dist is the "distance modulus"
# from this we can compute the distance is parsecs
dist_pc = 10.**(log_dist/5.+1.)
# distance is megaprsecs
dist_Mpc = dist_pc / 10**6
# error on that distance
dist_Merror = 10.**((log_dist+estimated_errors)/5.+1.-6.) - dist_Mpc

# the Hubble relation :  d = c*z/H0 , with H0 in km/s/Mpc
c = 3.e5   # speed of light in km/s
# more accurately, the Hubble relation is d = c*z*sqrt(z)/H0
# so let's estimate H0 from the data; but only for small zs in linear region:
indx = np.where(redshift < 0.05)
H0 = (c/dist_Mpc[indx]*redshift[indx]).mean()
#H0 = (c/dMpc*zs*np.sqrt(1+zs)).mean()
# make a string to print on the plot:
sH0 = 'H0 = '+str(round(H0))+' km/s/Mpc'


# we will draw curves to "predict" where the data points should lie.
# first, make a vector of redshifts with the numpy "arange" function.
dz = 0.001
zz = np.arange(dz,2.0,dz)
# the simplest (linear in z) Hubble relation curve:
ds1 = c/H0*zz
# a bit more accurate (and very similar to FRW with OmM = 0.43)
ds2 = c/H0*zz*np.sqrt(1.+zz)
# in terms of magnitudes rather than distance:
m1 = (np.log10(ds1)+5.)*5. 
m2 = (np.log10(ds2)+5.)*5. 


# compute the match between the data and the predictions,
# using the chisq-per-degree-of-freedom:
# get the predictions at the same redshifts as the data, by interpolating:
dp2 = np.interp(redshift,zz,ds2)
# compute the chisq per degree of freedom:
chisq2 = np.sum( ((dist_Mpc-dp2)/dist_Merror)**2 ) / dist_Mpc.size
print('chisq2, chisq3 = ',chisq2)


# draw a linear-linear plot with all the data and the two Hubble relation curves:
plt.figure()
plt.errorbar(redshift,dist_Mpc,xerr=dz,yerr=dist_Merror,fmt='+',label='supernova')
plt.plot(zz,ds1,'m',label="d = c/H0*z, linear")
plt.plot(zz,ds2,'g',label="d = c/H0*z*sqrt(1+z)")
#plt.xlim([0,1.5])
#plt.ylim([0,14000])
plt.xlabel('redshift z')
plt.ylabel('Luminosity distance (Mpc)')
plt.text(0.1,9000,sH0,fontsize = 12)
plt.grid(b=True,which='both')
plt.legend(loc='upper left')
plt.title('Hubble relations, data from Dark Energy Survey')
plt.show()


#plt.xlabel('z')
#plt.ylabel('log_d')
#plt.plot(redshift, log_dist, '.', ms=5, label = 'supernova', color = 'k')
#plt.legend()
#plt.show()

