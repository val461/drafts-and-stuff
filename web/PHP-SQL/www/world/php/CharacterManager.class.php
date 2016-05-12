<?php
namespace val\world;

	require_once $_SERVER['DOCUMENT_ROOT'].'/val/world/php/constants.php';
	require_once ROOT.'/val/world/php/DbInteractor.class.php';
	require_once ROOT.'/val/world/english/php/gameclasses.php';

	interface ClassCharacterManager
	{
		public function add				($name);
		public function delete			($name);
		public function exists			($name);

		public function changeName		($name, $newName);
		public function changePassword	($name, $password);

		public function load			($name, $password);
		public function save			($name, gameclasses\Being\Character $character);
	}

	class CharacterManager extends DbInteractor implements ClassCharacterManager
	{
/*		public function __construct()
		{
			parent::__construct();
		}
*/
		public function add($name)
		{
			
		}

		public function delete($name)
		{
			
		}

		public function exists($name)
		{
			
		}


		public function changeName($name, $newName)
		{
			$newName = htmlspecialchars((string) $newName);

			if($db->characters->exists($newName))
				return false;
			else
			{// name available
				// register in db
				// ...
				return true;
			}
		}
		public function changePassword	($name, $password);

		public function load($name, $password);
		public function save($name, gameclasses\Being\Character $character);
	}

