% Define the file path and sheet name
file_path = 'Bragg.xlsx';
sheet_name = 'Sheet1';

% Read data from Excel sheet
data = readtable(file_path, 'Sheet', sheet_name);

% Extract relevant columns from the table
x_data = data.thickness;  % Replace 'x_column_name' with the actual name of your x-axis column
y_data = data.stopping_power;  % Replace 'y_column_name' with the actual name of your y-axis column
error_y = data.sp_errors;  % Replace 'error_y_column_name' with the actual name of your y-axis error column

% Create a smooth line plot with markers
figure;
plot(x_data, y_data, 'b-', 'LineWidth', 2.0);
hold on;
errorbar(x_data, y_data, error_y, 'bo', 'MarkerSize', 8, 'MarkerEdgeColor', 'b', 'MarkerFaceColor', 'w');
hold off;

xlabel('Effective Thickness / Path Length (μm)');
ylabel('Stopping Power (-keV/μm)');
title('Nickel Bragg Curve');
grid on;
grid minor;


% Customize plot appearance if needed
% For example:
% xlim([min(x_data) max(x_data)]);
% ylim([min(y_data) max(y_data)]);

% Save the plot if needed
% saveas(gcf, 'scatter_plot_with_error_bars.png');