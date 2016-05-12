<?php
namespace val\world\gameclasses;

	interface ClassLocation
	{
		
	}
	
	class Location implements ClassLocation
	{
		protected $name = '';
		protected $picture = '';

		protected $planet = '';
		protected $continent = '';
		protected $country = '';
		protected $city = '';
		protected $street = '';
		protected $place = '';

		public setName		($name)	{$this->name	= htmlspecialchars((string) $name);}
		public setPicture	($url)	{$this->picture	= htmlspecialchars((string) $url);}
	}

