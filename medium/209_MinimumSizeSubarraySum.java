/**
 * 209. Minimum Size Subarray Sum
 * Medium
 * https://leetcode.com/problems/minimum-size-subarray-sum
 */
class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int l = nums.length;
        int left = 0;
        int right = 0;
        int sum = nums[0];
        int res = l + 1;
        while (right < l) {
            if (sum >= target) {
                if (left == right) {
                    return 1;
                } else {
                    res = Math.min(res, right - left + 1);
                    sum -= nums[left++];
                }
            } else if (right == l - 1) {
                break;
            } else {
                sum += nums[++right];
                if (right - left + 1 > res) {
                    sum -= nums[left++];
                }
            }
        }

        return res <= l ? res : 0;
    }
}