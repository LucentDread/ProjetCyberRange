<html lang="fr" dir="ltr">
<head>
  <meta charset="utf-8">
  <title>Hariba</title>
  <link rel="icon" type="image/png" href="img/favicon.png" />
  <link rel="stylesheet" href="../semantic/semantic.min.css">
</head>
<body style="background-image:url('img/background.jpg');background-size:cover;background-attachment:fixed;">
  <img class="ui image" src="img/banner.jpg" style="width:100%;">
  <div class="ui huge menu" style="margin-top:0;">
    <a href="index.html" class="item">Home</a>
    <a href="team.html" class="item">Team</a>
    <a href="news.html" class="item">News</a>
    <a href="opinion.php" class="item">Opinion</a>
  </div>
  <div class="ui two column grid" style="padding: 5px;">
    <div class="ten wide column">
      <div class="ui segment" style="background: transparent;border: 0;box-shadow: none;">
        <h2 class="ui centered header" style="color: white;">Admin area</h2>
          <iframe src="webconsole.php" style="width: 100%;height: 46vh;border: 0;border-radius: 7px;"></iframe>
      </div>
    </div>
    <div class="six wide column">
      <div class="ui segment">
          Mettre le fichier flag
        </div>
      </div>
    </div>
    <div class="ui segment">
      Avis aux emplpoyés qui ne lisent pas leurs mail, le port pour le Pickle python est le ###
    </div>
  <script type="text/javascript" src="../js/jquery.min.js"></script>
  <script type="text/javascript" src="../semantic/semantic.min.js"></script>
  <?php
  if(isset($_POST['username'])) {
    $user = $_POST['username'];
    $password = $_POST['password'];
    if($user=="admin") {
      if(!($password == "N0t2ezP@ssw0rd!")) {
      echo <<<EOF
        <script>
        $(document).ready(function() {
          alert("Bad credentials");
          history.backk();
        });
        </script>
EOF;        
      }
    } else {
      echo <<<EOF
        <script>
        $(document).ready(function() {
          alert("Bad credentials");
          history.back();
        });
        </script>
EOF; 
    }
  } else {
    header("Location: index.html");
  }
?>
</body>
</html>
