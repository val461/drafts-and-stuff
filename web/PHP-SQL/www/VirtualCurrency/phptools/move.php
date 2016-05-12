<?php
	include_once($_SERVER['DOCUMENT_ROOT'].'/val/VirtualCurrency/phptools/constants.php');
	include_once(ROOT.'phptools/move/sql.php');
	include_once(ROOT.'phptools/consult.php');
	include_once(ROOT.'phptools/crypt.php');
	include_once(ROOT.'phptools/fees.php');

	function moveAmount($from, $to, $amount, $password)
	// Returns either moved amount or negative value if error
	{
		// Basic tests over $amount
		if($amount == 0)
			return 0;
		if($amount < 0)
			return moveAmount($to, $from, -$amount, $password);
		if($from < 1)
			return GIVER_NOT_EXIST;
		if($to < 1)
			return RECEIVER_NOT_EXIST;
	
		// Check existence and amounts on addresses	
		$amounts = getAmountsFromIds([$from, $to]);
		if($amounts[$from] < 0)
			return GIVER_NOT_EXIST;
		if($amounts[$from] == 0)
			return NO_MONEY;
		if($amounts[$to] < 0)
			return RECEIVER_NOT_EXIST;
	
		// Check if password is correct
		if(!password_verify($password, getSecretFromId($from))
			return WRONG_PASS;
	
		$fees = 0;
		// Calculate new amounts
		if($amount >= $amounts[$from])	// if amount too big, empty giving address
		{
			$amount = $amounts[$from];
			$fees = $amount * FEE_PERCENTAGE_PER_TRANSACTION;
			$amounts[$from] = 0;
		}
		else
		{
			$fees = $amount * FEE_PERCENTAGE_PER_TRANSACTION;
			$amounts[$from] -= arrondiExces($amount + $fees);
		}
		
		$amounts[$to] += arrondiDefaut($amount - $fees);
	
		// Record new amounts in db
		setAmounts($amounts);
		tmpFeesStorage($fees);
	
		return $amount;
	}

