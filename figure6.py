import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function
def f(x):
    return 1/x

# Values
x = np.linspace(1, 5, 400)
t = np.linspace(0, 2*np.pi, 100)
x, t = np.meshgrid(x, t)

# Calculate y and z for the solid of revolution
y = f(x) * np.cos(t)
z = f(x) * np.sin(t)

# Create a 3D plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, color='b', alpha=0.3)
ax.set_title("Solid of Revolution - Gabriel's Horn")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.show()
