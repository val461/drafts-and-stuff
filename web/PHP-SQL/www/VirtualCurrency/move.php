<!DOCTYPE html>
<html>
	<head>
		<meta http-equiv="content-type" content="text/html;charset=utf-8" />
		<title>Move money to an address</title>
	</head>
	<body>
<?php
	include_once('links.php');
	
	// set by POST ? else set by GET ? else nothing set
	$from = isset($_POST['from'])?$_POST['from']:(isset($_GET['from'])?$_GET['from']:'');
	$to = isset($_POST['to'])?$_POST['to']:(isset($_GET['to'])?$_GET['to']:'');
	$amount = isset($_POST['amount'])?((float) $_POST['amount']):(isset($_GET['amount'])?((float) $_GET['amount']):'');
	// One should NOT send his password with method GET, for security reasons
	$password = isset($_POST['password'])?$_POST['password']:(isset($_GET['password'])?$_GET['password']:'');
	
	if($from)
	{
		function wrongParam($field)
		{
			echo 'Request could not be satisfied, it seems that field "'.$field.'" was not correctly filled.<br/>';		
		}
		
		if($to)
		{
			if($amount != NULL)
			{
				if($password)
				{
					include_once($_SERVER['DOCUMENT_ROOT'].'/val/VirtualCurrency/phptools/constants.php');
					include_once(ROOT.'phptools/move.php');
					
					if($amount < 0)
						wrongParam('Amount');
					else
					{
						$moved = moveAmount($from, $to, $amount, $password);
						if($moved < 0)
							switch($moved)
							{
								case GIVER_NOT_EXIST:
									wrongParam('Giving address');
									break;
								case RECEIVER_NOT_EXIST:
									wrongParam('Receiving address');
									break;
								case NO_MONEY:
									echo 'Request could not be satisfied, because no money is associated to the giving address.<br/>';
									break;
								case WRONG_PASS:
									wrongParam('Password');
									break;
								default:
									echo 'An unknown error happened.';	// This code is not supposed to ever be reached.
									break;
							}
						else
							echo 'Amount moved: '.$moved.' from '.$from.' to '.$to.'<br/>';
					}
				}
				else
					wrongParam('Password');
			}
			else
				wrongParam('Amount');
		}
		else
			wrongParam('Receiving address');
	}
?>
		<h2>Move units between addresses</h2>
		<p>
			Please be careful, you will not be prompted for confirmation after clicking on Proceed. Specifying a bigger amount than what is available on the giving address will move all funds available onto the receiving address.
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
				Password of giving address:
			</p>
			<input type="password" name="pass" value="<?php echo $password; ?>" onClick="this.setSelectionRange(0, this.value.length)">
			<p>
				<input type="submit" value="Proceed" />
			</p>
		</form>
	</body>
</html>

