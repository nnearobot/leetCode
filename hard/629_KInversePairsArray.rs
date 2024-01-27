// 629. K Inverse Pairs Array
// hard
// https://leetcode.com/problems/k-inverse-pairs-array/

impl Solution {
    pub fn k_inverse_pairs(n: i32, k: i32) -> i32 {
        const MOD: i32 = 1000000007;
        let mut dp: Vec<i32> = Vec::new();
        for i in (0..k + 1) {
            dp.push(0);
        }
        for i in (1..=n) {
            let mut tmp: Vec<i32> = Vec::new();
            for i in (0..k + 1) {
                tmp.push(0);
            }
            tmp[0] = 1;
            for j in (1..=k) {
                let mut val = if j >= i { dp[(j - i) as usize ] } else { 0 };
                val = (dp[j as usize] + MOD - val) % MOD;
                tmp[j as usize] = (tmp[(j - 1) as usize] + val) % MOD;
            }
            dp = tmp.clone();
        }
        let val = if k > 0 { dp[(k - 1) as usize] } else { 0 };

        (dp[k as usize] + MOD - val) % MOD
    }
}