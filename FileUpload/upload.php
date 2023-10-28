<?php
$target_dir = "uploads/";
$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
$uploadOk = 1;
$imageFileType = strtolower(pathinfo($target_file, PATHINFO_EXTENSION));

// Check if image file is a valid image
if(isset($_POST["submit"])) {

// Check if the file has a .php extension
if (strtolower(pathinfo($target_file, PATHINFO_EXTENSION)) === 'php') {
  echo "Uploading files with .php extension is not allowed.";
  $uploadOk = 0;
}

// Move the file to the target directory
if ($uploadOk == 1) {
  if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
    echo "The file ". basename( $_FILES["fileToUpload"]["name"]). " has been uploaded.";
  } else {
    echo "Sorry, there was an error uploading your file.";
  }
}
}
?>
