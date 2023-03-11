/**
 * 382. Linked List Random Node
 * Medium
 * https://leetcode.com/problems/linked-list-random-node
 */

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
import java.util.ArrayList;
import java.util.Random;

class Solution {
    private ArrayList<Integer> listArr;
    private Random rand;
    private int length;

    public Solution(ListNode head) {
        listArr = new ArrayList<Integer>();
        ListNode node = head;
        while (node != null) {
            listArr.add(node.val);
            node = node.next;
        }
        length = listArr.size();
        rand = new Random();
    }
    
    public int getRandom() {
        int i = rand.nextInt(length);
        return listArr.get(i);
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(head);
 * int param_1 = obj.getRandom();
 */