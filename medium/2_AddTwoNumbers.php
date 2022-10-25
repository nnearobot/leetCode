<?php
/**
 * MIT License
 *
 * Copyright (c) 2022 Rimma Maksiutova
 */

/**
 * 2. Add Two Numbers
 * Medium
 * You are given two non-empty linked lists representing two non-negative integers.
 * The digits are stored in reverse order, and each of their nodes contains a single digit.
 * Add the two numbers and return the sum as a linked list.
 * You may assume the two numbers do not contain any leading zero, except the number 0 itself.
 *
 * Definition for a singly-linked list.
 * class ListNode {
 *     public $val = 0;
 *     public $next = null;
 *     function __construct($val = 0, $next = null) {
 *         $this->val = $val;
 *         $this->next = $next;
 *     }
 * }
 */
class Solution {

    /**
     * @param ListNode $l1
     * @param ListNode $l2
     * @return ListNode
     */
    public function addTwoNumbers($l1, $l2)
    {
        $next1 = $l1;
        $next2 = $l2;
        $prevReg = 0;
        $sumList = null;
        $prevList = null;

        do {
            $sum = $prevReg;
            if (isset($next1)) {
                $sum += $next1->val;
            }
            if (isset($next2)) {
                $sum += $next2->val;
            }

            $prevReg = 0;
            if ($sum > 9) {
                $prevReg = 1;
                $sum = $sum - 10;
            }

            $next = new ListNode($sum);
            if (!isset($sumList)) {
                $sumList = $next;
            }

            if (isset($prevList)) {
                $prevList->next = $next;
            }
            $prevList = $next;

            $next1 = $next1->next;
            $next2 = $next2->next;
        } while (isset($next1) || isset($next2) || $prevReg > 0);

        return $sumList;
    }
}