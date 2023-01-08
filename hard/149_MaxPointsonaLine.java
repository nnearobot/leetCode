/**
 * 149. Max Points on a Line
 * Hard
 * https://leetcode.com/problems/max-points-on-a-line/
 */

/*
 * y1 = a * x1 + b
 * y2 = a * x2 + b
 * 
 * b = y1 - a * x1
 * y2 = a * x2 + y1 - a * x1
 * a * (x2 - x1) = y2 - y1
 * 
 * a = (y2 - y1) / (x2 - x1)  (1)
 * b = y1 - x1 * (y2 - y1) / (x2 - x1) (2)
 * 
 * y = x * (y2 - y1) / (x2 - x1) + y1 - x1 * (y2 - y1) / (x2 - x1)
 * y * (x2 - x1) = x * (y2 - y1) + y1 * (x2 - x1) - x1 * (y2 - y1)
 * y * (x2 - x1) = (x - x1) * (y2 - y1) + y1 * (x2 - x1)
*/

class Solution {
    public int maxPoints(int[][] points) {
        if (points.length < 3) {
            return points.length;
        }

        double yy, xx;
        int[] p1, p2, p3;
        int maxPointsOnLine = 2,
            n = points.length,
            currentPoints;
        Boolean vert, horiz;

        for (int i = 0; i < n - 2; ++i) {
            // for i and i + 1 points calculate a and b,
            // and then try all next points if they coordinates fits them
            p1 = points[i];
            for (int j = i + 1; j < n - 1; ++j) {
                p2 = points[j];
                vert = false;
                horiz = false;
                // a = (p2[1] - p1[1]) / (p2[0] - p1[0]);
                // b = p1[1] - (p1[0] * (p2[1] - p1[1]) / (p2[0] - p1[0]));

                if (p2[0] == p1[0]) {
                    vert = true;
                } else if (p2[1] == p1[1]) {
                    horiz = true;
                }

                currentPoints = 2;
                for (int k = j + 1; k < n; ++k) {
                    p3 = points[k];
                    if (vert) {
                        currentPoints += p3[0] == p1[0] ? 1 : 0;
                    } else if (horiz) {
                        currentPoints += p3[1] == p1[1] ? 1 : 0;
                    } else {
                        //y * (x2 - x1) = (x - x1) * (y2 - y1) + y1 * (x2 - x1)
                        yy = p3[1] * (p2[0] - p1[0]);
                        xx = (p3[0] - p1[0]) * (p2[1] - p1[1]) + p1[1] * (p2[0] - p1[0]);
                        currentPoints += yy == xx ? 1 : 0;
                    }
                }
                maxPointsOnLine = Math.max(maxPointsOnLine, currentPoints);
            }
        }

        return maxPointsOnLine;
    }
}