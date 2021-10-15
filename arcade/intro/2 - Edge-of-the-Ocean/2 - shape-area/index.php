<?php

    function shapeArea($n) {
        return $n * ($n -1) * 2 + 1;
    }

    function shapeAreaV2($n) {
        return $n * $n + ($n -1) * ($n - 1);
    }
