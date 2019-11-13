<?php

$target_file = "./fdd/output/message.txt";

if(isset($_POST['text'])) {
    $ret = file_put_contents($target_file, $_POST['text']);
    if($ret === false) {
	header("Location: error.html");
	exit();
    }
    else {
	header("Location: success.html");
	exit();
    }
}
else {
    header("Location: error.html");
    exit();
}

?>
