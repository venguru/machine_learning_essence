import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm


x = np.linspace(-5, 5)
y = norm.pdf(x)
plt.plot(x, y, color="r")
plt.show()

