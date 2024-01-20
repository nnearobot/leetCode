// 907. Sum of Subarray Minimums
// medium
// https://leetcode.com/problems/sum-of-subarray-minimums

use std::cmp::min;

impl Solution {
    pub fn sum_subarray_mins(arr: Vec<i32>) -> i32 {
        const MOD: i32 = 1000000007;
        let n = arr.len();
        let mut res = 0;
        let mut row_sum = 0;
        for i in (0..n) {
            if i > 0 && arr[i] <= arr[i - 1] {
                row_sum -= arr[i - 1];
            } else {
                row_sum = arr[i];
                let mut min_val = arr[i];
                for j in (i + 1..n) {
                    min_val = min(min_val, arr[j]);
                    row_sum += min_val;
                }
            }
            if row_sum >= (MOD - res) {
                res = row_sum - (MOD - res);
            } else {
                res += row_sum;
            }
        }

        res
    }
}