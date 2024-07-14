<?php
# 726. Number of Atoms
# hard
# https://leetcode.com/problems/number-of-atoms/

class Solution {

/**
 * @param String $formula
 * @return String
 */
function countOfAtoms($formula) {
    $letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    $lettersCap = str_split($letters);
    $lettersSmall = str_split(strtolower($letters));
    $digits = str_split('0123456789');

    $stack = [];
    $letterMap = [];
    $l = strlen($formula);
    $i = 0;
    while ($i < $l) {
        if ($formula[$i] == '(') {
            $stack[] = '(';
            $i++;
            continue;
        }

        if (in_array($formula[$i], $lettersCap)) {
            $element = $formula[$i];
            $i++;
            while ($i < $l && in_array($formula[$i], $lettersSmall)) {
                $element .= $formula[$i];
                $i++;
            }
            $num = '';
            while ($i < $l && in_array($formula[$i], $digits)) {
                $num .= $formula[$i];
                $i++;
            }
            $stack[] = [$element, $num ? intval($num) : 1];
            $letterMap[$element] = 0;
            continue;
        }

        $amount = 1;
        if ($formula[$i] == ')') {
            $i++;
            $num = '';
            while ($i < $l && in_array($formula[$i], $digits)) {
                $num .= $formula[$i];
                $i++;
            }
            $amount = $num ? intval($num) : 1;
            for ($j = count($stack) - 1; $j >= 0; $j--) {
                if ($stack[$j] == '(') {
                    array_splice($stack, $j, 1);
                    break;
                }
                if ($amount > 1) {
                    $stack[$j][1] *= $amount;
                }
            }
        }
    }

    foreach ($stack as $item) {
        if ($item == '(') {
            continue;
        }
        $letterMap[$item[0]] += $item[1];
    }
    ksort($letterMap);

    $ans = '';
    foreach ($letterMap as $item => $qty) {
        $ans .= $item.($qty > 1 ? $qty : '');
    }

    return $ans;
}
}