<?php
/**
 * MIT License
 *
 * Copyright (c) 2022 Rimma Maksiutova
 */


/**
 * This solution prints logs for checking purpose.
 * Remove these all before submitting to LeetCode.
 */
class Solution {
    const LAST_KEY = 8;

    private $board = [];
    private $map = [];
    private $threeXthree = [0 => [0 => [], 1 => [], 2 => []], 1 => [0 => [], 1 => [], 2 => []], 2 => [0 => [], 1 => [], 2 => []]];
    private $emptyCellQty = 0;
    private $removed = 0;

    /**
     * @param String[][] $board
     * @return NULL
     */
    function solveSudoku(&$board)
    {
        $this->board = $board;

        foreach ($this->board as $row => $rowArr) {
            echo implode(' ', $rowArr)."\n";
            foreach ($rowArr as $col => $val) {
                if ($val == ".") {
                    $this->emptyCellQty++;
                } else {
                    $this->addToThreeXthree($this->threeXthree, $row, $col, $val);
                }
            }
        }

        echo "\nEmpty cells: {$this->emptyCellQty}\n\n";
        echo "Fill all possible cells and create a map of the possible numbers of another cells:\n";

        $fillRes = $this->fillBoard($this->board, $this->threeXthree, $this->map, $this->emptyCellQty);
        if ($fillRes) {
            $this->board = $fillRes['board'];
            $this->threeXthree = $fillRes['threeXthree'];
            $this->map = $fillRes['map'];
            $this->emptyCellQty = $fillRes['emptyCellQty'];
        }

        $this->printLog();

        if (!$this->emptyCellQty) {
            if ($this->testBoardIsCorrect()) {
                echo "Board is correct\n\n";
            } else {
                echo "BOARD IS NOT CORRECT\n\n";
            }

            $board = $this->board;

            return;
        }

        echo "As a board is still has not been filled, testing possible numbers of an empty cells\n";
        $testRow = $testCol = $testNum = 0;
        do {
            if (empty($this->map[$testRow][$testCol])) {
                list($testRow, $testCol) = $this->getNextCell($testRow, $testCol);

                continue;
            }

            $tmpBoard = $this->board;
            $tmpMap = $this->map;
            $tmpThreeXthree = $this->threeXthree;
            $tmpEmptyCellQty = $this->emptyCellQty;

            $testVal = $this->map[$testRow][$testCol][$testNum]; // get a possible number for this cell
            echo "\nTesting a cell [$testRow, $testCol] with number $testVal:\n";

            $tmpBoard[$testRow][$testCol] = strval($testVal);
            $tmpMap[$testRow][$testCol] = [];
            $this->addToThreeXthree($tmpThreeXthree, $testRow, $testCol, $testVal);
            $tmpEmptyCellQty--;

            $fillRes = $this->fillBoard($tmpBoard, $tmpThreeXthree, $tmpMap, $tmpEmptyCellQty);

            if ($fillRes) {
                $testNum++;
                $this->printLog();
            } else {
                $this->removeFromMap($testRow, $testCol, $testVal);
            }

            if (!isset($this->map[$testRow][$testCol][$testNum])) {
                // if this is a final map cell...
                if ($testRow == self::LAST_KEY && $testCol == self::LAST_KEY) {
                    //...and nothing was removed from the map, quit this processing
                    if (!$this->removed) {
                        echo "\nNothing was removed within last iteration - quit\n\n";
                        break;
                    } else {
                        //...or continue with new iteration and reset the counter
                        echo "\nREMOVED: $this->removed. Continue with new iteration.\n\n";
                        $this->removed = 0;
                    }
                }

                list($testRow, $testCol) = $this->getNextCell($testRow, $testCol);

                $testNum = 0;
            }
        } while ($this->emptyCellQty > 0);

        if ($this->testBoardIsCorrect()) {
            echo "Board is correct\n\n";
        } else {
            echo "BOARD IS NOT CORRECT\n\n";
        }

        $board = $this->board;
    }

    private function printLog()
    {
        echo "\n\nCurrent board:\n";
        foreach ($this->board as $rowArr) {
            echo implode(' ', $rowArr)."\n";
        }

        echo "\n\nCurrent 3x3:\n";
        foreach ($this->threeXthree as $rowArr) {
            $resArr = [];
            foreach ($rowArr as $cellArr) {
                $resArr[] = '['.implode(' ', $cellArr).']';
            }
            echo implode(' ', $resArr)."\n";
        }

        echo "\n\nCurrent map:\n";
        foreach ($this->map as $row => $rowArr) {
            $resArr = [];
            foreach ($rowArr as $col => $cellArr) {
                $resArr[] = $col.':['.implode(' ', $cellArr).']';
            }
            echo $row.' - '.implode(' ', $resArr)."\n";
        }

        echo "\nEmpty cells: {$this->emptyCellQty}\n\n";
    }

    private function getNextCell(int $currentRow, int $currentCol): array
    {
        $currentCol++;
        if ($currentCol > self::LAST_KEY) {
            $currentCol = 0;
            $currentRow++;
        }
        if ($currentRow > self::LAST_KEY) {
            $currentRow = 0;
        }

        return [$currentRow, $currentCol];
    }

