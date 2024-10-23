# -*- coding: utf-8 -*-

"""
CODE TO FIND THE AVERAGE IONISATION ENERGY
FOR ALPHA PARTICLES ENERGY LOSS IN MATTER EXPERIMENT
BY SAJID IN COLLABORATION WITH MONTY.
NOV 16 2023
"""

# Call libraries/functions
import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

# Global Variables
NUM = 2.5*10**25  # number density
ATOMIC = 2.0  # atomic number
LOWER = 4671.4/1000  # initial energy MeV, lower limit of integration

# file containing data, DATA IN FILE MUST HAVE SAME UNITS AS BETHE-BLOCH EQUATION
file_path = "Data_For_Fit.csv"


# Function to read data from above file, splits into the 3 lists for each column
def read_data(file_path):
    data = np.loadtxt(file_path, delimiter=',', skiprows = 1, encoding='utf-8')
    E_values = data[:, 0]       # energy values
    observed_values = data[:, 1]    # effective thickness values
    observed_uncertainties = data[:, 2]     # uncertainties on effective thickness
    return E_values, observed_values, observed_uncertainties


# Bethe-Bloch equation, ie. the function to integrate to find range difference
def inverse_bethe_bloch(E, I):
    """ E represents the energy, I represents average ionisation energy """
    return -1 / ((3.801 * NUM * ATOMIC * (np.log(E) + 6.307 - np.log(I)) * 10**-19) / (E * 10**6))

# Chi-squared function with numerical integration
def chi_squared(I, E_values, observed_values, lower_limit, observed_uncertainties):
        expected_values = 1 * \
            np.array([quad(inverse_bethe_bloch, lower_limit, E, args=(I,))[0]
                     for E in E_values])  # integrates the function using scipy quad
        VAR = (observed_uncertainties)**2 # VARIANCE
        DOF = len(observed_values)  # number of degrees of freedom
        return (np.sum(((observed_values - expected_values)**2)/VAR))    # returns the chi²


# Read data from the file
E_values, observed_values, observed_uncertainties = read_data(file_path)

# minimises the chi² and extracts the optimal value for average ionisation energy
chi_min = 10000  # chi² reference value, any large number
chi_squared_values = []     # empty list to append values to later
I_values = np.linspace(20, 60, 3000)    # list of average ionisation energy values
for I_test in I_values:
    chi = chi_squared(I_test, E_values, observed_values,
                      LOWER, observed_uncertainties)
    chi_squared_values.append(chi)      # # chi² calculated and appended to list

    if chi < chi_min: 
        chi_min = chi   # minimises the value of chi² by comparing to reference value
        I_opt = I_test


min_index = np.argmin(chi_squared_values)
I_opt = I_values[min_index]     # gives optimal I value corresponding to minimum chi²
min_chi_squared = chi_squared_values[min_index]     # gives minimum chi²

# prints the values of optimal I and the corresponding chi²
print("The optimum Average Ionisation Energy from chi² minimisation is",
      I_opt, "with chi² value", chi_min)


# To calculate the errors for Average Ionisation energy using Minimum Chi² + 1 confidence interval
# appends values to intersection list that are within minimum chi² + 1 of the value of chi²
intersection_indices = []
for i in range(1, len(chi_squared_values) - 1):
    if (chi_squared_values[i] > min_chi_squared + 1 and chi_squared_values[i - 1] <= min_chi_squared + 1) or \
       (chi_squared_values[i] > min_chi_squared + 1 and chi_squared_values[i + 1] <= min_chi_squared + 1):
        intersection_indices.append(i)

# Get the I values at the intersection points
intersection_I_values = [I_values[i] for i in intersection_indices]
intersection_chi_squared_values = [chi_squared_values[i] for i in intersection_indices]

# PLOTTING THE GRAPHS
# plots ION values about the optimal with corresponding chi² values
plt.plot(I_values[min_index - 60:min_index + 60],
         chi_squared_values[min_index - 60:min_index + 60])

# plots single point at the value of optimal average ionisation energy
plt.scatter(I_opt, min_chi_squared, color='red',
            label=f'AIE = {I_opt:.1f} eV')

# plots a vertical line at the intersection points, this shows our upper and lower confidence interval
for i, I_intersection in enumerate(intersection_I_values):
    plt.axvline(x=I_intersection, color='purple', linestyle='--',
                label='\u03C7\u00B2 + 1' if i == 0 else '')
    plt.text(I_intersection, min_chi_squared + 0.4,
              f'{I_intersection:.1f}', rotation=0, color='purple',  fontsize=14)

# Gives axes labels, shows legend and plot.
plt.ylabel("\u03C7\u00B2")
plt.xlabel('Average Ionisation Energy (eV)')
plt.legend()
plt.show()

# prints the uncertainty in AIE
print("Uncertainty = ±", (intersection_I_values[1] - intersection_I_values[0])/2)
