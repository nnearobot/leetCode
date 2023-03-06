/**
 * 1539. Kth Missing Positive Number
 * Easy
 * https://leetcode.com/problems/kth-missing-positive-number
 */
class Solution {
    public int findKthPositive(int[] arr, int k) {
        int s = 0, e = arr.length - 1;
        while (e >= s) {
            int m = s + (e - s) / 2;
            if (arr[m] - m - 1 < k) {
                s = m + 1;
            } else {
                e = m - 1;
            }
        }

        return k + s;
    }
}