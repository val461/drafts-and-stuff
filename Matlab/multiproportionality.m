clear all;
clf;

a=-100;
b=100;
mu=1;

[X,Y]=meshgrid(linspace(a,b,50), linspace(a,b,50));
Z=mu*X.*Y;

hold on;

surface(X,Y,Z);

xlabel("x");
ylabel("y");
zlabel("z");

grid on;
