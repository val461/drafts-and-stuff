<?php
	include_once($_SERVER['DOCUMENT_ROOT'].'/val/VirtualCurrency/phptools/constants.php');

	if(isset($_GET['from']) && isset($_GET['to']) && isset($_GET['amount']) && isset($_GET['pass']))
	{
		include_once(ROOT.'phptools/move.php');
	
		$from = $_GET['from'];
		$to = $_GET['to'];
		$amount = $_GET['amount'];
		$password = $_GET['pass'];
	
		echo moveAmount($from, $to, $amount, $password);
	}
	else
		echo MISSING_PARAMETER;
?>

