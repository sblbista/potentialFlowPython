import numpy as np
import matplotlib.pyplot as plt
from computeCirculation import COMPUTE_CIRCULATION

# Knowns
m= -1        # Source/Sink Strength
X0= 0       # Source/Sink X-coordinate origin
Y0= 0       # Source/Sink Y-coordinate origin

# Calcluations

# Grid
numX= 100
numY= 100

X= np.linspace(-10,10, numX)
Y= np.linspace(-10,10,numY)
XX,YY= np.meshgrid(X,Y)

# Solve for Velocities

# Initialize the velocties
Vx= np.zeros([numX,numY])
Vy= np.zeros([numX,numY])
V= np.zeros([numX,numY])
Vr= np.zeros([numX,numY])
r= np.zeros([numX,numY])

for i in range (numX):
    for j in range (numY):
        x= XX[i,j]
        y= YY[i,j]
        dx= x-X0
        dy= y-Y0
        r= np.sqrt(dx**2+dy**2)

        Vx[i,j]= (m*dx)/(2*np.pi*r**2)
        Vy[i,j]= (m*dy)/(2*np.pi*r**2)

        V[i,j]= np.sqrt(Vx[i,j]**2+Vy[i,j]**2)
        Vr= m/2*np.pi*r

# Compute Circulation
a= 1.5
b= 1.5
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
plt.xlim([-2,2]);plt.ylim([-2,2])
plt.gca().set_aspect('equal')
plt.title('Source/Sink Flow')
plt.show()