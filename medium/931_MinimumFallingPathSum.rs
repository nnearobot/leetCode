// 931. Minimum Falling Path Sum
// medium
// https://leetcode.com/problems/minimum-falling-path-sum/

use std::cmp::min;

impl Solution {
    pub fn min_falling_path_sum(matrix: Vec<Vec<i32>>) -> i32 {
        let n = matrix.len();
        let mut dp: Vec<i32> = matrix[0].clone();
        for i in (1..n) {
            let mut tmp_vec: Vec<i32> = matrix[i].clone();
            for j in (0..n) {
                let mut min_val = dp[j];
                if j > 0 {
                    min_val = min(min_val, dp[j - 1]);
                }
                if j < n - 1 {
                    min_val = min(min_val, dp[j + 1]);
                }
                tmp_vec[j] += min_val;
            }
            dp = tmp_vec;
        }

        *dp.iter().min().unwrap()
    }
}