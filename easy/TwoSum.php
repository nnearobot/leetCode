<?php
/**
 * MIT License
 *
 * Copyright (c) 2022 Rimma Maksiutova
 */

class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer[]
     */
    function twoSum($nums, $target)
    {

        $map = [];

        foreach ($nums as $k1 => $v) {
            if (isset($map[$target - $v])) {
                $k2 = $map[$target - $v];
                break;
            }

            $map[$v] = $k1;
        }

        return [$k1, $k2];
    }
}