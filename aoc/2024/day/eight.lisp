(uiop:define-package aoc24.day.eight
  (:use #:cl #:let-plus)
  (:import-from #:aoc24
   :get-input)
  (:import-from #:str
   :lines))
(in-package #:aoc24.day.eight)

(defparameter *test-input* "")

(defparameter *input* (get-input 8))

(defun solve (input)
  input)

(solve *test-input*)
(solve *input*)

(defun read-grid (input)
  (loop for line in (lines input)
        collect (coerce (string-trim '(#\Space #\Newline) line) 'list)))

(defun collinear-p (p1 p2 p3)
  "Return `t' if all three points are collinear, else `nil'."
  (let+ (((x1 y1) p1) ((x2 y2) p2) ((x3 y3) p3))
    (= (/ (- y2 y1) (- x2 x1))
       (/ (- y3 y2) (- x3 x2)))))

(defun collinear-point (p1 p2 n)
  "Finds a point collinear to `p1' & `p2' which is `n' away."
  (let+ (((x1 y1) p1) ((x2 y2) p2)
         (dx (- x2 x1)) (dy (- y2 y1))
         (distance (sqrt (+ (* dx dy) (* dy dy))))
         (unit-x (/ dx distance)) (unit-y (/ dy distance)))
    (list (+ x1 (* n unit-x)) (+ y1 (* n unit-y)))))

(collinear-point '(0 0) '(1 1) 2)
(collinear-p '(1 2) '(4 5) '(4 5))
