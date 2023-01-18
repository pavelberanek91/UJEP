<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <title>Mixolog</title>
  </head>
  <body>

  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container-fluid">
        <a href="#" class="navbar-brand">Mixolog</a>
        <button type="button" class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#navbarCollapse">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarCollapse">
          <div class="navbar-nav">
            <a href="index.php" class="nav-item nav-link active">Domů</a>
              <?php
                require_once('sluzby.php');
                $adresar_s_recepty = 'dokumenty/';
                $nahodny_recept = vyber_nahodny_recept($adresar_s_recepty);
                echo '<a href="../dokumenty/'. $nahodny_recept . '" class="nav-item nav-link">Náhodný recept</a>';
              ?>      
              <a href="src/receptar.php" class="nav-item nav-link">Receptář</a>
              <a href="src/posli_recept.php" class="nav-item nav-link">Pošli recept</a>
          </div>
          <div class="navbar-nav ms-auto">
            <a href="src/registrace.php" class="nav-item nav-link">Registrace</a>
            <a href="src/prihlaseni.php" class="nav-item nav-link">Přihlášení</a>
          </div>
        </div>
      </div>
    </nav>

<div class="container">

    <div class="p-5 my-4 bg-light rounded-3">
        <h1>Mixolog</h1>
        <p class="lead">Barmanská profese se děli na dva tábory. Jedni vám v roztrhaných džínách a ušmudlaném tričku nalijí panáka vodky za 30 Kč, jiní vám v pečlivě vyžehleném obleku s pěstovaným knírkem udělají pečlivě nalitý koktejl za 500 Kč. Ten druhý typ barmanů nazýváme mixology, praktikanty oboru mixologie, což je odborný termín pro tvorbu opravdu dobrých koktejlů.</p>
        <p><a href="https://www.tutorialrepublic.com" target="_blank" class="btn btn-success btn-lg">Poznej svět mixologie</a></p>
    </div>

    <div class="row g-3">

      <?php

      $host = 'db';
      $uzivatel = 'administrator';
      $heslo = 'heslo';
      $database = 'alkoholnik';

      $spojeni = new mysqli($host, $uzivatel, $heslo, $database);
      if ($spojeni->connect_error){
        die('Chyba spojeni s DB' . $spojeni->connect_error);
      } else {
        echo '<h1>Registrovani uzivatele</h1>';
      }

      $sql = 'SELECT * FROM uzivatele';
      if ($vysledek_dotazu = $spojeni->query($sql)) {

        while ($data = $vysledek_dotazu->fetch_object()) {
          $uzivatele[] = $data;
        }

        foreach ($uzivatele as $uzivatel) {
          echo '<div class="col-md-6 col-lg-4 col-xl-3">';
          echo '<h2>' . $uzivatel->jmeno . '</h2>';
          echo '<p>' . $uzivatel->heslo . '</p>';
          echo '<p><a href="https://www.tutorialrepublic.com/html-tutorial/" target="_blank" class="btn btn-success">Learn More &raquo;</a></p>';
          echo '</div>';
        }
      }

      ?>

    </div>
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