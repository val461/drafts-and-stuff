clear all;
clf;

T=linspace(0,2,100);
X=T.^4;
Y=1+T+sin(2*pi*T);

hold on;

plot3(X,T,Y);
plot3(X,T,zeros(size(Y)));
plot3(zeros(size(X)),T,Y);

xlabel("x(t)");
ylabel("t");
zlabel("y(t)");
legend("v(t)","x(t)","y(t)");

axis nolabel;
grid on;
