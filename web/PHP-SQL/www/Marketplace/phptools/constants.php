<?php
$arr =	[
			// Parameters
//			'' => '',
			// Misc.
			'ROOT' => $_SERVER['DOCUMENT_ROOT'].'/val/Marketplace',
			'DOMAIN' => $_SERVER['HTTP_HOST'].'/val',
			// Errors
			'GIVER_NOT_EXIST' => -1,
			'RECEIVER_NOT_EXIST' => -2,
			'NO_MONEY' => -3,
			'WRONG_PASS' => '-4',
			'MISSING_PARAMETER' => -5,
			'LOCKED' => -6,
			'NOT_FOUND' => -7
		];

// Constants definition
foreach($arr as $constant => $value)
	define($constant, $value);

