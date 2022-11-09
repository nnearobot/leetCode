<?php
/**
 * MIT License
 *
 * Copyright (c) 2022 Rimma Maksiutova
 */

/**
 * 4. Median of Two Sorted Arrays
 * Hard
 * Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
 * The overall run time complexity should be O(log (m+n)).
 */
class Solution {

    /**
     * @param int[] $nums1
     * @param int[] $nums2
     * @return Float
     */
    function findMedianSortedArrays(array $nums1, array $nums2): float
    {
        $total = (count($nums1) + count($nums2));
        $middle = floor(($total - 1) / 2);

        $a = $b = $count = 0;
        $el1 = $el2 = null;

        while ($count <= $middle + 1) {
            if (isset($nums1[$a]) && isset($nums2[$b])) {
                if ($nums1[$a] < $nums2[$b]) {
                    $el = $nums1[$a];
                    $a++;
                } else {
                    $el = $nums2[$b];
                    $b++;
                }
            } elseif (isset($nums1[$a])) {
                $el = $nums1[$a];
                $a++;
            } elseif (isset($nums2[$b])) {
                $el = $nums2[$b];
                $b++;
            }

            if ($count == $middle) {
                if ($total % 2) {
                    return $el;
                } else {
                    $el1 = $el;
                }
            }

            if ($count == $middle + 1 && isset($el1)) {
                $el2 = $el;

                return ($el1 + $el2) / 2;
            }

            $count++;
        }

        return 0;
    }
}