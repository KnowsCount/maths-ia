import matplotlib.pyplot as plt
import numpy as np

# Create an array of x values from 1 to 10
x = np.linspace(1, 10, 400)

# Create a function for y
y = 1 / x

# Create the plot
plt.plot(x, y, label='y = 1/x')

# Set the title and labels
plt.title('Graph of the function y = 1/x for x >= 1')
plt.xlabel('x')
plt.ylabel('y')

# Add a legend
plt.legend()

# Show the plot
plt.show()
