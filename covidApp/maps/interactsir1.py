import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate, optimize

xdata = np.linspace(0, 9, 10)
ydata = np.array([1,9,15,29,50,85,120,140,152,160])


ydata = np.array(ydata, dtype=float)
xdata = np.array(xdata, dtype=float)

def sir_model(y, x, beta, gamma):
    S = -beta * y[0] * y[1] / N + .011 - .007 * y[0]
    I = beta * y[0] * y[1] / N - .0889 * y[1] - gamma * y[1]
    R = -S - I
    return S, I, R

def fit_odeint(x, beta, gamma):
    return integrate.odeint(sir_model, (S0, I0, R0), x, args=(beta, gamma))[:,1]

def extrapolate(timepoint,popt,xdata, ydata):
    [beta,gamma] = popt
    if timepoint > len(xdata):
        I_outs = integrate.odeint(sir_model,(S0,I0,R0), xdata, args=(beta,gamma))[:,1]
        I1 = I_outs[len(I_outs)-1]
        R_outs = integrate.odeint(sir_model,(S0,I0,R0), xdata, args=(beta,gamma))[:,2]
        R1 = R_outs[len(R_outs)-1]
        S1 = N - I1 - R1
        for i in range(timepoint - len(xdata)):
            xdata = np.append(xdata,len(xdata))
            dI = beta * S1 * I1 / N - .0889 * I1 - gamma * I1
            newy = ydata[len(ydata)-1] + dI
            ydata = np.append(ydata,newy)
        predicted = ydata[len(ydata)-1]
        print("Predicted infected is " + str(predicted))
    else:
        known = ydata[timepoint-1]      
        print("Known number of infect was " + str(known))
    return

ninput = input("Input initial total population: ")
try:
  N = int(ninput)
  print("Accepted")
except ValueError:
  print("Please try again with a numeral input")

I0 = ydata[0]
S0 = N - I0


tinput = input("Input a timepoint at which you would like to predict the total infected population: ")
try:
  timepoint = int(tinput)
  print("Accepted. Calculating total infected population and adjusted infection rate... ")
except ValueError:
  print("Please try again with a numeral input")

R0 = 0.0

popt, pcov = optimize.curve_fit(fit_odeint, xdata, ydata)
fitted = fit_odeint(xdata, *popt)

extrapolate(timepoint, popt, xdata, ydata)

