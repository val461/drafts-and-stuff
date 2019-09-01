close all;
##clear all;
##figure()

mise1 = 100;

##cote1 = 2.6; cote2 = 1.65;

##s = 1.0451612903225806;
cote1 = 2.4
cote2 = 1.36
##cote2 = 1/(s-1/cote1)

g1 = (cote1 - 1) * mise1;
l1 = 0;
mise2 = linspace(0, g1, 120);

g2 = (cote2 - 1) * mise2;
l2 = mise2;

g_cas_1 = g1 - l2;
g_cas_2 = g2 - l1;

p1 = 1/cote1;
p2 = 1/cote2;
E = g_cas_1 * p1 + g_cas_2 * p2;
##mean(E)
##e_alt = cote2/(cote1+cote2) * g_cas_1 + cote1/(cote1+cote2) * g_cas_2
f = g_cas_2 ./ g_cas_1;
disp('mise2 conseillée :')
mean(mise2(find(abs(f-cote1 / cote2)<0.1)))

plot(mise2, E, mise2, g_cas_1, mise2, g_cas_2)
set(gca,'FontSize',12)
xlabel("mise2", 'FontSize', 16);
ylabel("gains", 'FontSize', 16);
lgd = legend("E","g cas 1",'g cas 2');
set(lgd, 'FontSize', 13);
