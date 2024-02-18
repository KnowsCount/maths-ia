import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function
def f(x):
    return 1/x

# Values
x = np.linspace(1, 5, 400)
y = f(x)

# Plot the function
plt.figure(figsize=(8, 6))
plt.plot(x, y)
plt.title("Function $f(x) = 1/x$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.show()

# Plot Gabriel's Horn
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
x = np.linspace(1, 5, 400)
t = np.linspace(0, 2*np.pi, 100)
x, t = np.meshgrid(x, t)
y = f(x) * np.cos(t)
z = f(x) * np.sin(t)
ax.plot_surface(x, y, z, color='b', alpha=0.3)
ax.set_title("Solid of Revolution - Gabriel's Horn")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.show()
