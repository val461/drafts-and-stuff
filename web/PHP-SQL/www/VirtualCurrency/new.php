<!DOCTYPE html>
<html>
	<head>
		<meta http-equiv="content-type" content="text/html;charset=utf-8" />
		<title>Open a new address</title>
	</head>
	<body>
<?php include_once('links.php'); ?>
		<h2>Open a new address</h2>
<?php
	include_once($_SERVER['DOCUMENT_ROOT'].'/val/VirtualCurrency/phptools/constants.php');
	
	if(isset($_POST['length']) && $_POST['length'] > 0)
		$length = $_POST['length'];
	else
		$length = PASS_LENGTH;
	
	if(isset($_POST['length']))
	{
		include_once(ROOT.'phptools/crypt.php');
		include_once(ROOT.'phptools/new.php');
		
		$secret = computeHash($password = randomPassword($length));
		
		if(getIdFromHash($secret))	// if hash already in db, complain
		{
			echo 'Error '.WRONG_PASS.': The password that was generated is already in use; please try a longer password length.';
			$length = PASS_LENGTH;
		}
		else						// create address and show relevant information
		{
			$id = newAddress($secret);
			if($id > 0)
			{
?>
		<p>
			Address:<br/>
			<input type="text" value="<?php echo $id; ?>" onClick="this.setSelectionRange(0, this.value.length)" />
		</p>
		<p>
			Password:
		</p>
		<textarea onClick="this.setSelectionRange(0, this.value.length)"><?php echo $password; ?></textarea>
<?php
			}
			else
				echo 'Error '.$id.': the address couldn\'t be created.';
?>
<?php
		}
	}
?>
		<form method="post">
			<p>
				Password length:<br/>
				<input type="text" name="length" value="<?php echo $length ?>" onClick="this.setSelectionRange(0, this.value.length)" /><input type="submit" value="Create new address" />
			</p>
		</form>
	</body>
</html>

