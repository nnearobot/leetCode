<?php
/**
 * MIT License
 *
 * Copyright (c) 2022 Rimma Maksiutova
 */

class Solution {

    /**
     * @param Integer $x
     * @return Boolean
     */
    function isPalindrome($x)
    {
        if ($x < 0) {
            return false;
        }

        $xArr = [];
        $mod = 1;
        do {

            $modulo = $x % ($mod * 10);
            $xArr[] = floor($modulo / $mod);
            $mod *= 10;

        } while ($mod <= $x);

        $center = floor(count($xArr) / 2);
        for ($i = 0; $i <= $center; $i++) {
            $j = count($xArr) - 1 - $i;
            if ($j == $i) {
                return true;
            }

            if ($xArr[$i] != $xArr[$j]) {
                return false;
            }
        }

        return true;
    }
}