import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

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

# Create a colormap
cmap = cm.get_cmap("rainbow") # Rainbow colormap
norm = plt.Normalize(vmin=x.min(), vmax=x.max()) # Normalize the x values to [0,1]

# Plot surface with colormap
ax.plot_surface(x, y, z, rstride=1, cstride=1, facecolors=cmap(norm(x)), alpha=0.5, linewidth=0)

# Set titles and labels
ax.set_title("Gabriel's Horn - Painter's Paradox")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

# Show plot
plt.show()
