/**
 * 926. Flip String to Monotone Increasing
 * Medium
 * https://leetcode.com/problems/flip-string-to-monotone-increasing/description/
 * 
 * bottom-top (iterative) dp implementation
 */

 class Solution {
    public int minFlipsMonoIncr(String s) {
        int n = s.length();
        if (n == 1) {
            return 0;
        }

        Character[] chars = new Character[n];
        for (int i = 0; i < n; ++i) {
            chars[i] = s.charAt(i);
        }

        int[][] dp = new int[n][2];
        dp[0][0] = chars[0] == '0' ? 0 : 1;
        dp[0][1] = chars[0] == '1' ? 0 : 1;

        for (int i = 1; i < n; ++i) {
            dp[i][0] = dp[i - 1][0] + (chars[i] == '0' ? 0 : 1);
            dp[i][1] = Math.min(dp[i - 1][0], dp[i - 1][1]) + (chars[i] == '1' ? 0 : 1);
        }

        return Math.min(dp[n - 1][0], dp[n - 1][1]);
    }
}