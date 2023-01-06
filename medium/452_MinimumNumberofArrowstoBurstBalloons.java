/**
 * 452. Minimum Number of Arrows to Burst Balloons
 * Medium
 * https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/
 */
import java.util.Arrays;

class Solution {
    public int findMinArrowShots(int[][] points) {
        Arrays.sort(points, (balloon1, balloon2) -> {
            if (balloon1[1] < balloon2[1]) return -1;
            if (balloon1[1] == balloon2[1]) return 0;
            return 1;
        });

        int arrows = 1;
        int commonEnd = points[0][1];
        for (int[] balloon : points) {
            if (balloon[0] > commonEnd) {
                arrows++;
                commonEnd = balloon[1];
            }
        }

        return arrows;
    }
}