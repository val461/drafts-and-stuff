<?php
include_once($_SERVER['DOCUMENT_ROOT'].'/val/VirtualCurrency/phptools/constants.php');
include_once(ROOT.'phptools/sql.php');

function deleteIds($ids)
{
	foreach($ids as $id)
		deleteId($id);
}

function deleteId($id)
{
	global $bdd;
	
	$req = 'DELETE FROM `addresses` WHERE `id` = ?';
	$req = $bdd->prepare($req);
	$req->execute(
		[
			(int) $id
		]);
}

function getNumberOfShares($id)
{
	global $bdd;
	$id = (int) $id;
	
	$shares = 0;
	$error = 0;	// 0 means no error
	
	if($id >= 0)
	{
		$req = 'SELECT `shares` FROM `addresses` WHERE `id` = ?';
		$req = $bdd->prepare($req);
		$req->execute(
			[
				$id
			]);
		
		if($donnees = $req->fetch())
			$shares = (int) $donnees['shares'];
		else
			$error = NOT_FOUND;
		
		$req->closeCursor();
	}
	else
		$error = NOT_FOUND;
	
	return ['shares' => $shares, 'error' => $error];
}

function setNumberOfShares($shares, $id)
{
	global $bdd;
	
	$shares = (int) $shares;
	$id = (int) $id;
	
	if(getAmountFromId($id) >= 0)	// if address is in use
	{
		$req = 'UPDATE `addresses` SET `shares` = ? WHERE `id` = ?';
		$req = $bdd->prepare($req);
		$req->execute(
			[
				$shares,
				$id
			]);
	}
}

