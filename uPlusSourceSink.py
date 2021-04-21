import numpy as np
import matplotlib.pyplot as plt
from computeCirculation import COMPUTE_CIRCULATION

# Knowns
Vinf= 1
alpha= 0 
m= 1        # Source/Sink Strength
X0= 0       # Source/Sink X-coordinate origin
Y0= 0       # Source/Sink Y-coordinate origin

def degToRad(alpha):
    return alpha*(np.pi/180)

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

rad= degToRad(alpha)
for i in range (numX):
    for j in range (numY):
        x= XX[i,j]
        y= YY[i,j]
        dx= x-X0
        dy= y-Y0
        r= np.sqrt(dx**2+dy**2)

        Vx[i,j]= Vinf*np.cos(rad)+(m*dx)/(2*np.pi*r**2)
        Vy[i,j]= Vinf*np.sin(rad)+(m*dy)/(2*np.pi*r**2)

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
# Streamlines
numSL= 100
Xsl= -10*np.ones(numSL)
Ysl= np.linspace(-10,10,numSL)
XYsl= np.vstack((Xsl.T,Ysl.T)).T


# Quiver Plot
fig= plt.figure(1)
plt.cla()
plt.quiver(X,Y,Vx,Vy)
plt.streamplot(XX,YY,Vx,Vy, linewidth=0.5, density=10, color='r', arrowstyle='-', start_points=XYsl)
plt.plot(xC,yC,'b-')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.xlim([-2,2]);plt.ylim([-2,2])
plt.gca().set_aspect('equal')
plt.title('Uniform + Source/Sink Flow')
plt.show()