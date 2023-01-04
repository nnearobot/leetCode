/**
 * 520. Detect Capital
 * Easy
 * https://leetcode.com/problems/detect-capital/
 */
class Solution {
    // public boolean detectCapitalUse(String word) {
    //     return word.matches("[A-Z]*|.[a-z]*");
    // }

    public boolean detectCapitalUse(String word) {
        if (word.length() < 2) {
            return true;
        }

        Boolean firstCap = Character.isUpperCase(word.charAt(0));
        Boolean secondCap = Character.isUpperCase(word.charAt(1));

        if (!firstCap && secondCap) {
            return false;
        }

        for (int i = 2; i < word.length(); i++) {
            Boolean currentCap = Character.isUpperCase(word.charAt(i));
            if (firstCap) {
                if (secondCap && !currentCap || !secondCap && currentCap) {
                    return false;
                }
            } else if (currentCap) {
                return false;
            }
        }

        return true;
    }
}