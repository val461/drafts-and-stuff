<?php
include_once($_SERVER['DOCUMENT_ROOT'].'/val/VirtualCurrency/phptools/constants.php');
include_once(ROOT.'phptools/sql.php');

function newAddress($secret)
{
	global $bdd;
	
	$req = 'INSERT INTO `addresses` (`secret`) VALUES (?)';
	$req = $bdd->prepare($req);
	$req->execute(
		[
			$secret
		]);
	
	return getIdFromHash($secret);	// try to find id using hash to see if it was correctly set
}

function setPassword($secret, $id)
{
	global $bdd;
	
	$req = 'UPDATE `addresses` SET `secret` = ? WHERE `id` = ?';
	$req = $bdd->prepare($req);
	$req->execute(
		[
			$secret,
			(int) $id
		]);
	
	return getIdFromHash($secret);
}

function getIdsFromHashes($secrets)
{
	foreach($secrets as $secret)
		$ids[$secret] = getIdFromHash($secret);
	return $ids;
}

function getIdFromHash($secret)
{
	global $bdd;
	$id = NOT_FOUND;	// default value
	
	$req = 'SELECT `id` FROM `addresses` WHERE `secret` = ? ORDER BY `id` DESC LIMIT 0,1';
	$req = $bdd->prepare($req);
	$req->execute(
		[
			$secret
		]);
	
	if($donnees = $req->fetch())
		$id = (int) $donnees['id'];
	
	$req->closeCursor();
	
	return $id;
}

