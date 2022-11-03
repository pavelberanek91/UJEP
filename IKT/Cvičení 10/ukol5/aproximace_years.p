set terminal png
set output "bcyear.png"
f(x) = a + b*x + c*x**2 + d*x**3
a=1.0;b=1.0;
fit f(x) "bitcoin_years.dat" u 1:2 via a,b,c,d
plot "bitcoin_years.dat" u 1:2 with p pt 7 ps 2, a + b*x + c*x*x + d*x*x*x lw 3 lt 8
