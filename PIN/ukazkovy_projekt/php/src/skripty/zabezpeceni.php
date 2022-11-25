<?php
namespace zabezpeceni;

/* 
Rysy jsou metody, ktere resi problem vicenasobne dedicnosti v PHP.
Jedna se o metody, ktere mohou byt nahrany vice tridami a jsou tedy volatelne jejich instancemi.
*/
trait Zabezpeceni {

    //XSS utoky typu: <script>location.href('http://www.hacked.com/%27)</script>
    public function predzpracuj_vstup($data){  //ochrani pred XSS utoky
        $data = trim($data);                   //stripnuti bilych znaku
        $data = stripslashes($data);           //odstran lomitka
        $data = htmlspecialchars($data);       //preved html znaky na jejich entitni podobu
        return $data;
    }
}
?>