scale = 0.5
plot "scalar.dat" w image, "vec.dat" u 1:2:($3*scale):($4*scale) w vectors
