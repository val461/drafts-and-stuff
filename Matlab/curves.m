clear all;

c=0;
d=100;
s=10000;
t=linspace(c,d,s);

p=0.1;
a=0;
b=7;
for i=a:p:b
  plot(cos(i*t),sin(t*(i-1)).*cos(t*(i+2)));
  axis("equal");
  pause(0.1);
end
