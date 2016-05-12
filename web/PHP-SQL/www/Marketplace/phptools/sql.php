<?php
	$sqlUser = 'root';
	$sqlPassword = 'wertakis';
	
	try
	{
		$pdo_options[PDO::ATTR_ERRMODE] = PDO::ERRMODE_EXCEPTION;
		$bdd = new PDO('mysql:host=localhost;dbname=virtualcurrency', $sqlUser, $sqlPassword, $pdo_options);
	}
	catch (Exception $e)
	{
		die('Erreur : ' . $e->getMessage());
	}

