<?php
	include_once($_SERVER['DOCUMENT_ROOT'].'/val/VirtualCurrency/phptools/constants.php');

	if(isset($_POST['from']) && isset($_POST['to']) && isset($_POST['amount']) && isset($_POST['pass']))
	{
		include_once(ROOT.'phptools/move.php');
	
		$from = $_POST['from'];
		$to = $_POST['to'];
		$amount = $_POST['amount'];
		$password = $_POST['pass'];
	
		echo moveAmount($from, $to, $amount, $password);
	}
	else
		echo MISSING_PARAMETER;
?>

