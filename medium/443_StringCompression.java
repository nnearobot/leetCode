/**
 * 443. String Compression
 * Medium
 * https://leetcode.com/problems/string-compression
 */
import java.util.Arrays;

class Solution {
    public int compress(char[] chars) {
        int count = 1;
        int p = 1;
        String strCount = "";
        for (int i = 1; i <= chars.length; ++i) {
            if (i == chars.length || chars[i] != chars[i - 1]) {
                if (count > 1) {
                    strCount = Integer.toString(count);
                    for (int j = 0; j < strCount.length(); ++j) {
                        chars[p] = strCount.charAt(j);
                        p++;
                    }
                    count = 1;
                }
                if (i < chars.length) {
                    chars[p] = chars[i];
                }
                p++;
            } else {
                count++;
            }
        }
        p--;
        chars = Arrays.copyOfRange(chars, 0, p - 1);

        return p;
    }
}