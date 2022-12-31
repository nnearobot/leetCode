/**
 * MIT License
 *
 * Copyright (c) 2022 Rimma Maksiutova
 * 
 * 4. Median of Two Sorted Arrays
 * https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/description/
 * Hard
 * You are given two 0-indexed integer arrays nums and multipliers of size n and m respectively, where n >= m.
 * You begin with a score of 0. You want to perform exactly m operations. On the ith operation (0-indexed) you will:
 * Choose one integer x from either the start or the end of the array nums
 * Add multipliers[i] * x to your score.
 * Note that multipliers[0] corresponds to the first operation, multipliers[1] to the second operation, and so on.
 * Remove x from nums.
 * Return the maximum score after performing m operations.
 */
class Solution {
    public int maximumScore(int[] nums, int[] multipliers) {
        int n = nums.length;
        int m = multipliers.length;
        int[][] dp = new int[m + 1][m + 1];

        for (int i = m - 1; i >= 0; i--) {
            for (int l = i; l >= 0; l--) {
                int mult = multipliers[i];
                int r = n - 1 - (i - l);
                dp[i][l] = Math.max(mult * nums[l] + dp[i + 1][l + 1], mult * nums[r] + dp[i + 1][l]);
            }
        }

        return dp[0][0];
    }
}