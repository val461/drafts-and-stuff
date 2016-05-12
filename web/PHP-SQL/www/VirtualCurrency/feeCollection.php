<!DOCTYPE html>
<html>
	<head>
		<meta http-equiv="content-type" content="text/html;charset=utf-8" />
		<title>Fee collection</title>
	</head>
	<body>
<?php
	include_once($_SERVER['DOCUMENT_ROOT'].'/val/VirtualCurrency/phptools/constants.php');
	include_once(ROOT.'/links.php');
	include_once(ROOT.'/phptools/fees.php');
?>
		<h2>Launch fee collection</h2>
		<pre>
<?php
//	$before = getReceivers();
	$fees = feeCollection();
	if($fees >= 0)
	{
/*DEBUG		$after = getReceivers();
		
		if(count($before) == count($after))
		{
			foreach($before as $id => $receiver)
			{
				$before[$id]['moved'] = $after[$id]['amount'] - $before[$id]['amount'];
			}
			print_r($before);*/
?>
		</pre>
		<p>
			<?php echo $fees; ?> units were collected.
		</p>
<?php
/*		}
		else
		{
			echo "arrays not the same size:\n";
			print_r($before);
			print_r($after);
		}
*/	}
	else
		echo 'Error, nothing happened because server is locked (error '.$fees.')';
?>
		</pre>
	</body>
</html>

