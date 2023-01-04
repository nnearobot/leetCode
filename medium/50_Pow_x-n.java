/**
 * 50. Pow(x, n)
 * Medium
 * https://leetcode.com/problems/powx-n/
 */
class Solution {
    public double myPow(double x, int n) {
        long nn = n;
        if (n < 0) {
            x = 1 / x;
            nn = -nn;
        }

        return halfPow(x, nn);
    }

    private Double halfPow(Double x, long n) {
        if (n == 0) {
            return 1.0;
        }
        if (x == 1 || x == 0) {
            return x;
        }
        if (x == -1) {
            if (n % 2 == 0) {
                return 1.0;
            } else {
                return -1.0;
            }
        }

        Double pow = halfPow(x, n / 2);
        if (n % 2 == 1) {
            return pow * pow * x;
        }
        
        return pow * pow;
    }
}