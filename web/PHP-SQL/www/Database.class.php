<?php
namespace val
{
	interface ClassDatabase
	{
		public function connect($user, $password, $host, $dbName);
		public function readingQuery($query);
		public function writingQuery($query);
	}

	class MySqlDatabase implements ClassDatabase
	{
		protected $db		= NULL;
		protected $user		= 'root';
		protected $password	= '';
		protected $host		= 'localhost';
		protected $dbName	= '';

		public function __construct($host = NULL, $dbName = NULL, $user = NULL, $password = NULL)
		{
			$this->connect($host, $dbName, $user, $password);
		}

		public function connect($host = NULL, $dbName = NULL, $user = NULL, $password = NULL)
		{
			if(isset($host))
				$this->setHost($host);
			if(isset($dbName))
				$this->setDbName($dbName);
			if(isset($user))
				$this->setUser($user);
			if(isset($password))
				$this->setPassword($password);
			
			$this->setHandle(new \PDO('mysql:host=' . $this->host . ';dbname=' . $this->dbName, $this->user, $this->password));
		}

		public function readingQuery($query)
		{
			
		}

		public function writingQuery($query)
		{
			
		}

		public function setHost		($host)		{$this->host		= (string) $host;		}
		public function setDbName	($dbName)	{$this->dbName		= (string) $dbName;		}
		public function setUser		($user)		{$this->user		= (string) $user;		}
		public function setPassword	($password)	{$this->password	= (string) $password;	}
		public function setHandle	(\PDO $db)	{$this->db			= $db;					}
		public function getHandle	()			{return $this->db;							}
	}
}

