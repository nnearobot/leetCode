<?php
/**
 * MIT License
 *
 * Copyright (c) 2022 Rimma Maksiutova
 */

/**
 * Medium
 * Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
 *
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
    private $queue = [];

    /**
     * @param TreeNode $root
     * @return Integer[][]
     */
    function levelOrder($root) {
        $res = [];

        $this->enqueue($root);

        while (count($this->queue)) {
            list($nodeLvl, $node) = $this->dequeue();

            $res[$nodeLvl][] = $node->val;

            $this->enqueue($node->left, $nodeLvl + 1);
            $this->enqueue($node->right, $nodeLvl + 1);
        }

        return $res;
    }

    private function enqueue(TreeNode $node = null, int $lvl = 0)
    {
        if ($node) {
            $this->queue[$lvl][] = $node;
        }
    }

    private function dequeue(): array {
        foreach ($this->queue as $lvl => &$arr) {
            $el = array_shift($arr);
            if (!count($arr)) {
                unset($this->queue[$lvl]);
            }
            break;
        }

        return [$lvl, $el];
    }
}