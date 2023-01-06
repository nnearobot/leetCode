/**
 * 1833. Maximum Ice Cream Bars
 * Medium
 * https://leetcode.com/problems/maximum-ice-cream-bars/
 */
class Solution {
    public int maxIceCream(int[] costs, int coins) {
        int max = costs[0];
        for (int i : costs) {
            max = Math.max(max, i);
        }

        int[] freqs = new int[max + 1];
        for (int i : costs) {
            freqs[i]++;
        }

        int bars = 0;
        for (int i = 1; i <= max; i++) {
            if (freqs[i] == 0) {
                continue;
            }

            if (coins < i) {               
                break;
            }

            int newbars = Math.min(coins / i, freqs[i]);
            bars += newbars;
            coins -= newbars * i;
        }

        return bars;
    }
}