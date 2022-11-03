set terminal png
set palette grey
do for [i=1:50]{
    if (i < 10){
        set output "sum0".i.".png" 
        plot "sum0".i.".dat" matrix with image
    } else {
        set output "sum".i.".png"
        plot "sum".i.".dat" matrix with image
    }
}
