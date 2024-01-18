// 70. Climbing Stairs
// easy
// https://leetcode.com/problems/climbing-stairs

impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
        if n == 1 {
            return 1;
        }

        let mut dp_0 = 1;
        let mut dp_1 = 2;
        for i in (2..n) {
            let dp = dp_0 + dp_1;
            dp_0 = dp_1;
            dp_1 = dp;
        }

        dp_1
    }
}