import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from lmfit import minimize, Parameters, Parameter, report_fit
from decimal import Decimal

N = 1000

# Defining system of equations
def f(y,t,params):
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
def g(t, x0, param):
  x = odeint(f,x0,t, args=(params,))
  return x

# Computing residual between actual and fitted
def residual(params, t, data):
  init = params['S0'].value, params['I0'].value
  model = g(t,init,params)
  I_model = model[:,1]
  return (I_model - data).ravel()

def estimate(S0,I0,N,k0):
# initial conditions
  y0 = [S0,I0]

# insert data
  time = np.linspace(0, 9, 10)
  I_measured = np.array([1,9,15,29,50,85,120,140,152,160])

# insert parameters
  params = Parameters()
  params.add('S0', value=S0, vary=False)
  params.add('I0',value=I0, vary=False)
  params.add('k0',value=.4, min=.00001, max=10.)

# fit model
  result = minimize(residual, params, args=(time, I_measured), method='leastsq')  # leastsq nelder
# check results of the fit
  data_fitted = g(time, y0, result.params)
  estimated_infected = (timepoint, y0, result.params)
  print("There are " + estimated_infected[1,1] + " estimated infected")
  print("The infection rate is approximately " + k0 + " infections per infected")
  print("Statistical analysis of the model wll also be provided")
  # display fitted statistics
  return report_fit(result)



ninput = input("Input initial total population: ")
try:
  N = int(ninput)
  print("Accepted")
except ValueError:
  print("Please try again with a numeral input")

s0input = input("Input initial infected population: ")
try:
  I0 = int(s0input)
except ValueError:
  print("Please try again with a numeral input")
  
S0 = N - I0

k0input = input("What is your first guess for infection rate? (Usually a decimal from 0 to 10) ")
try:
  k0 = Decimal(k0input)
  print("Accepted")
except ValueError:
  print("Please try again with a numeral input")

tinput = input("Input a timepoint at which you would like to predict the total infected population: ")
try:
  timepoint = int(tinput)
  print("Accepted. Calculating total infected population and adjusted infection rate... ")
except ValueError:
  print("Please try again with a numeral input")

