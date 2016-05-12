<?php
	include_once($_SERVER['DOCUMENT_ROOT'].'/val/VirtualCurrency/phptools/constants.php');
	include_once(ROOT.'phptools/files.php');
	include_once(ROOT.'phptools/move/sql.php');
	include_once(ROOT.'phptools/fees/sql.php');
	include_once(ROOT.'phptools/consult.php');

	$dateFilePath = ROOT.'data/lastcollection.txt';

	function feeCollection()
	{
		if(!lock())
			return LOCKED;
		
		$feePercentage = feePercentage();
		if($feePercentage >= 0.01)
		{
			$fees = collect(feePercentage());
			recordTimeOfFeeCollection();
		}
		else
			$fees = 0;	// avoid processing fees till percentage gets high enough
		
		unlock();
		
		return $fees;
	}

	function lock()
	{
		$lock = ROOT.'data/LOCK';
		if(file_exists($lock))	// already locked; wait.
			return false;
		return createFile($lock);
	}

	function unlock()
	{
		$lock = ROOT.'data/LOCK';
		if(!file_exists($lock))	// no lock to remove.
			return true;
		return unlink($lock);
	}

	function feePercentage()
	{
		return FEE_PERCENTAGE_PER_INTERVAL / FEE_INTERVAL * timeSinceLastFeeCollection();
	}

	function collect($feePercentage)
	{
		$total = 0;
		$payers = getPayers();
		foreach($payers as $id => $payer)
		{
			$fee = $feePercentage * -$payer['shares'] * $payer['amount'];
			$newAmount = $payer['amount'] - arrondiExces($fee);
			if($newAmount < 0)	// if not enough money to pay the fee
			{
				$fee = $payer['amount'];
				$newAmount = 0;	// empty the address
			}
			$total += arrondiDefaut($fee);
			setAmount($newAmount, $id);
		}
		
		// Process leftovers from previous collections, stored on address 0 (see function pay($fees))
		$total += getAmountFromId(ADMIN);
		setAmount(0, ADMIN);
		
		return $total;
	}

	function pay($fees)
	{
		$receivers = getReceivers();
		$numberOfShares = sumOfShares($receivers);
		$shareValue = arrondiDefaut($fees / $numberOfShares);
	
		if($shareValue < 0.001)		// Too few to share
		{
			if($fees >= 0.001)		// But enough for one
			{
				tmpFeesStorage($fees);
				return $fees;
			}
			return 0;	// or not enough for any
		}
		
		$remainder = $fees - $shareValue*$numberOfShares;
	
		foreach($receivers as $id => $receiver)
		{
			$newAmount = $receiver['amount'] + $shareValue*$receiver['shares'];
			setAmount($newAmount, $id);
		}
		
		if($remainder > 0)
			pay($remainder);
		
		return $fees;
	}

	function sumOfShares($receivers)
	{
		$sum = 0;
		foreach($receivers as $receiver)
			$sum += $receiver['shares'];
		return $sum;
	}

	function tmpFeesStorage($fees)
	{
		$currentAmount = getAmountFromId(ADMIN);
		$newAmount = $currentAmount + $fees;
		setAmount($newAmount, ADMIN);
	}
/*
	function addUnitsToRandomId($units)	// pay fees (that are yet undistributed because of rounding errors) to share owners
	{									// their chance to get the fees is proportionate to the number of shares they own
		$receivers = getReceivers();
		$ids = getIds();
	
		$randomNumber = rand(0, count($ids)-1);
		$randomId = $ids[$randomNumber];
		$randomReceiver = $receivers[$randomId];
	
		$newAmount = $units + $randomReceiver['amount'];
		setAmount($newAmount, $randomReceiver['id']);
	
		echo "\n".'Remainder management: added '.$units.' units to id '.$randomId.' which contained '.$randomReceiver['amount']." units.\n";
	}
*/
	function arrondiDefaut($n)
	{
		return floor($n*1000) / 1000;
	}

	function arrondiExces($n)
	{
		return ceil($n*1000) / 1000;
	}
	
	function recordTimeOfFeeCollection()
	{
		global $dateFilePath;
		fileOverwrite($dateFilePath, time());
	}

	function timeSinceLastFeeCollection()
	{
		return time() - dateOfLastFeeCollection();
	}

	function dateOfLastFeeCollection()
	{
		global $dateFilePath;
		$lastFeeCollection = (int) fileRead($dateFilePath);
		if(!$lastFeeCollection)	// first fee collection
		{
			recordTimeOfFeeCollection();	// create file
			return time();					// collect nothing this time
		}
		return $lastFeeCollection;
	}

