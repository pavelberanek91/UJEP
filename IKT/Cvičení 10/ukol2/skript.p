stats "pocasi.dat" u 1:2
plot "pocasi.dat" u 1:(($2-STATS_min_y)/(STATS_max_y-STATS_min_y)*100) w lp pt 7
