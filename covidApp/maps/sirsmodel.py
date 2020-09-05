import numpy as np
import matplotib.pyplot as plt
from scipy.integrate import odeint
from lmfit import minimize, Parameters, Parameter, report_fit

N =

# Defining system of equations
  def model f(y,t,params)
  S = y[0]
  I = y[1]

  try:
    k0 = params['k0'].value
  except keyError:
    k0 = params

    f1 = (.0109 * N) - (.007 * S) - (k0 * S * I)/N
    f2 = (k0 * S * I)/N - (.007 + .0819)*I - (.9181 * S)
return [f1,f2]

# Solving ODE with initial condition
def g(t, x0, param)
  x = odeint(f,xo,t, args=(params,))
return x

# Computing residual between actual and fitted
def residual(params, t, data)
  init = params['S0'].value, params['I0'].value
  model = g(t,init,params)
  I_model = model[:,1]
return (I_model - data).ravel()

# initial conditions
S0 = 1
I0 = 0
y0 = [S0,I0]

# insert data
time = # some array
I_measured = # some array

plt.figure()
plt.scatter(time, I_measured, marker='o', color='b', label='measured data', s=75)

# insert parameters
params = Parameters()
params.add('S0', value=S0, vary=False)
params.add('I0',value=I0, vary=False)
params.add('k0',value=1.02, min=.00001, max=10.)

# fit model
result = minimize(residual, params, args=(time, I_measured), method='leastsq')  # leastsq nelder
# check results of the fit
data_fitted = g(time, y0, result.params)

# plot fitted data
plt.plot(time, data_fitted[:, 1], '-', linewidth=2, color='red', label='fitted data')
plt.legend()
plt.xlim([0, max(time)])
plt.ylim([0, 1.1 * max(data_fitted[:, 1])])
# display fitted statistics
report_fit(result)

plt.show()
