<?php
include_once($_SERVER['DOCUMENT_ROOT'].'/val/VirtualCurrency/phptools/constants.php');

function computeHash($data)
{
	return password_hash($data, PASSWORD_DEFAULT, ['cost' => HASH_COST]);
}

function randomPassword($length = PASS_LENGTH)
{
	$length = (int) $length;
	$password = '';
	$alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
	$max = strlen($alphabet);
	
	for($i = 0; $i < $length; $i++)
		$password .= $alphabet[randomInRange(0, $max)];
	
	return $password;
}

function randomInRange($min, $max)	// max excluded
{
	do	// $rand == $max is less likely that any other value (due to floor), so $max is excluded for a better equiprobability
	{
	    $rand = ($min + floor(($max-$min)*(randomNumber()/0xffffffff)));
	} while($rand >= $max);
	return (int) $rand;
}

function randomNumber()	// random 32bit int
{
	return hexdec(bin2hex(openssl_random_pseudo_bytes(4)));
}
