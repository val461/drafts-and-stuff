<?php
	include_once($_SERVER['DOCUMENT_ROOT'].'/val/VirtualCurrency/phptools/constants.php');
	include_once(ROOT.'phptools/sql.php');

	function getPayers()
	{
		global $bdd;
	
		$req = 'SELECT `id`,`amount`,`shares` FROM `addresses` WHERE `id` > 0 AND `shares` < 0 AND `amount` > 0';
		$req = $bdd->query($req);
	
		while($donnees = $req->fetch())
		{
			$payers[$donnees['id']]['amount'] = $donnees['amount'];
			$payers[$donnees['id']]['shares'] = $donnees['shares'];
		}
	
		$req->closeCursor();
	
		return $payers;
	}

	function getReceivers()
	{
		global $bdd;
	
		$req = 'SELECT `id`,`amount`,`shares` FROM `addresses` WHERE `shares` > 0 AND `amount` >= 0';
		$req = $bdd->query($req);
	
		while($donnees = $req->fetch())
		{
		//	$receivers[] = $donnees;
		
			$receivers[$donnees['id']]['amount'] = $donnees['amount'];
			$receivers[$donnees['id']]['shares'] = $donnees['shares'];
		}
	
		$req->closeCursor();
	
		return $receivers;
	}

	function getIds()	// Returns a particular array of receivers, used by addUnitsToRandomId() in fees.php
	{
		global $bdd;
	
		$req = 'SELECT `id`,`shares` FROM `addresses` WHERE `shares` > 0 AND `amount` >= 0';
		$req = $bdd->query($req);
	
		while($donnees = $req->fetch())
		{
			for($i = 0; $i < $donnees['shares']; $i++)	// duplicate ids as much as owned shares
				$ids[] = $donnees['id'];
		}
	
		$req->closeCursor();
	
		return $ids;
	}

