<?php
namespace val\world;

	require_once $_SERVER['DOCUMENT_ROOT'].'/val/world/php/constants.php';
	require_once ROOT.'/val/Database.class.php';
	require_once ROOT.'/val/world/php/CharacterManager.class.php';

	interface ClassDatabase extends \val\ClassDatabase
	{
		
	}

	class Database extends \val\MySqlDatabase implements ClassDatabase
	{
		public $characters;
		
		public __construct()
		{
			$this->characters = new CharacterManager($this);
		}
	}

