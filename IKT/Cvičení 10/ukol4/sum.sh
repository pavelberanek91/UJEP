python sum.py
gnuplot sum.p
convert -delay 20 -loop 0 sum*.png sum.gif
rm sum*.png
rm sum*.dat
