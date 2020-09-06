import pylab as pp
import numpy as np
from scipy import integrate, interpolate
from scipy import optimize
from get_covid_data import read_data
import matplotlib.pyplot as plt

pops=np.array([265429,936692,445384,507078,92560,150972,799767,291408,
      676061,124714,369811,829685,621354,494228,
      601651,503310,62607,331164,140799,558067,105779])

print(pops)

cases,deaths=read_data() #both in alphabetical order

case_data=np.asarray(cases[1:,1:]) #remove dates and names *dates start at 3/24
case_data= case_data.astype(int) #convert to int
case_data=np.cumsum(case_data,axis=1) #convert to cumulative sum

death_data=np.asarray(deaths[1:,1:]) #remove dates and names *dates start at 3/24
death_data= death_data.astype(int) #convert to int
death_data=np.cumsum(death_data,axis=1) #convert to cumulative sum

time_range=np.arange(len(case_data[0]))
print(time_range)

##initialize the data
x_data = time_range
y_data = case_data[0]

def f(y, t, k): 
    """define the ODE system in terms of 
        dependent variable y,
        independent variable t, and
        optinal parmaeters, in this case a single variable k """
    return (0.0109*pops[0]-0.007*y[0]-k[0]*y[0]*y[1]/pops[0],
          k[0]*y[0]*y[1]/pops[0]-(0.007+0.0819))

def my_ls_func(x,teta):
    """definition of function for LS fit
        x gives evaluation points,
        teta is an array of parameters to be varied for fit"""
    # create an alias to f which passes the optional params    
    f2 = lambda y,t: f(y, t, teta)
    # calculate ode solution, retuen values for each entry of "x"
    r = integrate.odeint(f2,y0,x)
    #in this case, we only need one of the dependent variable values
    return r[:,1]

def f_resid(p):
    """ function to pass to optimize.leastsq
        The routine will square and sum the values returned by 
        this function""" 
    return y_data-my_ls_func(x_data,p)
#solve the system - the solution is in variable c
guess = [0.2,0.3] #initial guess for params
y0 = [1,0,0] #inital conditions for ODEs
(c,kvg) = optimize.leastsq(f_resid, guess) #get params

print("parameter values are ",c)

# fit ODE results to interpolating spline just for fun
xeval=np.linspace(min(x_data), max(x_data),30) 
gls = interpolate.UnivariateSpline(xeval, my_ls_func(xeval,c), k=3, s=0)

#pick a few more points for a very smooth curve, then plot 
#   data and curve fit
xeval=np.linspace(min(x_data), max(x_data),200)
#Plot of the data as red dots and fit as blue line
pp.plot(x_data, y_data,'.r',xeval,gls(xeval),'-b')
pp.xlabel('xlabel',{"fontsize":16})
pp.ylabel("ylabel",{"fontsize":16})
pp.legend(('data','fit'),loc=0)
pp.show()