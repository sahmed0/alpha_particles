# -*- coding: utf-8 -*-

"""
Code to calculate the average ionisation energy for the range difference
and effective thicknesses from the experimental data.
bY Sajid 23/11/2023
"""


import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize_scalar
import matplotlib.pyplot as plt

# global variables
NUM_DENSITY = 2.5 * 10**25  # number density of stopping material
PROTON = 2.0  # proton / atomic number of material

SUB = 50    # number of sub-intervals for integration

# Define the function to be integrated
def bethe_block_formula(x, ION):
    func = 1 / ((3.801 * NUM_DENSITY * PROTON * ((np.log(x) + 6.307 - np.log(ION+10**-100))) * (10**-19)) / (x * 10**6))
    return func

# Define the integration limits
LOWER = 1560.99 / 1000  # lower limit of integration
UPPER = 4671.40 / 1000  # upper limit of integration

# Define a function that returns the chi-square value
target_integral = 135.19 / 1000

def chi_square(ION):
    integral_values, error = quad(bethe_block_formula, LOWER, UPPER, args=(ION,))
    return np.sum((integral_values - target_integral)**2/ target_integral)

# Find the optimal value of 'ION' using optimization
result = minimize_scalar(chi_square)
optimal_ION = result.x

print("Optimal value of 'ION':", optimal_ION)

# Store ION values and corresponding chi-square values
ION_values = np.linspace(1, 120, num=SUB)
chi_square_values = [chi_square(ION) for ION in ION_values]

# Plot the graph
plt.plot(ION_values, chi_square_values, label='Chi-square Values')

# Mark the optimal point
plt.scatter(optimal_ION, chi_square(optimal_ION), color='red', marker='o', label='Optimal Point')

# Labeling the axes and adding a legend
plt.xlabel('ION Value (eV)')
plt.ylabel('Chi-square Value')
plt.legend()

# Show the plot
plt.show()
