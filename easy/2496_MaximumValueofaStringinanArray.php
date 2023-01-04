<?php
/**
 * 2496. Maximum Value of a String in an Array
 * Easy
 * https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/
 */

class Solution {
    /**
     * @param String[] $strs
     */
    function maximumValue($strs): int
    {
        $digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'];
        $max = 0;
        
        foreach ($strs as $str) {
            $num = '';
            $len = strlen($str);
            for ($i = 0; $i < $len; $i++) {
                if (in_array($str[$i], $digits)) {
                    $num .= $str[$i];
                } else {
                    $max = $max > $len ? $max : $len;
                    $num = '';
                    break;
                }
            }
            if ($num) {
                $num = intval($num);
                $max = $max > $num ? $max : $num;
            }
        }
        
        return $max;
    }
}