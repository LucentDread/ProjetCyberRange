<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);
$mysqli = new mysqli('127.0.0.1', 'root', 'toort', 'cyberrange');
$opinions = $mysqli->query("SELECT * FROM opinion");
if(isset($_POST['opinion'])) {
  $mysqli->query("INSERT INTO opinion(content) VALUES ('".$_POST['opinion']."')");
  header("Location:opinion.php");
}

?>
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
    <a href="opinion.php" class="active item">Opinion</a>
  </div>
  <div class="ui two column grid" style="padding: 5px;">
    <div class="ten wide column">
      <div class="ui segment" style="color:white !important;background-color: transparent; border: transparent; box-shadow: none;">
        <?php

        while ($op = $opinions->fetch_assoc()) {
          $content = $op["content"];
          $date = $op["date"];
          echo <<<EOF
          <div class="ui segment" style="color:black;">
            $content<br />
            <span style="display:block;text-align:right;color:grey;">$date</span>
          </div>
EOF;
        }

         ?>
      </div>
      <hr />
      <div class="ui segment" style="color:white !important;background-color: transparent; border: transparent;">
        <h1 class="ui header" style="color:white">Give your opinion</h1>
        Any question ? Any observation ?<br>
        Do not hesitate to give us a feedback on your Hariba experience by using the following input field !<br>
        Our team will answer you as soon as possible <br><br>
        <form method="POST">
        <div class="ui form">
          <div class="field">
            <label></label>
            <textarea name="opinion" placeholder="Leave a review here!"></textarea>
          </div>
          <div class="ui input">
            <input class="ui blue button" type="submit" value="Send your comment">
          </div>
        </div>
      </form>
      </div>
    </div>
    <div class="six wide column">
      <div class="ui bottom attached segment">
        <h2 class="ui header">Contact us</h2>
        <i class="big blue mail icon"></i><i style="font-family:lato;" class="big blue icon">contact@hariba.fr</i><hr>
        <i class="big blue phone icon"></i><i style="font-family:lato;" class="big blue icon">09.12.66.69.42</i>
      </div>
    </div>
  </div>
  <script type="text/javascript" src="../js/jquery.min.js"></script>
  <script type="text/javascript" src="../semantic/semantic.min.js"></script>
</body>
</html>
