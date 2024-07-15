<?php
# 2196. Create Binary Tree From Descriptions
# medium
# https://leetcode.com/problems/create-binary-tree-from-descriptions/


/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     public $val = null;
 *     public $left = null;
 *     public $right = null;
 *     function __construct($val = 0, $left = null, $right = null) {
 *         $this->val = $val;
 *         $this->left = $left;
 *         $this->right = $right;
 *     }
 * }
 */
class Solution {
    private $nodes = [];

    /**
     * @param Integer[][] $descriptions
     * @return TreeNode
     */
    function createBinaryTree($descriptions): TreeNode
    {
        foreach ($descriptions as $description) {
            $this->nodes[$description[0]][$description[2]] = $description[1];
            $this->nodes[$description[1]][2] = $description[0];
        }

        $root = new TreeNode($val);
        foreach ($this->nodes as $val => $data) {
            if (!isset($data[2])) {
                $root->val = $val;
                break;
            }
        }

        return $this->setNode($root);
    }

    private function setNode($node): TreeNode
    {
        $data = $this->nodes[$node->val];
        if (isset($data[1])) {
            $node->left = $this->setNode(new TreeNode($data[1]));
        }
        if (isset($data[0])) {
            $node->right = $this->setNode(new TreeNode($data[0]));
        }

        return $node;
    }
}