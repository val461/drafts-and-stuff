<!DOCTYPE html>
<html>
	<head>
		<meta http-equiv="content-type" content="text/html;charset=utf-8" />
		<title>Consult amount on an address</title>
	</head>
	<body>
<?php include_once('links.php'); ?>
		<h2>Check an address</h2>
<?php
	$id = isset($_GET['id'])?$_GET['id']:'';
?>
		<form method="get">
			<input type="text" name="id" value="<?php echo $id ?>" onClick="this.setSelectionRange(0, this.value.length)" /><input type="submit" value="Check" />
		</form>
<?php
	if(isset($_GET['id']))
	{
?>
		<p>
			Address:
		</p>
		<p>
<?php
		echo $id;
?>
		</p>
		<p>
			Amount (in units):
		</p>
		<p>
<?php
		include_once($_SERVER['DOCUMENT_ROOT'].'/val/VirtualCurrency/phptools/constants.php');
		include_once(ROOT.'phptools/consult.php');
		
		if(($amount = getAmountFromId($id)) >= 0)
			echo $amount;
		else
			echo 'Address is currently not in use.';
?>
		</p>
<?php
	}
?>
	</body>
</html>

