% Load data from the spreadsheet
data = xlsread('Energy_Thickness_Values.xlsx');

% Extract data for energies
t1 = data(:, 1);
t2 = data(:, 2);
t3 = data(:, 3);
t4 = data(:, 4);
t5 = data(:, 5);

% Extract data for thicknesses
E1 = data(:, 6);
E2 = data(:, 7);
E3 = data(:, 8);
E4 = data(:, 9);
E5 = data(:, 10);

% Assume error data is in the next columns (adjust indices accordingly)
error_set1 = data(:, 11);
error_set2 = data(:, 12);
error_set3 = data(:, 13);
error_set4 = data(:, 14);
error_set5 = data(:, 15);

% Create a scatter plot with error bars
figure;
% errorbar(E1, t1, error_set1, 'r-', 'LineWidth', 1.0, 'Marker', 'o', 'MarkerSize', 6, 'MarkerEdgeColor', 'r', 'MarkerFaceColor', 'w', 'DisplayName', 'Argon');
hold on;
% errorbar(E2, t2, error_set2, 'g-', 'LineWidth', 1.0, 'Marker', 'o', 'MarkerSize', 6, 'MarkerEdgeColor', 'g', 'MarkerFaceColor', 'w', 'DisplayName', 'Nitrogen');
% errorbar(E3, t3, error_set3, 'b-', 'LineWidth', 1.0, 'Marker', 'o', 'MarkerSize', 6, 'MarkerEdgeColor', 'b', 'MarkerFaceColor', 'w', 'DisplayName', 'Helium');
errorbar(E4, t4, error_set4, 'r-', 'LineWidth', 1.0, 'Marker', 'o', 'MarkerSize', 6, 'MarkerEdgeColor', 'r', 'MarkerFaceColor', 'w', 'DisplayName', 'Nickel');
errorbar(E5, t5, error_set5, 'g-', 'LineWidth', 1.0, 'Marker', 'o', 'MarkerSize', 6, 'MarkerEdgeColor', 'g', 'MarkerFaceColor', 'w', 'DisplayName', 'Aluminium');

% Add legend and labels
legend('Location', 'eastoutside');
xlabel('Thickness (μm)');
ylabel('Energy (keV)');
title('Energy - Thickness graph');
grid on;
grid minor;

% Hold off to stop adding to the current plot
hold off;
