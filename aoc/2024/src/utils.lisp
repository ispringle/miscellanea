(uiop:define-package aoc24.utils
  (:use #:cl)
  (:export #:list= #:within-range))
(in-package aoc24.utils)

(defun list= (l1 l2 &optional (test #'equal))
  (loop for i in l1
        for j in l2
        always (funcall test i j)))

(defun within-range (l min max)
  (loop for i from 0 below (1- (length l))
        always (let* ((current (nth i l))
                      (next (nth (1+ i) l))
                      (diff (abs (- current next))))
                 (and (<= min diff) (>= max diff)))))
