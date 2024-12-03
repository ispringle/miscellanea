(uiop:define-package aoc24
  (:use #:cl))
(in-package #:aoc24)

(named-readtables:defreadtable
    :sugar
  (:merge :fn.reader))
