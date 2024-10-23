% Define the file path and sheet name
file_path = 'Energy_Thickness_Values.xlsx';
sheet_name = 'Sheet2';

% Read data from Excel sheet
data = readtable(file_path, 'Sheet', sheet_name);

% Extract relevant columns from the table
x_data = data.thickness;  % Replace 'x_column_name' with the actual name of your x-axis column
y_data = data.energy;  % Replace 'y_column_name' with the actual name of your y-axis column
error_y = data.energy_errors;  % Replace 'error_y_column_name' with the actual name of your y-axis error column

% Create a scatter plot with error bars for both x and y axes
figure;
errorbar(x_data, y_data, error_y, 'o', 'MarkerEdgeColor', '#4DBEEE', 'MarkerFaceColor', '#4DBEEE');
xlabel('Thickness (μm)');
ylabel('Energy (keV)');
title('Energy - Thickness graph');
grid on;
grid minor;

% Customize plot appearance if needed
% For example:
% xlim([min(x_data) max(x_data)]);
% ylim([min(y_data) max(y_data)]);

% Save the plot if needed
% saveas(gcf, 'scatter_plot_with_error_bars.png');