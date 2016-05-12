<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html>
	<head>
		<meta http-equiv="content-type" content="text/html;charset=utf-8" />
		<title>World</title>
	</head>
	<body>
<?php
	require_once $_SERVER['DOCUMENT_ROOT'].'/val/world/english/php/constants.php';
	require_once IROOT.'/php/loginform.php';
	
	if($action == 'log_in')
	{
		require_once IROOT.'/php/load.php';
	}
	else if($action == 'new_character')
	{
		require_once IROOT.'/php/new.php';
	}
?>
	</body>
</html>

