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
              <a href="receptar.php" class="nav-item nav-link active">Receptář</a>
              <a href="posli_recept.php" class="nav-item nav-link">Pošli recept</a>
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

            <h1>Receptář</h1>
            <p class="lead">
                Zde naleznete seznam všech receptů, které nám fanoušci poslali. Při kliku na název drinku se zobrazí stránka s receptem.
            </p>
        
            <ol class="list-group list-group-light list-group-numbered">

            <?php

                $recepty_soubory = scandir('../recepty/');
                $recepty_soubory = array_diff( $recepty_soubory, ['.', '..'] );

                foreach ($recepty_soubory as $recept_soubor) {
                    echo '<li class="list-group-item d-flex justify-content-between align-items-start">';
                    echo '<div class="ms-2 me-auto">';
                    $xml = simplexml_load_file('../recepty/' . $recept_soubor);
                    if ($xml == true){
                        echo '<div class="fw-bold"><a href="../dokumenty/'. $recept_soubor .'.html">'. $xml->informace->název . '</a></div>';
                        $polozky = '';
                        foreach ($xml->ingredience->children() as $polozka){
                            $polozky = $polozky . $polozka . ', ';
                        }
                        $polozky = substr($polozky, 0, -2);
                        echo $polozky;
                        echo '</div>';
                    }
                    echo '</li>';
                }

            ?>

            </ol>
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