<?php

$target_dir = "uploads/";
$target_file = $target_dir . basename($_FILES["file"]["name"]);
$fileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));

if ($fileType != "mp4") {
	echo "Supported file formats: MP4";
	return;
}

if (move_uploaded_file($_FILES["file"]["tmp_name"], $target_file)) {
	echo "File Uploaded.";
}
else {
	echo "Error uploading file!";
}

shell_exec("./convert.sh $target_file");

?>
