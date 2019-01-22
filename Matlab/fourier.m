clear all;
close all;
X=linspace(-pi,pi);
m=-1;
Y=zeros(size(X));
kX=Y;
for k=1:500
  m=-m;
  kX+=X;
  Y+=(2*m/k)*sin(kX);
  plot(X,X,X,Y)
  grid on;
  pause(0.0002)
endfor
