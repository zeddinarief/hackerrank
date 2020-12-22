<?php

function bayarcok($val = 7)
{
	$price = 0;
	while ($val > 0) {
		if ($val >= 5) {
			$price += 18000;
			$val -= 5;
		} else {
			$price += 4000;
			$val -= 1;
		}
	}
	return $price;
}

echo bayarcok(10);