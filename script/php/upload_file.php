<?php

ini_set('display_errors',1);
error_reporting(E_ALL);

$root_dir = $_SERVER["DOCUMENT_ROOT"];
$target_dir = $root_dir."/fdd/input/";
$target_file = $target_dir . basename($_FILES["file"]["name"]);
$fileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));
$screen_driver = "echo -n images > fdd_fifo";

if ($fileType != "mp4") {
	echo "Supported file formats: MP4";
	return;
}

if (move_uploaded_file($_FILES["file"]["tmp_name"], $target_file)) {
	shell_exec($root_dir."/fdd/convert.sh $target_file");
	shell_exec($screen_driver);
	header("Location: /modes/success.html");
	exit();
}
else {
	header("Location: /modes/error.html");
	exit();
}

?>
