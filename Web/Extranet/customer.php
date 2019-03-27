<!DOCTYPE html>
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
    <a href="opinion.html" class="item">Opinion</a>
  </div>
  <div class="ui two column grid" style="padding: 5px;">
    <div class="ten wide column">
      <div class="ui segment" style="background: transparent; border: transparent;">
        <div class="ui form" method="post" action="customer.php">
          <h2 class="ui centered header" style="color: white;">Customer area</h2>
          <h3 class="ui header" style="color: white;">Submit your file here</h3>
          <div class="field">
            <div class="ui input">
              <input type="text" placeholder="Filename" name="filename">
            </div>
          </div>
          <div class="field">
            <div class="ui input">
              <textarea name="file_desc" placeholder="File description"></textarea>
            </div>
          </div>
          <div class="field">
            <div class="ui input">
              <input type="file" id="file" name="file" accept="image/*, .pdf">
            </div>
          </div>
          <div class="ui input">
            <input type="submit" value="Send" class="ui blue button">
          </div>
        </div>

        <?php

        $mysqli = mysqli_connect("localhost", "root", "", "");

        if(!$mysqli){
          echo "Error connecting to the database.";
        } else {

          $AfficherFormulaire=1;

          if(isset($_POST['file'])){

            if(empty($_POST['file'])){
              echo "Please submit a file.";

            } elseif(){

              echo "Invalid file type.";

            } else {
              echo "Your file has been transmitted, you will be contacted by email as soon as the file has been processed.";

              $AfficherFormulaire=0;
            }
          }
        }
        if($AfficherFormulaire==1){
          ?>

          <?php
        }
        ?>

      </div>
    </div>
    <div class="six wide column">
      <div class="ui segment">
        <div class="ui form">
          <h2 class="ui centered header">Administration section</h2>
          <div class="field">
            <div class="ui input">
              <input type="text" placeholder="Username" name="username">
            </div>
          </div>
          <div class="field">
            <div class="ui input">
              <input type="password" placeholder="Password" name="password">
            </div>
          </div>
          <div class="ui input">
            <input type="submit" value="Log in" class="ui blue button">
          </div>
        </div>
      </div>
    </div>
  </div>
  <script type="text/javascript" src="../js/jquery.min.js"></script>
  <script type="text/javascript" src="../semantic/semantic.min.js"></script>
</body>
</html>
