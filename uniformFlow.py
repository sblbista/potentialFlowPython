import numpy as np
import matplotlib.pyplot as plt
from computeCirculation import COMPUTE_CIRCULATION

# Known values
Vinf= 1
alpha= 0

# Calcuations
# Grid
numX= 10
numY= 10
X= np.linspace(-10,10,numX)
Y= np.linspace(-10,10,numY)

XX, YY= np.meshgrid(X,Y)

# Solve for Velocities
Vx= np.zeros([numX,numY])
Vy= np.zeros([numX,numY])

for i in range (numX):
    for j in range (numY):
        Vx[i,j]= Vinf*np.cos(alpha*(np.pi/180))
        Vy[i,j]= Vinf*np.sin(alpha*(np.pi/180))

# Compute Circulation
a= 5
b= 5
x0= 0
y0= 0
numT= 100

Gamma, xC, yC, VxC, VyC= COMPUTE_CIRCULATION(a,b,x0,y0,numT,Vx,Vy,X,Y)
print('Circulation: ', Gamma)

# Plotting

# Quiver Plot
fig= plt.figure(1)
plt.cla()
plt.quiver(X,Y,Vx,Vy)
plt.plot(xC,yC,'b-')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.gca().set_aspect('equal')
plt.show()