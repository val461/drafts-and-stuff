<!DOCTYPE html>
<html>
	<head>
		<meta http-equiv="content-type" content="text/html;charset=utf-8" />
		<title>World</title>
		<style>
			a:hover
			{
				text-decoration: none;
			}
		</style>
	</head>
	<body>
		<h1>World</h1>
		<hr/>
		<p>
			Please select your language:
		</p>
		<ul>
<?php
	require_once $_SERVER['DOCUMENT_ROOT'].'/val/world/php/constants.php';
	if($handle = opendir(ROOT)) {
		$not_languages = ['.', '..', 'index.php', 'php'];
		while (false !== ($lang = readdir($handle))) {
			if(! in_array($lang, $not_languages, true))
				{
?>
			<li><a href="<?php echo $lang; ?>"><?php echo $lang; ?></a></li>
<?php
				}
		}
		closedir($handle);
	}
?>
		</ul>
	</body>
</html>

