<?php
include_once($_SERVER['DOCUMENT_ROOT'].'/val/VirtualCurrency/phptools/constants.php');
include_once(ROOT.'phptools/sql.php');

function getAmountsFromIds($ids)
{
	foreach($ids as $id)
		$amounts[$id] = getAmountFromId($id);
	return $amounts;
}

function getAmountFromId($id)
{
	global $bdd;
	
	$id = (int) $id;
	$amount = NOT_FOUND;	// default value
	
	if($id >= 0)
	{
		$req = 'SELECT `amount` FROM `addresses` WHERE `id` = ?';
		$req = $bdd->prepare($req);
		$req->execute(
			[
				$id
			]);
		
		if($donnees = $req->fetch())
			$amount = (float) $donnees['amount'];
		
		$req->closeCursor();
	}
	
	return $amount;
}