    private function fillBoard(array $board, array $threeXthree, array $map, int $emptyCellQty): ?array
    {
        do {
            $prevEmptyCellQty = $emptyCellQty;

            // for each cell in the board...
            foreach ($board as $row => $rowArr) {
                foreach ($rowArr as $col => $val) {
                    if ($val != ".") {
                        $map[$row][$col] = [];
                        continue;
                    }

                    //...process if it is empty...
                    if (!empty($map[$row][$col])) {
                        $testNumbers = $map[$row][$col];
                    } else {
                        $testNumbers = range(1, 9);
                    }

                    $map[$row][$col] = [];
                    //...test all $testNumbers [1...9]...
                    foreach ($testNumbers as $num) {
                        if ($this->isNumberAllowedForCell($num, $row, $col, $board, $threeXthree)) {
                            $map[$row][$col][] = $num; // save this number as potentially possible for this cell.
                        }
                    }

                    // if we can't find at least one possible number for this cell, it is an error
                    if (!count($map[$row][$col])) {
                        echo "Can't find possible number for cell [$row, $col]\n";

                        return null;
                    }

                    // if there is only one possible number for this cell, then this is an actual number for it
                    if (count($map[$row][$col]) == 1) {
                        $val = reset($map[$row][$col]);
                        $board[$row][$col] = strval($val); // put this number to this cell on the board
                        $this->addToThreeXthree($threeXthree, $row, $col, $val); // put this number to the 3x3 array
                        $emptyCellQty--;
                        echo "\$board[{$row}][{$col}] = ".$val."\n";
                        $map[$row][$col] = [];
                    }
                }
            }
        } while ($emptyCellQty > 0 && $prevEmptyCellQty != $emptyCellQty);

        return ['board' => $board, 'threeXthree' => $threeXthree, 'map' => $map, 'emptyCellQty' => $emptyCellQty];
    }

    private function isNumberAllowedForCell(int $num, int $row, int $col, array $board, array $threeXthree)
    {
        return !in_array(strval($num), $board[$row]) //...if the row of this cell does not include this number...
            && !in_array(strval($num), array_column($board, $col)) //...and if the coll of this cell does not include this number...
            && !$this->isInThreeXthree($threeXthree, $row, $col, $num); //...and if the 3x3 sub-box of this cell does not include this number...
    }

    private function addToThreeXthree(&$threeXthree, $row, $col, $val)
    {
        $threeRow = floor($row / 3);
        $threeCol = floor($col / 3);
        $threeXthree[$threeRow][$threeCol][] = $val;
        $threeXthree[$threeRow][$threeCol] = array_unique($threeXthree[$threeRow][$threeCol]);
        sort($threeXthree[$threeRow][$threeCol]);
    }

    private function isInThreeXthree($threeXthree, $row, $col, $num)
    {
        return in_array($num, $threeXthree[floor($row / 3)][floor($col / 3)]);
    }

    private function removeFromMap(int $row, int $col, int $testVal)
    {
        foreach ($this->map[$row][$col] as $k => $v) {
            if ($v == $testVal) {
                unset($this->map[$row][$col][$k]);
                break;
            }
        }
        $this->map[$row][$col] = array_values($this->map[$row][$col]);
        $this->removed++;

        $this->printLog();

        if (count($this->map[$row][$col]) != 1) {
            return;
        }

        $num = reset($this->map[$row][$col]);
        $this->board[$row][$col] = strval($num);
        $this->addToThreeXthree($this->threeXthree, $row, $col, $num);
        $this->map[$row][$col] = [];
        $this->emptyCellQty--;

        // as we filled cell, we must check all the associated maps and remove this number from them
        foreach ($this->map as $r => $rarr) {
            foreach ($rarr as $c => $arr) {
                if (empty($arr)) {
                    continue;
                }
                if ($r == $row && $c == $col) { // skip the same cell
                    continue;
                }
                if ($r == $row || $c == $col || (floor($r / 3) == floor($row / 3) && floor($c / 3) == floor($col / 3))) {
                    foreach ($arr as $i => $n) {
                        if (!$this->isNumberAllowedForCell($n, $r, $c, $this->board, $this->threeXthree)) {
                            $this->removeFromMap($r, $c, $n);
                        }
                    }
                }
            }
        }

    }

    private function testBoardIsCorrect(): bool
    {
        $testArr = range(1, 9);

        foreach ($this->board as $arr) {
            if (count(array_unique($arr)) != count($testArr)) {
                return false;
            }
        }

        for ($c = 0; $c <= self::LAST_KEY; $c++) {
            if (count(array_unique(array_column($this->board, $c))) != count($testArr)) {
                return false;
            }
        }

        $threeXthree = [];
        foreach ($this->board as $row => $rowArr) {
            foreach ($rowArr as $col => $val) {
                $this->addToThreeXthree($threeXthree, $row, $col, $val);
            }
        }
        foreach ($threeXthree as $rowArr) {
            foreach ($rowArr as $arr) {
                if (count(array_unique($arr)) != count($testArr)) {
                    return false;
                }
            }
        }

        return true;
    }
}


// test data

//$board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]];
//$board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]];
//$board = [[".",".",".","2",".",".",".","6","3"],["3",".",".",".",".","5","4",".","1"],[".",".","1",".",".","3","9","8","."],[".",".",".",".",".",".",".","9","."],[".",".",".","5","3","8",".",".","."],[".","3",".",".",".",".",".",".","."],[".","2","6","3",".",".","5",".","."],["5",".","3","7",".",".",".",".","8"],["4","7",".",".",".","1",".",".","."]];
$board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]];

$solution = new Solution();
$solution->solveSudoku($board);

