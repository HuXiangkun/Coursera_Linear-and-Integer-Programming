clear all
clc
close all

data = importdata('Data_Corr.txt');
t = data(:,1);
n = length(t);
y_corr = data(:,2);

A = [ones(n,1) t t.^2 t.^3 t.^4];
b = y_corr

Sol = pinv(A)*b;
y_sol = Sol(1) + Sol(2).*t + Sol(3).*t.^2 + Sol(4).*t.^3 + Sol(5).*t.^4;

Sol(2)

hold on
plot(t,y_sol,'r','linewidth',2)

set(gca,'fontsize',18)