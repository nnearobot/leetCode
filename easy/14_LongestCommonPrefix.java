/**
 * 14. Longest Common Prefix
 * Easy
 * https://leetcode.com/problems/longest-common-prefix/description/
 * Write a function to find the longest common prefix string amongst an array of strings.
 * If there is no common prefix, return an empty string "".
 */
class Solution {
    public String longestCommonPrefix(String[] strs) {
        String prefix = strs[0];

        for (int i = 1; i < strs.length; i++) {
            String str = strs[i];
            if (str.length() < prefix.length()) {
                prefix = prefix.substring(0, str.length());
            }
            String tmpPref = "";
            int j = prefix.length();
            int step = j;
            if (step % 2 == 1) {
                step++;
            }
            do {
                step /= 2;
                if (prefix.substring(0, j).equals(str.substring(0, j))) {
                    tmpPref = prefix.substring(0, j);
                    j += step;
                } else {
                    j -= step;
                }
            } while (j <= prefix.length() && step > 0);

            if (tmpPref == "") {
                return "";
            }

            prefix = tmpPref;
        }

        return prefix;
    }
}