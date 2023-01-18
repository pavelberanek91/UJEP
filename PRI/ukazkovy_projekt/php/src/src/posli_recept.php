<?php 
ob_start();
?>

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <title>Mixolog|Pošli recept</title>
  </head>
  <body>

  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container-fluid">
        <a href="../index.php" class="navbar-brand">Mixolog</a>
        <button type="button" class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#navbarCollapse">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarCollapse">
          <div class="navbar-nav">
            <a href="../index.php" class="nav-item nav-link">Domů</a>
              <?php
                require_once('sluzby.php');
                $adresar_s_recepty = '../dokumenty/';
                $nahodny_recept = vyber_nahodny_recept($adresar_s_recepty);
                echo '<a href="../dokumenty/'. $nahodny_recept . '" class="nav-item nav-link">Náhodný recept</a>';
              ?>      
              <a href="receptar.php" class="nav-item nav-link">Receptář</a>
              <a href="posli_recept.php" class="nav-item nav-link active">Pošli recept</a>
          </div>
          <div class="navbar-nav ms-auto">
            <a href="registrace.php" class="nav-item nav-link">Registrace</a>
            <a href="prihlaseni.php" class="nav-item nav-link">Přihlášení</a>
          </div>
        </div>
      </div>
    </nav>

<div class="container">

    <div class="p-5 my-4 bg-light rounded-3">
        <h1>Pošli recept</h1>
        <p class="lead">
          Chcete se podělit s námi o úžasný recept, který nám v databázi chybí? Neváhejte a zašlete nám ho. Stačí vytvořit XML soubor, který splňuje následující .DTD schéma: <a href="../šablony/menu.dtd">ZDE</a>
        </p>
        <form enctype="multipart/form-data" action="posli_recept.php" method="POST">
          <label for="recept" class="form-label">Přetažením nebo kliknutím nahrajte recept ve validním XML souboru.</label>
          <div class="file-upload-wrapper">
            <input type="file" name="recept" class="file-upload" data-max-file-size="2M"/>
          </div>
          <br>
          <button type="submit" class="btn btn-success btn-lg">Odeslat</button>
        </form>
    </div>

    <?php

      if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        $adresar_recepty = '../recepty/';
        $nahrany_recept = $adresar_recepty . basename($_FILES['recept']['name']);

        if (file_exists($nahrany_recept)){
          echo '<p class="text-danger">Soubor se stejným názvem již existuje v databázi. Prosím přejmenujte soubor.!</p>';
        } else if (move_uploaded_file($_FILES['recept']['tmp_name'], $nahrany_recept)) {

          /* DTD validace
          $puvodni_xml = new DOMDocument();
          $puvodni_xml->load($nahrany_recept);
          $koren = 'drink';
          $generator_dokumentu = new DOMImplementation;
          $doctype = $generator_dokumentu->createDocumentType($koren, "", 'recept.dtd');
          $novy_xml = $generator_dokumentu->createDocument(null, "", $doctype);
          $novy_xml->encoding = "utf-8";

          $puvodni_uzel = $puvodni_xml->getElementsByTagName($koren)->item(0);
          $novy_uzel = $novy_xml->importNode($puvodni_uzel, true);
          $novy_xml->appendChild($novy_uzel);

          if ($novy_xml->validate()) {
          */

          // XSD validace
          $xml = new DOMDocument;
          $xml->load($nahrany_recept);
          if ($xml->schemaValidate('../šablony/recept.xsd')){
          
            echo '<p class="text-success">Nahraný soubor je validní a byl úspěšně nahrán do databáze.</p>';
            
            // XML
            $xml_dokument = new DOMDocument();
            $xml_dokument->load($nahrany_recept);

            // XSL
            $xsl_dokument = new DOMDocument();
            $xsl_dokument->load("../styly/recept.xsl");

            // XSLTtransformation
            $xsl_procesor = new XSLTProcessor();
            $xsl_procesor->importStylesheet($xsl_dokument);
            $transformovany_xml = $xsl_procesor->transformToDoc($xml_dokument);
              
            // ulozeni transformovaneho dokumentu
            $nazev_dokumentu = basename($_FILES['recept']['name']) . ".html";
            $transformovany_xml->save("../dokumenty/" . $nazev_dokumentu );

            // ulozeni nahraneho souboru do cookies
            $cookie_klic = 'mixology';
            $pocet_sekund = 3600;
            if(isset($_COOKIE[$cookie_klic])) {              
              $cookie_hodnota = $_COOKIE[$cookie_klic] . ';' . $nahrany_recept;  
            } else {
              $cookie_hodnota = $nahrany_recept;
            }
            setcookie($cookie_klic, $cookie_hodnota, time() + $pocet_sekund, "/");
            ob_end_flush();

          } else {
            echo '<p class="text-warning">Nahraný soubor není validní! Prosím zkontrolujte správnou strukturu.</p>';
            unlink($nahrany_recept);
          }
        } else {
            echo '<p class="text-danger">Došlo k chybě při nahrávání souboru!</p>';
        }
      }

    ?>

    <hr>
    <footer>
        <div class="row">
            <div class="col-md-6">
                <p>Copyright &copy; 2022 Mixolog s.r.o.</p>
            </div>
            <div class="col-md-6 text-md-end">
            <p>šablona stažena z: <a href="https://www.tutorialrepublic.com/twitter-bootstrap-tutorial/bootstrap-responsive-layout.php">tutorialrepublic</a></p>
            </div>
        </div>
    </footer>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
</body>
</html>