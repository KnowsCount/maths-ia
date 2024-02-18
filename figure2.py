import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create an array of x values from 1 to 10
x = np.linspace(1, 10, 400)

# Create a function for y
y = 1 / x

# Create theta values for rotation
theta = np.linspace(0, 2.*np.pi, 400)

# Convert x, y, and theta to 2D arrays
t, x = np.meshgrid(theta, x)
_, y = np.meshgrid(theta, y)

# Convert to cylindrical coordinates
# r is the distance from the origin to the point (x, y)
# theta is the angle from the positive x-axis
# z is the height above the x-y plane
r = y
x = r * np.cos(t)
z = r * np.sin(t)

# Create the figure and an Axes3D object
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_surface(x, z, y, color='b', alpha=0.6)

# Set the title
ax.set_title("Gabriel's Horn")

# Show the plot
plt.show()
