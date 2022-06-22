import numpy as np
from matplotlib import pyplot
pi=np.pi
a0=-0.2
b0=0.2
c=a0+1j*b0
a=a0+np.sqrt(1-b0**2)
α=20
α=np.deg2rad(α)
r0=np.sqrt((a-a0)**2+b0**2)
Γ=4*pi*np.sin(α+np.arcsin(b0))
k=Γ/2/pi
zeta=lambda z:(z+a**2/z)*np.exp(-1j*α)
xy=np.arange(-5,5,0.01)
(x,y)=np.meshgrid(xy,xy)
z=x+1j*y+c
W=((z-c)*np.exp(-1j*α)+r0**2/(z-c)*np.exp(1j*α))+1j*k*np.log(z-c)
psi=W.imag
psi=np.where(np.abs(z-c)<=1,0,psi)
pyplot.contour(zeta(z).real,zeta(z).imag,psi,levels=np.arange(-5,5,0.2))
zz=np.exp(1j*np.linspace(0,2,100)*pi)+c
pyplot.plot(zeta(zz).real,zeta(zz).imag)
pyplot.xlim([-3,3])
pyplot.ylim([-3,3])
pyplot.show()