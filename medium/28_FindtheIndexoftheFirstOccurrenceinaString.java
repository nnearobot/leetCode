/**
 * 28. Find the Index of the First Occurrence in a String
 * Medium
 * https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string
 */
class Solution {
    public int strStr(String haystack, String needle) {
        if (needle.length() > haystack.length()) {
            return -1;
        }

        for (int i = 0; i <= haystack.length() - needle.length(); ++i) {
            if (haystack.charAt(i) != needle.charAt(0)) {
                continue;
            }

            boolean isEqual = true;
            for (int j = 1; j < needle.length(); ++j) {
                if (haystack.charAt(i + j) != needle.charAt(j)) {
                    isEqual = false;
                    break;
                }
            }

            if (isEqual) {
                return i;
            }
        }

        return -1;
    }
}