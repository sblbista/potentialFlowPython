import numpy as np
import matplotlib.pyplot as plt
from computeCirculation import COMPUTE_CIRCULATION


# Known Variables
gamma= 10
X0= 0 
Y0= 0
theta= 0
Vinf= 1
alpha= 0

def degToRad(alpha):
    return alpha*(np.pi/180)


rad= degToRad(alpha)
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

        Vx[i,j]= Vinf*np.cos(rad)+(gamma*dy)/(2*np.pi*r**2)
        Vy[i,j]= Vinf*np.sin(rad)+(-gamma*dx)/(2*np.pi*r**2)

        Vt[i,j]= -gamma/2*np.pi*r


# Circulation 1
a= 5
b= 5 
numT= 100
x0= 0
y0= 0
Gamma1, xC1, yC1, VxC1, VyC1= COMPUTE_CIRCULATION(a,b,x0,y0,numT,Vx,Vy,X,Y)
print('Circulation: ',Gamma1)

# Circulation 2
a= 1.5
b= 1.5 
numT= 100
x0= 0
y0= 3
Gamma2, xC2, yC2, VxC2, VyC2= COMPUTE_CIRCULATION(a,b,x0,y0,numT,Vx,Vy,X,Y)
print('Circulation: ',Gamma2)




# Plot


# Streamlines
numSL= 20
Xsl= -10*np.ones(numSL)
Ysl= np.linspace(-10,10,numSL)
XYsl= np.vstack((Xsl.T,Ysl.T)).T

fig= plt.figure(2)
plt.quiver(X,Y,Vx,Vy)
plt.streamplot(XX,YY,Vx,Vy,density=10, linewidth=0.5, start_points=XYsl, color='r')
plt.plot(xC1,yC1,'-b')
plt.plot(xC2,yC2,'g-')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Vortex Flow')
plt.xlim([-6, 6])                                                               # Set X-limits
plt.ylim([-6, 6])                                                               # Set Y-limits
plt.gca().set_aspect('equal') 
plt.show()
