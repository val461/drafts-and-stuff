<?php
include_once($_SERVER['DOCUMENT_ROOT'].'/val/VirtualCurrency/phptools/constants.php');
include_once(ROOT.'phptools/sql.php');
include_once(ROOT.'phptools/consult.php');

function getSecretsFromIds($ids)
{
	foreach($ids as $id)
		$secrets[$id] = getSecretFromId($id);
	return $secrets;
}

function getSecretFromId($id)
{
	global $bdd;
	
	$id = (int) $id;
	$secret = NOT_FOUND;	// default value
	
	if($id >= 0)
	{
		$req = 'SELECT `secret` FROM `addresses` WHERE `id` = ?';
		$req = $bdd->prepare($req);
		$req->execute(
			[
				$id
			]);
		
		if($donnees = $req->fetch())
			$secret = $donnees['secret'];
		
		$req->closeCursor();
	}
	
	return $secret;
}

function setAmounts($amounts)
{
	foreach($amounts as $id => $amount)
		setAmount($amount, $id);
}

function setAmount($amount, $id)
{
	global $bdd;
	
	$amount = (float) $amount;
	$id = (int) $id;
	
	if(getAmountFromId($id) >= 0)	// if address is in use
	{
		$req = 'UPDATE `addresses` SET `amount` = ? WHERE `id` = ?';
		$req = $bdd->prepare($req);
		$req->execute(
			[
				$amount,
				$id
			]);
	}
}

