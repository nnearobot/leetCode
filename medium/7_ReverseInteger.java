/**
 * 7. Reverse Integer
 * Medium
 * https://leetcode.com/problems/reverse-integer/description/
 */
class Solution {
    // Int has a minimum value of -2,147,483,648 and a maximum value of 2,147,483,647 (inclusive).

    public int reverse(int x) {
        int n = 0,
            tmpX = Math.abs(x);
        while (tmpX > 0) {
            tmpX /= 10;
            n++;
        }

        if (n == 1) {
            return x;
        }

        Boolean isNeg = x < 0;
        x = Math.abs(x);

        int[] max = {2, 1, 4, 7, 4, 8, 3, 6, 4, 7};
        if (isNeg) {
            max[9] = 8;
        }

        int res = 0,
            i = 0,
            digit;
        Boolean over = x > 999999999;
        while (x > 0) {
            digit = x % 10;
            if (over) {
                if (digit > max[i]) {
                    return 0;
                }
                if (digit < max[i]) {
                    over = false;
                }
            }

            if (digit != 0) {
                res += digit * Math.pow(10, n - i - 1);
            }

            x /= 10;
            i++;
        }

        if (isNeg) {
            res = 0 - res;
        }

        return res;
    }
}