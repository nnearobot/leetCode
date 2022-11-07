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

        $num = strval($num);
        $res = '';
        $changed = false;
        for ($i = 0; $i < strlen($num); $i++) {
            if (!$changed && $num[$i] == '6') {
                $res .= '9';
                $changed = true;
            } else {
                $res .= $num[$i];
            }
        }

        return (int) $res;
    }
}
