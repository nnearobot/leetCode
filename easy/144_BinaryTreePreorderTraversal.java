/**
 * 144. Binary Tree Preorder Traversal
 * Easy
 * https://leetcode.com/problems/binary-tree-preorder-traversal/description/
 */
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
import java.util.Stack;
import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> tree = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        stack.add(root);
        
        while (!stack.isEmpty()) {
            TreeNode node = stack.peek();
            stack.pop();
            if (node == null) {
                continue;
            }

            tree.add(node.val);
            if (node.right != null) {
                stack.add(node.right);
            }
            if (node.left != null) {
                stack.add(node.left);
            }
        }
        
        return tree;
    }
}