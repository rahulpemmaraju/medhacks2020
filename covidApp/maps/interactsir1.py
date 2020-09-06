import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate, optimize
from .get_covid_data import clean_data

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
        return predicted
    else:
        known = ydata[timepoint-1]      
        return known


def determine_cases(ys,populations):
  output=np.zeros((len(populations),181))
  ys = np.array(ys, dtype=float)
  x_data=np.arange(len(ys[0]))
  x_data = np.array(x_data, dtype=float)
  for i in range(len(ys)):
    global N
    N=populations[i]
    ydata=ys[i,:]
    global I0
    I0=ydata[0]
    global S0
    S0=N-I0
    global R0
    R0=0.0
    popt,pcov=optimize.curve_fit(fit_odeint,x_data,ydata)
    fitted = fit_odeint(x_data, *popt)
    for j in range(1,181):
      output[i][j-1]=extrapolate(j,popt,x_data,ydata)
  return output


pops,cases,deaths=clean_data()
output=determine_cases(cases,pops)
np.savetxt("cases.csv", output, delimiter=",")