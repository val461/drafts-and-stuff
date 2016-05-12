<?php
	$resetPassword = false;	// Setting this to true and loading this page should remove admin password, thus it should always be set to false
	$newPassword = '';		// You can get a new password in the administration panel (admin.php)
	
	if($resetPassword)
	{
		include_once($_SERVER['DOCUMENT_ROOT'].'/val/VirtualCurrency/phptools/constants.php');
		include_once(ROOT.'phptools/crypt.php');
		include_once(ROOT.'phptools/new.php');
		
		setPassword(computeHash($newPassword), ADMIN);
		echo 'Password reset.';
	}
	else
		echo 'This page needs to be manually edited in order to reset password.';
?>

