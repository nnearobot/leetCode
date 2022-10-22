<?php
/**
 * MIT License
 *
 * Copyright (c) 2022 Rimma Maksiutova
 */

class TreeNode {
    public $val = null;

    /** @var TreeNode|null  */
    public $left = null;

    /** @var TreeNode|null  */
    public $right = null;

    function __construct($val = 0, TreeNode $left = null, TreeNode $right = null)
    {
      $this->val = $val;
      $this->left = $left;
      $this->right = $right;
    }
}

class Solution {
    function mergeTrees(TreeNode $root1 = null, TreeNode $root2 = null): TreeNode
    {
        $tree = new TreeNode(null);

        if (!isset($root1->val) && !isset($root2->val)) {
            return $tree;
        }

        $tree->val = intval(@$root1->val) + intval(@$root2->val);

        if (isset($root1->left) || isset($root2->left)) {
            $tree->left = $this->mergeTrees(@$root1->left, @$root2->left);
        }

        if (isset($root1->right) || isset($root2->right)) {
            $tree->right = $this->mergeTrees(@$root1->right, @$root2->right);
        }

        return $tree;
    }
}
