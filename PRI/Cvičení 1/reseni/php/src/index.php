<!DOCTYPE html>

<html>

<head>
    <title>Fakultonahrávač</title>
</head>

<body>
    <h1>Fakultonahrávač</h1>
    <form enctype="multipart/form-data" action="index.php" method="POST">
        <label for="fakulta">Kliknutím nahrajte recept ve validním XML souboru.</label>
        <br>
        <input type="file" name="fakulta" data-max-file-size="2M"/>
        <br>
        <button type="submit">Odeslat</button>
    </form>

<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $adresar_fakulty = 'fakulty/';
    $nahrana_fakulta = $adresar_fakulty . basename($_FILES['fakulta']['name']);

    if (file_exists($nahrana_fakulta)){
        echo '<p class="text-danger">Soubor se stejným názvem již existuje v databázi. Prosím přejmenujte soubor.!</p>';
    } 
    else if (move_uploaded_file($_FILES['fakulta']['tmp_name'], $nahrana_fakulta)) {
        $puvodni_xml = new DOMDocument();
        $puvodni_xml->load($nahrana_fakulta);
        $koren = 'fakulta';
        $generator_dokumentu = new DOMImplementation;
        $doctype = $generator_dokumentu->createDocumentType($koren, "", 'fakulta.dtd');
        $novy_xml = $generator_dokumentu->createDocument(null, "", $doctype);
        $novy_xml->encoding = "utf-8";

        $puvodni_uzel = $puvodni_xml->getElementsByTagName($koren)->item(0);
        $novy_uzel = $novy_xml->importNode($puvodni_uzel, true);
        $novy_xml->appendChild($novy_uzel);

        if ($novy_xml->validate()) {
            echo '<p>Nahraný soubor je validní a byl úspěšně nahrán do databáze.</p>';
        } else {
            echo '<p>Nahraný soubor není validní! Prosím zkontrolujte správnou strukturu.</p>';
            unlink($nahrana_fakulta);
        }
    } else {
         echo '<p>Došlo k chybě při nahrávání souboru!</p>';
    }
}
?>

</body>

</html>