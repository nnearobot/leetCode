// 1143. Longest Common Subsequence
// Medium
// https://leetcode.com/problems/longest-common-subsequence

function longestCommonSubsequence(text1: string, text2: string): number {
    let n = text1.length;
    let m = text2.length;
    let dp = [];
    for (let i = 0; i <= n; i++) {
        dp.push(new Array(m + 1).fill(0));
    }
    for (let i = 1; i <= n; i++) {
        for (let j = 1; j <= m; j++) {
            if (text1[i - 1] === text2[j - 1]) {
                dp[i][j] = 1 + dp[i - 1][j - 1];
            } else {
                dp[i][j] = Math.max(dp[i][j - 1], dp[i - 1][j]);
            }
        }
    }

    return dp[n][m];
};

