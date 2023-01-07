/**
 * 1056. Confusing Number
 * Easy
 * https://leetcode.com/problems/confusing-number/description/
 */
import java.util.HashMap;

class Solution {
    public boolean confusingNumber(int n) {
        HashMap<Character, Character> valid = new HashMap<Character, Character>();
        valid.put('0', '0');
        valid.put('1', '1');
        valid.put('6', '9');
        valid.put('8', '8');
        valid.put('9', '6');

        String nString = Integer.toString(n);
        int slen = nString.length();
        int halfLen = (slen + 1) / 2;
        Boolean confusing = false;
        for (int i = 0; i < halfLen; ++i) {
            Character digit1 = nString.charAt(i);
            Character digit2 = nString.charAt(slen - i - 1);
            if (!valid.containsKey(digit1) || !valid.containsKey(digit2)) {
                return false;
            }
            if (digit1 != valid.get(digit2)) {
                confusing = true;
            }
        }
        
        return confusing;
    }
}