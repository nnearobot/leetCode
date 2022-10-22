<?php
/**
 * MIT License
 *
 * Copyright (c) 2022 Rimma Maksiutova
 */

class Solution {
    /**
     * @param String[][] $board
     * @return Boolean
     */
    function isValidSudoku($board): bool
    {
        foreach ($board as $arr) {
            $tmpArr = [];
            foreach ($arr as $val) {
                if ($val != '.') {
                    $tmpArr[] = $val;
                }
            }
            if (count($tmpArr) != count(array_unique($tmpArr))) {
                return false;
            }
        }

        for ($c = 0; $c < 9; $c++) {
            $tmpArr = [];
            foreach (array_column($board, $c) as $val) {
                if ($val != '.') {
                    $tmpArr[] = $val;
                }
            }
            if (count($tmpArr) != count(array_unique($tmpArr))) {
                return false;
            }
        }

        $tmpArr = [];
        foreach ($board as $row => $rowArr) {
            foreach ($rowArr as $col => $val) {
                if ($val != '.') {
                    $tmpArr[floor($row / 3)][floor($col / 3)][] = $val;
                }
            }
        }
        foreach ($tmpArr as $rowArr) {
            foreach ($rowArr as $arr) {
                if (count($arr) != count(array_unique($arr))) {
                    return false;
                }
            }
        }

        return true;
    }
}

// $board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]];
$board = [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
];


$solution = new Solution();
echo $solution->isValidSudoku($board)."\n\n";
