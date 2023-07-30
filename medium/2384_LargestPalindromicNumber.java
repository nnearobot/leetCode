/**
 * 2384. Largest Palindromic Number
 * Medium
 * https://leetcode.com/problems/largest-palindromic-number
 */
class Solution {
    public String largestPalindromic(String num) {
        int[] digitCount = new int[10]; // we have totally 10 digits from 0 to 9

        // let's count all the digits in the input string:
        for (char digit : num.toCharArray()) {
            digitCount[digit - '0']++;
        }

        // The approach is to make a left and right parts of the palindrome
        // from the digits which are twice or more in the input string, 
        // starting from the max digit.
        // And if the input string have a digits, which are just once
        // (or have one remainder of pairs), the max of them can be a middle of the palindrome
        String left = "";
        String middle = "";
        String right = "";

        // Make a palindrome from largest to smallest digits, that are in the input string:
        for (int i = 9; i >= 0; i--) {
            if (i == 0 && left.length() == 0 && middle.length() == 0) {
                return "0";
            }

            int pairCount = digitCount[i] / 2;
            int remainder = digitCount[i] % 2;
             System.out.println(Integer.toString(i) + ": " + Integer.toString(pairCount) + ", " + Integer.toString(remainder));

            // if there are at least 2 digits in the input string,
            // they can be at the left and right part of the palindrom:
            for (int j = 0; j < pairCount; j++) {
                if (i == 0 && left.length() == 0) {
                    continue;
                }

                left += Integer.toString(i);
                right = Integer.toString(i) + right;
            }

            // if there one digit remains, it can be in a middle of the palindrome,
            // if there is nothing is in the middle yet (the max digit will be in the middle):
            if (remainder != 0 && middle.length() == 0) {
                middle = Integer.toString(i);
            }
        }

        // an answer is a combination of all three parts:
        String res = left + middle + right;

        return res;
    }
}