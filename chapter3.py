import numpy as np
import matplotlib.pyplot as plt


def step_function(x):
    return np.array(x>0, dtype=np.int)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.arange(-5.0, 5.0, 0.1)

fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

y1 = step_function(x)
y2 = sigmoid(x)

ax1.plot(x, y1)
ax2.plot(x, y2)

ax1.set_ylim(-0.1, 1.1)
ax2.set_ylim(-0.1, 1.1)

ax1.set_title("step")
ax2.set_title("sigmoid")

plt.show()