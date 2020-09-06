import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate, optimize

xdata = np.linspace(0, 9, 10)
ydata = np.array([.001,.009,.015,.029,.050,.085,.120,.140,.152,.160])


ydata = np.array(ydata, dtype=float)
xdata = np.array(xdata, dtype=float)

def sir_model(y, x, beta, gamma):
    S = -beta * y[0] * y[1] / N + .011 - .007 * y[0]
    I = beta * y[0] * y[1] / N - .0889 * y[1] - gamma * y[1]
    R = -S - I
    return S, I, R

def fit_odeint(x, beta, gamma):
    return integrate.odeint(sir_model, (S0, I0, R0), x, args=(beta, gamma))[:,1]

N = 1.0
I0 = ydata[0]
S0 = N - I0
R0 = 0.0

popt, pcov = optimize.curve_fit(fit_odeint, xdata, ydata)
fitted = fit_odeint(xdata, *popt)

plt.plot(xdata, ydata, 'o')
plt.plot(xdata, fitted)
plt.show()
