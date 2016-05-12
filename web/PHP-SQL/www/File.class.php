<?php
namespace val
{
	interface ClassFile
	{
		public function setPath($path);
		public function getPath();
		public function delete();
		public function create();
		public function readCharacter();
		public function readLine();
		public function write();
		public function exists();
	}
	
	class File implements ClassFile // TODO
	{
		protected $path;
		protected $handle;
		
		public function __construct($path)
		{
			$this->setPath($path);
		}
		
		public function __toString()
		{
			return $this->getPath();
		}
		
		public function setPath($path)
		{
			$this->path = (string) $path;
		}
		
		public function getPath()
		{
			return $this->path;
		}
		
		public function delete()
		{
			
		}
		
		public function create()
		{
			
		}
		
		public function readCharacter()
		{
			
		}
		
		public function readLine()
		{
			
		}
		
		public function write()
		{
			
		}
		
		public function exists()
		{
			return \file_exists($this->getPath());
		}
	}
}

