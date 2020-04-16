import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-5, 5, 300)
y = x**2

fig, ax = plt.subplots()
ax.plot(x, y, color="r")
plt.show()

