/**
 * 746. Min Cost Climbing Stairs
 * Easy
 * You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
 * You can either start from the step with index 0, or the step with index 1.
 * Return the minimum cost to reach the top of the floor.
 */
class Solution {
    private HashMap<Integer, Integer> memo = new HashMap<Integer, Integer>();
    private int[] cost;

    public int minCostClimbingStairs(int[] cost) {
        this.cost = cost;

        return Math.min(dp(cost.length - 1), dp(cost.length - 2));
    }

    public int dp(int i) {
        if (i == 0) return cost[0];
        if (i == 1) return cost[1];

        if (!memo.containsKey(i)) {
            memo.put(i, Math.min(dp(i - 1), dp(i - 2)) + cost[i]);
        }

        return memo.get(i);
    }
}