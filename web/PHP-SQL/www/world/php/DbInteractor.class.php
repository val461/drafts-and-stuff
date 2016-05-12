<?php
namespace val\world;

	require_once $_SERVER['DOCUMENT_ROOT'].'/val/world/php/constants.php';
	require_once ROOT.'/val/world/php/Database.class.php';

	class DbInteractor
	{
		protected $db;
		
		public function __construct(Database $db = NULL)	// A PARAMETER SHOULD BE SPECIFIED OR GLOBAL VARIABLE $db WILL BE USED INSTEAD
		{
			if(isset($db))
				$this->setDb($db);
			else
				$this->globalDb();
		}

		public setDb(Database $db)
		{
			$this->db = $db;
		}

		public globalDb()
		{
			global $db;
			$this->setDb($db);
		}
	}

