#!/usr/bin/python

#chaotic pendulum problem
#plots phase space

# variables
# w  : angular frequency
# th : angle
# ph : driven angle
# wd : driven angular frequency
# q  : damping factor
# g  : driven force amplitude


from numpy import sin,cos,pi
import matplotlib 
matplotlib.use("gtk3cairo")
import matplotlib.pyplot as plt

# dw/dt
def fw (t,w,th,ph,q,g,wd) :
  return -w/q-sin(th)+g*cos(ph)

# dth/dt
def fth (t,w,th,ph,q,g,wd) :
  return w

# dph/dt  
def fph (t,w,th,ph,q,g,wd) :
  return wd

# just runge-kutta for this problem  
def solve (init) :
  f = (fw,fth,fph)
  dt = 0.01
  t = 0
  i = 0
  
  res = ([init[0]],[init[1]],[init[2]],init[3],init[4],init[5])
  
  while (i < 5000) :
    j = 0
    while (j < 3) :
      k1 = dt * f[j](t,res[0][i],res[1][i],res[2][i],init[3],init[4],init[5])
      k2 = dt * f[j](t+dt/2,res[0][i]+k1/2,res[1][i]+k1/2,res[2][i]+k1/2,init[3],init[4],init[5])
      k3 = dt * f[j](t+dt/2,res[0][i]+k2/2,res[1][i]+k2/2,res[2][i]+k1/2,init[3],init[4],init[5])
      k4 = dt * f[j](t+dt,res[0][i]+k3,res[1][i]+k3,res[2][i]+k1/2,init[3],init[4],init[5])
      res[j].append(res[j][i] + 1./6. * (k1 + 2*k2 + 2*k3 + k4))
      j = j + 1
    i = i + 1  
    t = t + dt
  
  plt.plot(res[0],res[1])
  plt.show()
