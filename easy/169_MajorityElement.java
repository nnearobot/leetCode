/**
 * 169. Majority Element
 * Easy
 * https://leetcode.com/problems/majority-element/d
 */

// Boyer-Moore Voting Algorithm
class Solution {
    public int majorityElement(int[] nums) {
        int count = 0;
        Integer ans = null;
        for (int el : nums) {
            if (count == 0) {
                ans = el;
            }

            count += (el == ans) ? 1 : -1;
        }

        return ans;
    }
}

/*
import java.utils.HashMap;

class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

        int l = nums.length;
        double halfSize = Math.floor(l / 2);

        for (int i = 0; i < l; ++i) {
            int el = nums[i];
            map.put(nums[i], (map.get(el) == null ? 0 : map.get(el)) + 1);
            if (map.get(el) > halfSize) {
                return el;
            }
        }

        return 0;
    }
}
*/