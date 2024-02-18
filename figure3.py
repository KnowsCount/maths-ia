import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return 1/x

# Create x values
x = np.linspace(1, 5, 400)

# Create y values
y = f(x)

# Plot the function
plt.plot(x, y, label="y=1/x")

# Create the disks (represented as rectangles here)
num_disks = 10
x_disks = np.linspace(1, 5, num_disks+1)

for i in range(num_disks):
    # Create the rectangle (disk) parameters
    x_left = x_disks[i]
    x_right = x_disks[i+1]
    y_height = f(x_left)  # Use the left x value to calculate the y height
    width = x_right - x_left
    plt.gca().add_patch(plt.Rectangle((x_left, 0), width, y_height, fill=None, edgecolor='r', linewidth=1))

# Set the labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Method of Disks')

# Show the plot
plt.show()
