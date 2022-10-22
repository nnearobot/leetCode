<?php
/**
 * MIT License
 *
 * Copyright (c) 2022 Rimma Maksiutova
 */

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
    /**
     * @param TreeNode $root
     * @return Integer[]
     */
    function inorderTraversal(TreeNode $root = null): array
    {
        if (!$root || !isset($root->val)) {
            return [];
        }

        $res = [];
        $res = array_merge($res, $this->inorderTraversal($root->left));
        $res[] = $root->val;
        $res = array_merge($res, $this->inorderTraversal($root->right));

        return $res;
    }
}