<?php
	include_once($_SERVER['DOCUMENT_ROOT'].'/val/VirtualCurrency/phptools/constants.php');

	if(isset($_GET['id']))
	{
		include_once(ROOT.'phptools/consult.php');
		echo getAmountFromId($_GET['id']);
	}
	else
		echo MISSING_PARAMETER;
?>

