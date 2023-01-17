/**
 * 926. Flip String to Monotone Increasing
 * Medium
 * https://leetcode.com/problems/flip-string-to-monotone-increasing/description/
 * 
 * top-bottom (recursive) dp implementation
 */

import java.util.HashMap;

class Solution {
    private HashMap<Integer, HashMap<Character, Integer>> memo = new HashMap<Integer, HashMap<Character, Integer>>();
    Character[] chars;

    public int minFlipsMonoIncr(String s) {
        int n = s.length();
        if (n == 1) {
            return 0;
        }
        
        chars = new Character[n];
        for (int i = 0; i < n; ++i) {
            chars[i] = s.charAt(i);
        }

        return Math.min(dp(chars.length - 1, '0'), dp(chars.length - 1, '1'));
    }

    int dp(int i, Character ch) {
        if (i == 0) {
            if (ch == '1') {
                return 0;
            }
            if (chars[0] == '1') {
                return 1;
            }
            return 0;
        }

        if (!memo.containsKey(i)) {
            memo.put(i, new HashMap<Character, Integer>());
        }

        if (!memo.get(i).containsKey('0')) {
            memo.get(i).put('0', dp(i - 1, '0') + (chars[i] == '0' ? 0 : 1));
        }

        if (ch == '0') {
            // if right character is 0, current character can only be 0,
            // so we dont need to calculate a dp() for '1' 
            return memo.get(i).get('0');
        }

        if (!memo.get(i).containsKey('1')) {
            memo.get(i).put('1', dp(i - 1, '1') + (chars[i] == '1' ? 0 : 1));
        }
        
        return Math.min(memo.get(i).get('0'), memo.get(i).get('1'));
    }
}