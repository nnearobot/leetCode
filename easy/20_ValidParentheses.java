/**
 * 20. Valid Parentheses
 * Easy
 * https://leetcode.com/problems/valid-parentheses/description/
 */

import java.util.*;

class Solution {
    public boolean isValid(String s) {
        Set<Character> open = new HashSet<Character>(Arrays.asList('(', '{', '['));
        Map<Character, Character> close = new HashMap<Character, Character>();
        close.put(')', '(');
        close.put('}', '{');
        close.put(']', '[');

        Stack<Character> stack = new Stack<Character>();
        Character bracket, prevBracket;
        for (int i = 0; i < s.length(); ++i) {
            bracket = s.charAt(i);
            if (open.contains(bracket)) {
                stack.push(bracket);
                continue;
            }

            if (stack.empty()) return false;
            if (stack.pop() != close.get(bracket)) return false;
        }

        return stack.empty();
    }
}