<?php
	include_once($_SERVER['DOCUMENT_ROOT'].'/val/VirtualCurrency/phptools/constants.php');

	include_once(ROOT.'phptools/crypt.php');
	include_once(ROOT.'phptools/new.php');

	if(isset($_GET['length']) && $_GET['length'] > 0)
		$length = $_GET['length'];
	else
		$length = PASS_LENGTH;

	$secret = computeHash($password = randomPassword($length));

	if(getIdFromHash($secret))	// if hash already in db, complain
		echo WRONG_PASS;
	else						// else show password and create address
		echo newAddress($secret).';'.$password.';';
?>

