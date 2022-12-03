import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt


def func(x, t, M, k, b, F):
    theta, omega = x
    # theta'(t) = omega
    dxdt = [omega, (F - b * omega - k * theta) / M]
    return dxdt


M, k, b, F = 1.0, 0.5, 0.2, 1.0
init_status = -1, 0.0
t = np.arange(0, 50, 0.02)
sol = integrate.odeint(func, init_status, t, args=(M, k, b, F))
plt.plot(t, sol[:, 0])
plt.plot(t, sol[:, 1])
plt.legend(["theta(t)", "omega(t)"])
plt.xlabel('t')
plt.grid()
plt.show()
