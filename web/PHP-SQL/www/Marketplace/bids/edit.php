<!DOCTYPE html>
<html>
	<head>
		<meta http-equiv="content-type" content="text/html;charset=utf-8" />
		<title>
			Manage an ad
		</title>
		<style>
			table
			{
				margin: auto;
				width: 80%;
			}
			td
			{
				padding-top: 10px;
				padding-right: 50px;
			}
			input, select, textarea
			{
				width: 100%;
			}
			textarea
			{
				height: 16em;
			}
		</style>
	</head>
	<body>
<?php
	include_once($_SERVER['DOCUMENT_ROOT'].'/val/Marketplace/phptools/constants.php');
	include_once(ROOT.'/links.php');
	include_once(ROOT.'/phptools/manage.php');
	
	$ad['id'] = isset($_POST['id'])?$_POST['id']:(isset($_GET['id'])?$_GET['id']:'');
	$ad['token'] = isset($_POST['token'])?$_POST['token']:(isset($_GET['token'])?$_GET['token']:'');
	
	if($ad = getAd($ad['id'], $ad['token']))
	{
		if($ad['error'])
		{
?>
		<p>
			An error happened. Code: <?php echo $ad['error']; ?>
		</p>
<?php
		}
?>
		<form method="post">
			<table>
				<tr>
					<td>
						<input type="hidden" name="token" value="<?php echo $ad['token']; ?>"/>
						<input type="hidden" name="id" value="<?php echo $ad['id']; ?>"/>
						<label for="publink">Public ad link:</label><br/>
						<input type="text" id="publink" value="<?php echo $ad['publink']; ?>" onClick="this.setSelectionRange(0, this.value.length)"/>
					</td>
					<td colspan="2">
							<label for="title">Title:</label><br/>
							<input type="text" name="title" id="title" value="<?php echo $ad['title']; ?>" maxlength="255"/>
					</td>
				</tr>
				<tr>
					<td>
						<label for="edlink">Ad edition link:</label><br/>
						<input type="text" id="edlink" value="<?php echo $ad['edlink']; ?>" onClick="this.setSelectionRange(0, this.value.length)"/>
					</td>
					<td>
						<label for="quantity">Quantity:</label><br/>
						<input type="text" name="quantity" id="quantity" value="<?php echo $ad['quantity']; ?>"/>
					</td>
					<td>
						<label for="category">Category:</label><br/>
						<input type="text" name="category" id="category" value="<?php echo $ad['category']; ?>"/>
					</td>
				</tr>
				<tr>
					<td title="Seller will receive payment to this address.">
						<label for="address">Address to receive payment:</label><br/>
						<input type="text" name="address" id="address" value="<?php echo $ad['address']; ?>" onClick="this.setSelectionRange(0, this.value.length)"/>
					</td>
					<td>
						<label for="price">Price per unit:</label><br/>
						<input type="text" name="price" id="price" value="<?php echo $ad['price']; ?>"/>
					</td>
					<td>
						<label for="shipfee">Shipping fee:</label><br/>
						<input type="text" name="shipfee" id="shipfee" value="<?php echo $ad['shipfee']; ?>"/>
					</td>
				</tr>
				<tr>
					<td>
						<label for="exp">Expiration (YYYY-MM-DD):</label><br/>
						<input type="text" name="exp" id="exp" value="<?php echo $ad['exp']; ?>"/>
					</td>
					<td colspan="3" rowspan="4">
						<label for="content">Content:</label><br/>
						<textarea name="content" id="content"><?php echo $ad['content']; ?></textarea>
					</td>
				</tr>
				<tr>
					<td>
						<label for="status">Ad status:</label><br/>
						<select name="status" id="status">
							<option value="visible"<?php echo ($ad['visible']?' selected="selected"':''); ?>>Visible</option>
							<option value="hidden"<?php echo ($ad['visible']?'':' selected="selected"'); ?>>Hidden</option>
						</select>
					</td>
				</tr>
				<tr>
					<td>
						<label for="action">Action:</label><br/>
						<select name="action" id="action">
							<option value="save" selected="selected">Save</option>
							<option value="cancel">Cancel</option>
							<option value="delete">Delete ad (irreversible; consider just hiding it)</option>
						</select>
					</td>
				</tr>
				<tr>
					<td>
						<input type="submit" value="Proceed"/>
					</td>
				</tr>
			</table>
		</form>
<?php
	}
	else
	{
?>
		<p>
				We have been unable to find an ad. Query details:<br/>
				Id:<br/>
				<?php echo $ad['id']; ?><br/>
				Token:<br/>
				<?php echo $ad['token']; ?>
		</p>
<?php
	}
?>
	</body>
</html>

