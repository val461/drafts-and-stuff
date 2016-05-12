<?php
namespace val\world\gameclasses;

	require_once ROOT.'/val/world/php/DbInteractor.class.php';

	class Being extends DbInteractor
	{
		protected $name;
		protected $picture;

/*		public function __construct()
		{
			parent::__construct();
		}
*/
		public setName		($name)						{$this->name	= htmlspecialchars((string) $name);}
		public setPicture	($url)						{$this->picture	= htmlspecialchars((string) $url);}
	}

