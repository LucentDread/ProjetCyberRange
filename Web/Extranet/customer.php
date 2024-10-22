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
      <div class="ui segment" style="background-color: transparent; border: transparent; box-shadow: none;">
        <form method="post" enctype="multipart/form-data" action="customer.php">
          <div class="ui form">
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
                <input type="file" name="myfile" accept="image/*, .pdf">
              </div>
            </div>
            <div class="ui input">
              <input type="submit" value="Send" class="ui blue button">
            </div>
                <?php
    // File sending and error test
    if (isset($_FILES['myfile']) AND $_FILES['myfile']['error'] == 0) {
      // File size test
      if ($_FILES['myfile']['size'] <= 50000000) {
        // Extension test
        $fileinfo = pathinfo($_FILES['myfile']['name']);
        $upload_extension = $fileinfo['extension'];
        $allowed_extensions = array('jpg', 'jpeg', 'gif', 'png', 'pdf');
        if (in_array($upload_extension, $allowed_extensions)) {
          // File validation and permanent storage
          move_uploaded_file($_FILES['myfile']['tmp_name'], 'uploads/' . basename($_FILES['myfile']['name']));
          $action = "positive";
          $message = "Your file has been transmitted, you will be contacted by email as soon as the file has been processed.";
        } else {
          $action = "negative";
          $message = "Invalid file type.";
        }
      } else {
        $action = "negative";
        $message = "Your file is too big, please submit a file smaller than 50MB.";
      }
    } else {
      $action = "hidden";
      $message = "Please submit a file.";
    }
    echo <<<EOF
      <div class="ui $action message">
      $message
      </div>
EOF;

      // ----- FTP UPLOAD -----
      // Setting up a basic connection
      $ftp_server = "grosftp.com";
      $conn_id = ftp_connect($ftp_server);

      // Identification with a username and password
      $ftp_user_name = "willywonka";
      $ftp_user_pass = "comeandlickmycandy";
      $login_result = ftp_login($conn_id, $ftp_user_name, $ftp_user_pass);
      ftp_pasv($conn_id, true);

      // Checking the connection
      if ((!$conn_id) || (!$login_result)) {
        echo "FTP connection failed!";
        echo "Attempted to connect to $ftp_server for user $ftp_user_name";
        exit;
      } else {
        echo "Connected to $ftp_server, for user $ftp_user_name";
      }

      // Uploading a file
      $destination_file= "destination";
      $upload = ftp_put($conn_id, $destination_file, $source_file, FTP_BINARY);

      // Checking the status of the upload
      if (!$upload) {
        echo "FTP upload failed!";
      } else {
        echo "File $source_file uploaded to $ftp_server as $destination_file";
      }

      // Fermeture du flux FTP
      ftp_close($conn_id);

    ?>


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
  </div>
  <script type="text/javascript" src="../js/jquery.min.js"></script>
  <script type="text/javascript" src="../semantic/semantic.min.js"></script>
  <?php
  ini_set('display_errors', 1);
  ini_set('display_startup_errors', 1);
  error_reporting(E_ALL);
  if(isset($_GET['username']) && isset($_GET['password']) || isset($_FILES['myfile'])) {
    if(!isset($_FILES['myfile'])) {
    $username = $_GET['username'];
    $password = $_GET['password'];
    $mysqli = new mysqli("127.0.0.1", "root", "toort", "cyberrange");
    $query = $mysqli->query("SELECT * FROM users WHERE username='".$username."' and password='".$password."'");
    if($query->num_rows == 0) {
      echo <<<EOF
      <script>
      $(document).ready(function() {
        alert("Bad credentials");
        history.back();
        });
        </script>
EOF;
      }
    }
    } else {
      header("Location: index.html");
    }
    ?>
  </body>
  </html>
