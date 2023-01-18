<?php

function vyber_nahodny_recept($adresar_s_recepty){
    $recepty_soubory = scandir($adresar_s_recepty);
    $recepty_soubory = array_diff($recepty_soubory, ['.', '..'] );
    if (empty($recepty_soubory)){
        $nahodny_recept = "#";
    } else {
        $nahodny_recept = $recepty_soubory[array_rand($recepty_soubory)];
    }
    return $nahodny_recept;
}

function vyber_recepty_z_cookies($nazev_cookie){
    if(isset($_COOKIE[$nazev_cookie])) {
        echo "Cookie '" . $nazev_cookie . "' is set!<br>";
        echo "Value is: " . $_COOKIE[$nazev_cookie];
    }
}

?>