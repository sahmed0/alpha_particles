# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 13:59:07 2023

@author: ahmed
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# Function to read data from a CSV file and plot a graph with error bars
def plot_graph(csv_file):
    # Read data from CSV file using pandas
    data = pd.read_csv(csv_file)

    # Extracting data from columns
    x_values = data['Thickness']
    y_values = data['Stopping']
    error_values = data['errors']
    
    # Calculate the line of best fit using numpy
    slope, intercept = np.polyfit(x_values, y_values, 1)
    
    # Plotting the graph with error bars
    plt.errorbar(x_values, y_values, yerr=error_values, fmt='o--', label='Data with Error Bars')
    
    # Plotting the line of best fit
    # plt.plot(x_values, slope * x_values + intercept, color='red', label='Line of Best Fit')

    # Adding labels and title
    plt.xlabel('Thickness (mm)')
    plt.ylabel('Stopping Power (MeV/mm)')
    # plt.title('Energy - Thickness for Helium')

    # legend
    # plt.legend()

    # Display the plot
    plt.show()

# location of the file that is being read
plot_graph('Data_For_Fit.csv')
