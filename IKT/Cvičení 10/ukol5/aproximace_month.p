set terminal png
set output "bcmonth.png"
f(x) = a*x**4 + b*x**3 + c*x**2 + d*x + e
a=0;b=0;c=0;d=0;e=0
fit f(x) "bitcoin_month.dat" u 1:2 via a,b,c,d,e
plot "bitcoin_month.dat" u 1:2 with p pt 7 ps 2, a*x**4 + b*x**3 + c*x**2 + d*x + e lw 3 lt 8
