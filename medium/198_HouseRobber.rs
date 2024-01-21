// 198. House Robber
// medium
// https://leetcode.com/problems/house-robber

use std::cmp::max;

impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {
        if nums.len() == 1 {
            return nums[0];
        }

        let mut dp_prev = nums[0];
        let mut dp = max(nums[0], nums[1]);
        for i in (2..nums.len()) {
            let dp_tmp = max(dp_prev + nums[i], dp);
            dp_prev = dp;
            dp = dp_tmp;
        }

        dp
    }
}