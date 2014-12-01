clear all
clc
close all

food = {'Rice';
    'Quinoa';
    'Tortilla';
    'Lentils';
    'Broccoli'};

nutrients = {'Carbs';
    'Proteins';
    'Fat'};

amountOfNutrientsPerFood = [53 4.4 0.4
    40 8 3.6
    12 3 2
    53 12 0.9
    6 1.9 0.3];

cost = [0.5
    0.9
    0.1
    0.6
    0.4];

min_nutrients = [100
    10
    0];

max_nutrients = [1000
    100
    100];

sol = linprog(cost,[amountOfNutrientsPerFood';-amountOfNutrientsPerFood'],[max_nutrients;-min_nutrients],[],[],zeros(1,5));
I2 = find(sol>1e-6);
disp(cost'*sol);
for ii=1:length(I2)
    disp(food{I2(ii)})
end