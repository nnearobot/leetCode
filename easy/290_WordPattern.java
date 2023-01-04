/**
 * 290. Word Pattern
 * Easy
 * https://leetcode.com/problems/word-pattern/
 */
import java.util.HashMap;

class Solution {
    public boolean wordPattern(String pattern, String s) {
        HashMap<String, String> keys = new HashMap<String, String>();
        HashMap<String, String> vals = new HashMap<String, String>();
        String[] words = s.split(" ");

        if (words.length != pattern.length()) {
            return false;
        }

        for (int i = 0; i < pattern.length(); i++) {
            String k = pattern.substring(i, i + 1);
            String word = words[i];
 
            if (keys.containsKey(k) && !keys.get(k).equals(word)) {
                return false;
            }

            if (vals.containsKey(word) && !vals.get(word).equals(k)) {
                return false;
            }

            if (!keys.containsKey(k)) {
                keys.put(k, word);
                vals.put(word, k);
            }
        }

        return true;
    }
}