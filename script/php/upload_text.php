<?php

ini_set('display_errors',1);
error_reporting(E_ALL);

$root_dir = $_SERVER["DOCUMENT_ROOT"];
$target_file = $root_dir."/fdd/text/message.txt";
$screen_driver = "echo -n text > fdd_fifo";

if(isset($_POST['text'])) {
	$ret = file_put_contents($target_file, $_POST['text']);
	if($ret == false) {
		header("Location: /modes/error.html");
		exit();
	}
	else {
		shell_exec($screen_driver);
		header("Location: /modes/success.html");
		exit();
	}
}
else {
	header("Location: /modes/error.html");
	exit();
}

?>
