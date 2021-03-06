# -*- coding: utf-8 -*-
"""
Created on Tue May  5 19:23:26 2020

MCMC chains plotted from the Supernova Cosmology Probe (SCP) 
using the linear Hubble relation. Data and emcee chains can be obtained from hubble.py

@author: Lani Chastain
"""


import numpy as np
import matplotlib.pyplot as plt


#For Plotting: 

chain = np.genfromtxt('hubble_chain.txt')
chain = chain.reshape(1,1000,500)

for c in chain:
    plt.plot(c)

plt.tight_layout()
plt.savefig('SCP_chains.pdf')
plt.xlabel('Step Number')
plt.show()

data = np.genfromtxt('SCPUnion2.1_mu_vs_z.txt')
redshift = data.T[1]
mm = data.T[2]
dm = data.T[3]
dlabel = 'SCP_2.1'
dpc = 10.**(mm/5.+1.)
dMpc = dpc / 10.**6


plt.plot(redshift, dMpc, '.')
plt.plot(redshift, 4900*redshift)
plt.show()

H0 = 3e5/4900
print(H0)
