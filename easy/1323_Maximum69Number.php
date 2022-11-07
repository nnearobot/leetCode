<?php
/**
 * MIT License
 *
 * Copyright (c) 2022 Rimma Maksiutova
 */

/**
 * 1323. Maximum 69 Number
 * Easy
 * You are given a positive integer num consisting only of digits 6 and 9.
 * Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).
 */
class Solution {
    /**
     * @param Integer $num
     * @return Integer
     */
    function maximum69Number($num)
    {
        if ($num == 9) {
            return $num;
        }

        if ($num == 6) {
            return 9;
        }

        $numArr = [];
        while ($num) {
            $numArr[] = $num % 10;
            $num = floor($num / 10);
        }

        for ($i = $numArr[count($numArr) - 1]; $i >= 0; $i--) {
            if ($numArr[$i] == 6) {
                $numArr[$i] = 9;
                break;
            }
        }

        $mod = 1;
        $res = 0;
        foreach ($numArr as $i) {
            $res += $i * $mod;
            $mod *= 10;
        }

        return $res;
    }
}