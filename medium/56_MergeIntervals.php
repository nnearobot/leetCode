<?php
/**
 * MIT License
 *
 * Copyright (c) 2022 Rimma Maksiutova
 */

/**
 * 56. Merge Intervals
 * Medium
 * Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
 * and return an array of the non-overlapping intervals that cover all the intervals in the input.
 */
class Solution {

    /**
     * @param Integer[][] $intervals
     * @return Integer[][]
     */
    function merge($intervals) {
        $map = array_fill(0, 10000, []);
        foreach ($intervals as $ind => $interval) {
            for ($i = $interval[0]; $i <= $interval[1]; $i++) {
                $map[$i][$ind] = true;
            }
        }

        $newIntervals = [];
        $insideInt = false;
        $kPrev = null;
        $int = [];
        $intInd = [];
        foreach ($map as $k => $v) {
            if ($insideInt) {
                if (!$v || !array_intersect_key($intInd, $v)) {
                    $int[1] = $kPrev;
                    $newIntervals[] = $int;
                    $int = [];

                    if ($v) {
                        $intInd = $v;
                        $int[0] = $k;
                    } else {
                        $insideInt = false;
                    }
                } else {
                    $intInd = $intInd + $v; // not array_merge because array_merge resets indexes
                }
            } elseif ($v) {
                $insideInt = true;
                $int[0] = $k;
                $intInd = $v;
            }
            $kPrev = $k;
        }

        if ($insideInt) {
            $int[1] = $kPrev;
            $newIntervals[] = $int;
        }

        return $newIntervals;
    }
}