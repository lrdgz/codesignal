<?php


    function adjacentElementsProduct($inputArray) {
        $result = -1000;
        for ($i = 0; $i < count($inputArray) - 1; $i = $i + 1) {
            $first = $inputArray[$i];
            $sec = $inputArray[$i+1];
            $product = $first * $sec;
            if ($product > $result) {
                $result = $product;
            }
        }
        return $result;
    }

    // print "($i) $first $sec $product |";
    //echo adjacentElementsProduct(array(3, 6, -2, -5, 7, 3)); // 21
    //echo adjacentElementsProduct([1, 2, 3, 0]);              // 6
    echo adjacentElementsProduct([-23, 4, -3, 8, -12]);        // -12