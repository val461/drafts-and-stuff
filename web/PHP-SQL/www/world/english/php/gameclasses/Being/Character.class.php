<?php
namespace val\world\gameclasses\Being;
use val\world\gameclasses as gameclasses;

	require_once ROOT.'/val/world/english/php/gameclasses.php';

	interface ClassCharacter extends gameclasses\ClassBeing
	{
		
	}
	
	class Character extends gameclasses\Being implements ClassCharacter
	{
		public function __destruct()
		{
			$db->characters->save($this->getName(), $this);
		}

		public function setName($name)	
		{
			$name = htmlspecialchars((string) $name);

			if($this->db->characters->changeName($this->getName(), $name))
			{
				$this->name	= $name;
				return true;
			}
			else
				return false;
		}

		public function getName()	{return $this->name;}
	}

