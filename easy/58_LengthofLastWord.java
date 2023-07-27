/**
 * 58. Length of Last Word
 * Easy
 * https://leetcode.com/problems/length-of-last-word
 */
class Solution {
    public int lengthOfLastWord(String s) {
        boolean isWord = false;
        int l = 0;
        for (int i = s.length() - 1; i >= 0; --i) {
            if (s.charAt(i) == ' ') {
                if (!isWord) {
                    continue;
                } else {
                    return l;
                }
            } else {
                isWord = true;
                l++;
            }
        }

        return l;
    }
}