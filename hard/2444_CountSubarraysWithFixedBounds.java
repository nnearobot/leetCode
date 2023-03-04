/**
 * 2444. Count Subarrays With Fixed Bounds
 * Hard
 * https://leetcode.com/problems/count-subarrays-with-fixed-bounds
 */
class Solution {
    public long countSubarrays(int[] nums, int minK, int maxK) {
        int start = 0, minStart = 0, maxStart = 0;
        long res = 0;
        boolean isMin = false, isMax = false;
        for (int i = 0; i < nums.length; ++i) {
            if (nums[i] < minK || nums[i] > maxK) {
                start = i + 1;
                isMin = isMax = false;
                continue;
            }
            if (nums[i] == minK) {
                minStart = i;
                isMin = true;
            }
            if (nums[i] == maxK) {
                maxStart = i;
                isMax = true;
            }
            if (isMin && isMax) {
                res += (Math.min(minStart, maxStart) - start + 1);
            }
        }

        return res;
    }
}