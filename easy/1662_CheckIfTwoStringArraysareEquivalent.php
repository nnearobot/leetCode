<?php
/**
 * MIT License
 *
 * Copyright (c) 2022 Rimma Maksiutova
 */

/**
 * 1662. Check If Two String Arrays are Equivalent
 * Easy
 * Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.
 * A string is represented by an array if the array elements concatenated in order forms the string.
 */
class Solution {

    /**
     * @param String[] $word1
     * @param String[] $word2
     * @return Boolean
     */
    function arrayStringsAreEqual($word1, $word2) {
        return join($word1) == join($word2);
    }
}