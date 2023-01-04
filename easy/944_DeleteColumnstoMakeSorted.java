/**
 * 944. Delete Columns to Make Sorted
 * Easy
 * https://leetcode.com/problems/delete-columns-to-make-sorted/
 */
class Solution {
    public int minDeletionSize(String[] strs) {
        int colNum = 0;
        for (int letterNum = 0; letterNum < strs[0].length(); letterNum++ ) {
            for (int wordNum = 1; wordNum < strs.length; wordNum++) {
                if (strs[wordNum].charAt(letterNum) < strs[wordNum - 1].charAt(letterNum)) {
                    colNum++;
                    break;
                }
            }
        }
        return colNum;
    }
}