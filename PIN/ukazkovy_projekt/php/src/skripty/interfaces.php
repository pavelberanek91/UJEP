<?php

#definice jmenneho prostoru
namespace interfaces;

#rozhrani - vsechny tridy, ktere ho implementuji se zavazuji k implementaci metod
interface XMLZapisovatelne {
    public function zapisDoXML($cesta);
}

interface SessionZapisovatelne {
    public function zapisDoSession($klic, $hodnota);
}

?>