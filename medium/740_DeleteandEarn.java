/**
 * 740. Delete and Earn
 * Medium
 * https://leetcode.com/problems/delete-and-earn/
 */
import java.util.HashMap;

class Solution {
    private HashMap<Integer, Integer> points = new HashMap<Integer, Integer>();
    private HashMap<Integer, Integer> memo = new HashMap<Integer, Integer>();
    
    public int deleteAndEarn(int[] nums) {
        int maxNum = 0;
        for (int num : nums) {
            points.put(num, points.getOrDefault(num, 0) + num);
            maxNum = Math.max(maxNum, num);
        }
        
        return dp(maxNum);
    }
    
    public int dp(int num) {
        if (num == 0) {
            return 0;
        }
        
        if (num == 1) {
            return points.getOrDefault(1, 0);
        }
        
        if (!memo.containsKey(num)) {
            memo.put(num, Math.max(dp(num - 1), dp(num - 2) + points.getOrDefault(num, 0)));   
        }
        
        return memo.get(num);
    }
}