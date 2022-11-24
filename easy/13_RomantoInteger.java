/**
 * 13. Roman to Integer
 * Easy
 * Given a roman numeral, convert it to an integer.
 */
class Solution {
    public int romanToInt(String s) {
        int res = 0;
        int length = s.length();

        for (int i = 0; i < length; i++) {
            res += switch (s.charAt(i)) {
                case 'I' -> i < length - 1 && (s.charAt(i + 1) == 'V' || s.charAt(i + 1) == 'X') ? -1 : 1;
                case 'V' -> 5;
                case 'X' -> i < length - 1 && (s.charAt(i + 1) == 'L' || s.charAt(i + 1) == 'C') ? -10 : 10;
                case 'L' -> 50;
                case 'C' -> i < length - 1 && (s.charAt(i + 1) == 'D' || s.charAt(i + 1) == 'M') ? -100 : 100;
                case 'D' -> 500;
                case 'M' -> 1000;
                default -> 0;
            };
        }
        
        return res;
    }
}