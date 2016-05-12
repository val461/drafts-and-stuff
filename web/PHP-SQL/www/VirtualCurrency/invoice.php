<!DOCTYPE html>
<html>
	<head>
		<meta http-equiv="content-type" content="text/html;charset=utf-8" />
		<title>Invoice generator</title>
	</head>
	<body>
<?php
	include_once('links.php');
	
	// set by POST ? else set default
	$from = isset($_POST['from'])?$_POST['from']:'');
	$to = isset($_POST['to'])?$_POST['to']:'');
	$amount = isset($_POST['amount'])?((float) $_POST['amount']):'');
	$link = '';
	
	if($_POST != [])
	{
		$baseURL = 'http://'.DOMAIN.'/';
	}
?>
		<h2>Generate an invoice</h2>
		<p>
			All fields are facultative. Clicking on button &quot;Generate&quot; will produce a URL that you can then give to your client.
		</p>
		<form method="post">
			<table>
				<tr>
					<td>
						Giving address:<br/>
						<input type="text" name="from" value="<?php echo $from; ?>" onClick="this.setSelectionRange(0, this.value.length)" />
					</td>1
					<td>
						Receiving address:<br/>
						<input type="text" name="to" value="<?php echo $to; ?>" onClick="this.setSelectionRange(0, this.value.length)" />
					</td>
				</tr>
			</table>
			<p>
				Amount of units:<br/>
				<input type="text" name="amount" value="<?php echo $amount; ?>" onClick="this.setSelectionRange(0, this.value.length)" />
			</p>
			<p>
				<input type="submit" value="Generate" />
			</p>
		</form>
	</body>
</html>

