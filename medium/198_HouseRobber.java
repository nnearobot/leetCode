/**
 * 198. House Robber
 * Medium
 * You are a professional robber planning to rob houses along a street.
 * Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them 
 * is that adjacent houses have security systems connected and it will automatically contact the police 
 * if two adjacent houses were broken into on the same night.
 * Given an integer array nums representing the amount of money of each house, return the maximum amount 
 * of money you can rob tonight without alerting the police.
 * 
 * 
 */

class Solution {
    private HashMap<Integer, Integer> memo = new HashMap<Integer, Integer>();
    private int[] nums;
    
    public int rob(int[] nums) {
        this.nums = nums;
        
        return this.dp(nums.length - 1);
    }
    
    private int dp(int i) {
        if (i == 0) return this.nums[0];
        if (i == 1) return Math.max(this.nums[0], this.nums[1]);
        
        if (!this.memo.containsKey(i)) {
            this.memo.put(i, Math.max(this.dp(i - 1), this.dp(i - 2) + nums[i]));
        }

        return this.memo.get(i);
    }
}