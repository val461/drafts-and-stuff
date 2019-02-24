clear all;
clf;

# À périmètre fixé, l'aire du rectangle est maximisée lorsqu'il est un carré.

a=4
b=7

X=linspace(b,a,100);
Y=linspace(a,b,100);
A=X.*Y;

hold on;

plot3(X,Y,A);

xlabel("x");
ylabel("y");
zlabel("A");

%~ grid on;
