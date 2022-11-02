<?php
/**
 * MIT License
 *
 * Copyright (c) 2022 Rimma Maksiutova
 */

/**
 * 3. Longest Substring Without Repeating Characters
 * Medium
 * Given a string s, find the length of the longest substring without repeating characters.
 */
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function lengthOfLongestSubstring($s) {
        $res = 0;
        $tmpLength = 0;
        $map = [];
        $nextNum = 0;

        while ($nextNum < strlen($s) - $res) {
            for ($i = $nextNum; $i < strlen($s); $i++) {
                $char = $s[$i];
                if (isset($map[$char])) {
                    if ($tmpLength > $res) {
                        $res = $tmpLength;
                    }

                    $tmpLength = 0;
                    $nextNum = $map[$char] + 1;
                    $map = [];
                    break;
                }

                $tmpLength++;
                $map[$char] = $i;
            }

            if ($map && $tmpLength > $res) {
                $res = $tmpLength;
            }
        }

        return $res;
    }
}