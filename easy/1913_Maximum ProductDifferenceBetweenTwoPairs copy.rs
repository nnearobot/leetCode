// 1913. Maximum Product Difference Between Two Pairs
// easy
// https://leetcode.com/problems/maximum-product-difference-between-two-pairs

impl Solution {
    pub fn max_product_difference(nums: Vec<i32>) -> i32 {
        let mut sorted = nums;
        sorted.sort();
        let ln = sorted.len();
        (sorted[ln - 1] * sorted[ln - 2]) - (sorted[0] * sorted[1])
    }
}