<?php

ini_set('display_errors',1);
error_reporting(E_ALL);

$target_dir = "./fdd/input/";
$target_file = $target_dir . basename($_FILES["file"]["name"]);
$fileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));

if ($fileType != "mp4") {
	echo "Supported file formats: MP4";
	return;
}

if (move_uploaded_file($_FILES["file"]["tmp_name"], $target_file)) {
	shell_exec("./fdd/convert.sh $target_file");
	header("Location: success.html");
	exit();
}
else {
	header("Location: error.html");
	exit();
}

?>
