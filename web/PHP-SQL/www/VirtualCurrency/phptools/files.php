<?php

function fileOverwrite($filePath, $newValue)
{
	// file is created if it does not exist
	$file = fopen($filePath, 'w');
	fputs($file, $newValue);
	fclose($file);
}

function fileRead($filePath)
{
	$file = fopen($filePath, 'r');
	$value = fgets($file);
	fclose($file);
	return $value;
}

function createFile($filePath)
{
	return fclose(fopen($filePath, 'w'));
}

