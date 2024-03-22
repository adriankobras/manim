import numpy as np
import matplotlib.pyplot as plt

def custom_function(x, a, b, c, d, e):
    return a * np.exp(-b * x**2) + c * np.exp(-d * (x - e)**2) + c * np.exp(-d * (x + e)**2)

# Define the parameters
a = 1.0
b = 0.2
c = 0.5
d = 0.1
e = 2.0

# Generate x-values
x = np.linspace(-10, 10, 500)

# Evaluate the function for the given x-values
y = custom_function(x, a, b, c, d, e)

# Plot the function
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Function Plot')
plt.grid(True)
plt.show()
