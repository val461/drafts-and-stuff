<?php
$arr =	[
			// Parameters
			'FEE_PERCENTAGE_PER_TRANSACTION' => 0.001,	// 0.1%, this fee is distributed between shareholders
			'FEE_PERCENTAGE_PER_INTERVAL' => 0.01,		// 1%, this fee is not distributed to any shareholder but accounts for storage fees
			'FEE_INTERVAL' => 30*24*60*60,				// 30 days
			'PASS_LENGTH' => 40,	// 40-character passwords
			'HASH_COST' => 10,
			// Misc.
			'ROOT' => $_SERVER['DOCUMENT_ROOT'].'/val/VirtualCurrency/',
			'DOMAIN' => $_SERVER['HTTP_HOST'].'/val',
			// WHAT FOLLOWS IS NOT SUPPOSED TO BE CHANGED
			'ADMIN' => 0,	// Address 0 should NOT be used for transfers. It is meant to keep admin password and temporarily store fees.
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

