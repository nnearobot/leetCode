<?php
/**
 * MIT License
 *
 * Copyright (c) 2022 Rimma Maksiutova
 */

class Solution {
    private $window = [];
    private $t = 0;

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @param Integer $t
     * @return Boolean
     */
    function containsNearbyAlmostDuplicate($nums, $k, $t) {
        if (!$k) {
            return false;
        }

        $this->t = $t;

        $this->window = [$nums[0]]; // sliding window

        for ($i = 1; $i < count($nums); $i++) {
            if ($i > $k) {
                // if the first element of the k-els-window is equal to the next one,
                // it's the same state, so there is nothing to check
                if ($nums[$i] == $nums[$i - $k - 1]) {
                    continue;
                }
                array_splice($this->window, array_search($nums[$i - $k - 1], $this->window), 1, []);
            }


            if ($nums[$i] >= $this->window[count($this->window) - 1]) {
                if ($this->isNumsAreNearby($nums[$i], $this->window[count($this->window) - 1])) {
                    return true;
                }
                $this->window[] = $nums[$i];
                continue;
            }

            if ($nums[$i] <= $this->window[0]) {
                if ($this->isNumsAreNearby($nums[$i], $this->window[0])) {
                    return true;
                }
                array_unshift($this->window, $nums[$i]);
                continue;
            }

            $upperIndex = $this->getUpperIndex($nums[$i]);
            if ($this->isNumsAreNearby($nums[$i], $this->window[$upperIndex])) {
                return true;
            }

            $lowerIndex = $this->getLowerIndex($nums[$i], $upperIndex);
            if ($this->isNumsAreNearby($nums[$i], $this->window[$lowerIndex])) {
                return true;
            }

            array_splice($this->window, $lowerIndex + 1, 0, $nums[$i]);
        }

        return false;
    }

    private function isNumsAreNearby($num1, $num2)
    {
        return (abs($num1 - $num2) <= $this->t);
    }

    private function getUpperIndex($num)
    {
        $indUpper = count($this->window) - 1;
        $indLower = 0;

        if ($num < $this->window[$indLower]) {
            return $indLower;
        }

        while ($indUpper > $indLower) {
            $centerInd = $indLower + ceil(($indUpper - $indLower) / 2);
            if ($centerInd == $indUpper) {
                break;
            }
            if ($num >= $this->window[$centerInd]) {
                $indLower = $centerInd;
            } else {
                $indUpper = $centerInd;
            }
        };

        return $centerInd;
    }

    private function getLowerIndex($num, $upperIndex)
    {
        if (!$upperIndex) {
            return 0;
        }

        $indLower = 0;
        $indUpper = $upperIndex;

        if ($num >= $this->window[$indUpper]) {
            return $indUpper;
        }

        while ($indUpper > $indLower) {
            $centerInd = $indLower + floor(($indUpper - $indLower) / 2);
            if ($centerInd == $indLower) {
                break;
            }
            if ($num < $this->window[$centerInd]) {
                $indUpper = $centerInd;
            } else {
                $indLower = $centerInd;
            }
        };

        return $centerInd;
    }

}

/*

[-133377540,-49518270,114953848,-38541241,-209515557,-86864903,-22714637,212614133,-106142289,73366795,-244791457,222381196,251988775,-256363523,-128817321,118463226,-222813561,66939415,151245440,-24290898,-211009113,-130082670,-224483461,-114359812,220160656,-26276063,-206936941,-11836477,-63872203,-128350686,2105381,143826569,89028665,-94883742,-5189725,110419253,57130308,15866312,42261386,14681793,-56630082,47018107,2201999,1876515,-177816570,-166786428,132535436,-87838021,130827492,-210230492,-101624960,-147250314,-6356605,180340531,43077742,-50888453,221214686,-111453711,-116315557,10243319,-171888156,-50753906,8905485,-199998100,-171574747,-69053551,-249763800,-40288416,-204819319,-36869913,-184562204,-32688012,-50705283,-94566765,-88821316,-143916036,139232717,-26215490,-48027759,252344499,33753677,-235536117,138232202,-200420014,211136143,-220469485,-102015020,87903247,88281996,-216903120,225542089,48435460,66405575,241261758,66279757,57050131,-34697163,18312433,-53491241,-1969...
6387
12886

 */