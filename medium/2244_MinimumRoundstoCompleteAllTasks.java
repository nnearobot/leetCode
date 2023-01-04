/**
 * 2244. Minimum Rounds to Complete All Tasks
 * Medium
 * https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/
 */

 import java.util.HashMap;

 class Solution {
     public int minimumRounds(int[] tasks) {
         if (tasks.length == 1) {
             return -1;
         }
 
         HashMap<Integer, Integer> taskMap = new HashMap<Integer, Integer>();
 
         //first create a quantity map of tasks
         for (int difficulty : tasks) {
             if (!taskMap.containsKey(difficulty)) {
                 taskMap.put(difficulty, 0);
             }
 
             taskMap.put(difficulty, taskMap.get(difficulty) + 1);
         }
 
         int rounds = 0;
         for (int qty : taskMap.values()) {
             if (qty == 1) {
                 return -1;
             }
 
             int rnds = qty / 3;
             rounds += rnds;
 
             int remainder = qty % 3;
             if (remainder > 0) {
                 rounds += 1;
             }
         }
 
         return rounds;
     }
 }