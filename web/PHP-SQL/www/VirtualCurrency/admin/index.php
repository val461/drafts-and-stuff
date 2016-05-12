<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html>
	<head>
		<meta http-equiv="content-type" content="text/html;charset=utf-8" />
		<title>Administration page &mdash; Restricted to private access only</title>
	</head>
	<body>
<?php 
	include_once($_SERVER['DOCUMENT_ROOT'].'/val/VirtualCurrency/phptools/constants.php');
	include_once(ROOT.'/links.php');
?>
		<h2>Administration page</h2>
<?php
	if(isset($_POST['password']))
	{
		include_once(ROOT.'/phptools/move/sql.php');
		include_once(ROOT.'/phptools/crypt.php');
		
		$password = $_POST['password'];
		
		if(password_verify($password, getSecretFromId(ADMIN)))	// if correct admin password
		{
			$id = -1;	// default value
			
			if(isset($_POST['changepassword']))
			{
				include_once(ROOT.'/phptools/new.php');
				
				$secret = computeHash($password = randomPassword());
				
				if(getIdFromHash($secret) >= 0)	// if hash already in db, complain
					echo 'Error '.WRONG_PASS.': the generated password is already in use; please try a longer password length.';
				else							// else create address and show relevant information
				{
					$id = setPassword($secret, ADMIN);
					if($id >= 0)
					{
?>
		<p>
			Address (should be 0):<br/>
			<input type="text" value="<?php echo $id; ?>" onClick="this.setSelectionRange(0, this.value.length)" />
		</p>
		<p>
			New password:
		</p>
		<textarea onClick="this.setSelectionRange(0, this.value.length)"><?php echo $password; ?></textarea>
<?php
					}
					else
						echo 'Error '.$id;
				}
			}
			else if(isset($_POST['id']) && $_POST['id'] != '')
			{
				include_once(ROOT.'/phptools/consult.php');
		
				$id = (int) $_POST['id'];
				$currentAmount = getAmountFromId($id);
		
				if($currentAmount >= 0)	// if address is in use
				{
					if(isset($_POST['delete']) && $id > ADMIN)	// ADMIN shouldn't be deleted
					{
						if($currentAmount <= 0)
						{
							include_once(ROOT.'/phptools/admin.php');
							echo 'Deleting address';
							deleteId($id);
						}
						else
							echo 'Address was not deleted because amount is not empty.';
					}
					else if(isset($_POST['addshares']))
					{
						include_once(ROOT.'/phptools/admin.php');
						
						$result = getNumberOfShares($id);
						if($result['error'] == 0)	// if no error
						{
							$currentAmount = $result['shares'];
?>
		<p>
			Address <i><?php echo $id; ?></i><br/>
			Current number of share(s): <i><?php echo $currentAmount; ?></i>
		</p>
<?php
							if(isset($_POST['shares']) && $_POST['shares'] != '')
							{
								$newAmount = $currentAmount + (int) $_POST['shares'];
?>
		<p>
			Setting number of shares to <i><?php echo $newAmount; ?></i> share(s)
			(adding <?php echo ($newAmount - $currentAmount); ?> share(s))
?>
		</p>
<?php
								setNumberOfShares($newAmount, $id);
?>
		<p>
			New amount: <i><?php echo getNumberOfShares($id)['shares']; ?></i> share(s).
		</p>$str$str
<?php
							}
						}
						else
						{
?>
		<p>
			Error, nothing was done because ID wasn't found in database.
		</p>
<?php
						}
					}
					else if(isset($_POST['amount']))
					{
						$amount = (float) $_POST['amount'];
			
						if(isset($_POST['add']))
						{
							$newAmount = $currentAmount + $amount;
							$action = 'Adding <i>'.$amount.'</i> unit(s)';
						}
						else if(isset($_POST['rem']))
						{
							if($amount < $currentAmount)
							{
								$newAmount = $currentAmount - $amount;
								$action = 'Removing <i>'.$amount.'</i> unit(s)';
							}
							else
							{
								$newAmount = 0;
								$action = 'Emptying '.$id;
							}
						}
						else if(isset($_POST['empty']))
						{
							$newAmount = 0;
							$action = 'Emptying '.$id;
						}
						else
						{
							$newAmount = $currentAmount;
							$action = 'Error: action not understood.';
						}
?>
		<p>
			Address <i><?php echo $id; ?></i><br/>
			Current amount: <i><?php echo $currentAmount; ?></i> unit(s)
		</p>
		<p>
			<?php echo $action; ?><br/>
			Setting amount to <i><?php echo $newAmount; ?></i> unit(s)
		</p>
<?php
						setAmount($newAmount, $id);
?>
		<p>
			New amount: <i><?php echo getAmountFromId($id); ?></i> unit(s).
		</p>
<?php
					}
					else
					{
?>
		<p>
			Error, nothing was done because action was not understood.
		</p>
<?php
					}
				}
				else
				{
?>
		<p>
			Error, nothing was done because ID was not found in database.
		</p>
<?php
				}
			}
?>
		<hr/>
		<form method="post">
			<p>
				Id:<br/>
				<input type="text" name="id" value="<?php if($id >= 0) echo $id; ?>" onClick="this.setSelectionRange(0, this.value.length)" />
			</p>
			<p>
				Amount of unit(s):<br/>
				<input type="text" name="amount" onClick="this.setSelectionRange(0, this.value.length)" />
			</p>
			<p>
				Number of share(s):<br/>
				<input type="text" name="shares" onClick="this.setSelectionRange(0, this.value.length)" />
			</p>
			<p>
				<input type="submit" name="add" value="Add unit(s)" /><input type="submit" name="rem" value="Remove unit(s)" />
			</p>
			<p>
				<input type="submit" name="empty" value="Empty address (set amount to 0 unit)" />
			</p>
			<p>
				<input type="submit" name="addshares" value="Add share(s) (use a negative value for removal)" />
			</p>
			<p>
				<input type="submit" name="delete" value="Delete address (address must already be empty before deletion)" />
			</p>
			<p>
				Current admin password:<br/>
				<input type="password" name="password" value="<?php echo $password; ?>" onClick="this.setSelectionRange(0, this.value.length)" /><br/>
				<input type="submit" name="changepassword" value="Change admin password" />
			</p>
		</form>
<?php
		}
		else	// wrong password
		{
?>
		<p>
			Wrong password.
		</p>
<?php
		}
	}
	else	// if no password
	{
?>
		<form method="post">
			<p>
					Password:<br/>
					<input type="password" name="password" onClick="this.setSelectionRange(0, this.value.length)" /><br/>
					<input type="submit" value="Login" />
			</p>
		</form>
<?php
	}
?>
	</body>
</html>

