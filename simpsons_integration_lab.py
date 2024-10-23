# -*- coding: utf-8 -*-

"""
This is a program to evaluate a numerical integration
using Simpson's Rule and conduct the Chi-square minimisation
To find the ION value for the materials using our observed data
In the Alpha particle energy loss in matter
Year 3 Physics Lab experiment
by Sajid Ahmed
on 18-10-2023.
"""

import numpy as np
from scipy.integrate import simpson

# Global constants
NUM_DENSITY = 2.5*10**25  # number density of material
PROTON = 18.0      # atomic / proton number of material

SUB = 2   # number of sub intervals for integration

ION = np.linspace(180, 220, SUB)
ION_LOGS = [np.log(i) for i in ION]

# Define a function that returns the absolute difference between the integral and the target value (1)
target_thickness = 9.93/1000

# Define the integration limits
LOW = 3684.223076/1000    # lower limit of integration
UP = 4671.4/1000     # upper limit of integration

# Define the subinterval points
x = np.linspace(LOW, UP, SUB)

# Define the bethe bloch formula
def bethe_bloch_integral():
    """ Define the bethe bloch formula and integrate it """
    for ion in ION_LOGS:
        integral = [simpson(1/(3.801 * NUM_DENSITY * PROTON * (np.log(x) + 6.307 - ion)
                  * (10**-19)) / (x * 10**6), x)]
    return integral

# Use Simpson's rule for numerical integration
# def range_diff():
#     """ Use Simpson's rule for numerical integration to calculate the range difference """
#     for i in y:
#         integral = simpson(y, x)
#     return integral

range_difference = bethe_bloch_integral()

# def chi2():
#     """ function to find the chi squared value of range difference, for each value of ION """
#     chi = np.sum((range_difference - target_thickness)**2/target_thickness)
#     return chi

# chi_value = chi2()

print(ION_LOGS)
print(range_difference)
# print(chi_value)
