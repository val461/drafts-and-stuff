<?php
	$name = isset($_POST['name'])?$_POST['name']:'';
	$pass = isset($_POST['pass'])?$_POST['pass']:'';
	$action = isset($_POST['action'])?$_POST['action']:'';
?>
		<form method="post">
			Name: <input type="text" name="name" value="<?php echo $name; ?>" />
			Password: <input type="password" name="pass" value="<?php echo $pass; ?>" />
			<select name="action">
				<option value="log_in">log in</option>
				<option value="new_character">new character</option>
			</select>
			<input type="submit" value="proceed" />
		</form>
		<hr/>
<?php

