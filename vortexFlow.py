import numpy as np
import matplotlib.pyplot as plt
from computeCirculation import COMPUTE_CIRCULATION


# Known Variables
gamma= 2
X0= 0 
Y0= 0
theta= 0


# Calculations

# Grid
numX= 100
numY= 100
X= np.linspace(-10,10,numX)
Y= np.linspace(-10,10,numY)
XX,YY= np.meshgrid(X,Y)

# Solve for velocities
# Initialise varaibles
Vx= np.zeros([numX,numY])
Vy= np.zeros([numX,numY])
V= np.zeros([numX,numY])
Vt= np.zeros([numX,numY])
r= np.zeros([numX,numY])

for i in range(numX):
    for j in range(numY):
        x= XX[i,j]
        y= YY[i,j]
        dx= x-X0
        dy= y-Y0
        r= np.sqrt(dx**2+dy**2)

        Vx[i,j]= (gamma*dy)/(2*np.pi*r**2)
        Vy[i,j]= -(gamma*dx)/(2*np.pi*r**2)

        Vt[i,j]= -gamma/2*np.pi*r


# Circulation
a= 2
b= 2 
numT= 100
x0= 0
y0= 0
Gamma, xC, yC, VxC, VyC= COMPUTE_CIRCULATION(a,b,x0,y0,numT,Vx,Vy,X,Y)
print('Circulation: ',Gamma)


# Plot
fig= plt.figure(2)
plt.quiver(X,Y,Vx,Vy)
plt.plot(xC,yC,'-b')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Vortex Flow')
plt.xlim([-3, 3])                                                               # Set X-limits
plt.ylim([-3, 3])                                                               # Set Y-limits
plt.gca().set_aspect('equal') 
plt.show()
