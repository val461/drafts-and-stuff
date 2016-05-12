<?php
	include_once($_SERVER['DOCUMENT_ROOT'].'/val/Marketplace/phptools/constants.php');
	
	function getAd($id, $token = NULL)
	{
		$ad = NULL;
//		if(correctId($id))
		if(true)
		{
			$ad['id'] = '';
			$ad['title'] = '';
			$ad['quantity'] = '';
			$ad['price'] = '';
			$ad['category'] = '';
			$ad['content'] = '';
			$ad['visible'] = true;
			$ad['exp'] = '';
			
			$ad['type'] = 'bids';
			if($ad['type'] == 'bids')
			{
				$ad['address'] = '';
				$ad['shipfee'] = '';
			}
			else if($ad['type'] == 'asks')
			{
			    
			}
			$baseUrl = 'http://'.DOMAIN.'/'.$ad['type'];
			$ad['publink'] = $baseUrl.'/consult.php?id='.$ad['id'];
		}
		if(isset($token))	// token provided: check authorization
		{
			$ad['token'] = $token;
			$ad['id'] = '';
			$ad['error'] = NULL;
			
			$ad['edlink'] = $baseUrl.'/edit.php?id='.$ad['id'].'&token='.$ad['token'];
		}
		else	// no token: mere consulting
		{
			
		}
		return $ad;
	}

