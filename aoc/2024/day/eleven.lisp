(uiop:define-package aoc24.day.eleven
  (:use #:cl #:iterate #:let-plus)
  (:import-from #:aoc24
   :get-input)
  (:import-from #:str
   :split))
(in-package #:aoc24.day.eleven)

(declaim (optimize (speed 3) (space 1) (debug 0)))

(defparameter *test-input* "125 17")

(defparameter *input* (get-input 11))

(defun parse (s)
  (coerce (mapcar #'parse-integer
                  (split " " s :omit-nulls t))
          'vector))

(defun count-digits (n)
  "Count the number of digits in `n'."
  (1+ (floor (log (max 1 n) 10))))

(defun split-number (n)
  "Split number `n' into left and right digit halves.
Example (split-number 1234) => 12 34"
  (let* ((div (expt 10 (floor (count-digits n) 2)))
         (left (floor n div))
         (right (mod n div)))
    (list left right)))

(defun split-stone (stone)
  (let+ (((left right) (split-number stone)))
    (list left right)))

(defun transform-stone (stone)
  (declare (type integer stone))
  (cond 
    ((= stone 0) (list 1))
    ((evenp (count-digits stone)) (split-stone stone))
    (t (list (* stone 2024)))))

(defun blink (stones)
  (declare (type (vector integer) stones))
  (let* ((transformed (make-array (max 2 (* 2 (length stones)))
                                  :element-type 'integer
                                  :adjustable t
                                  :fill-pointer 0)))
    (iter
      (for stone in-vector stones)
      (iter (for new-stone in (transform-stone stone))
        (vector-push-extend new-stone transformed)))
    transformed))

(defun do-blink (stones blink-cnt)
  (iter
    (repeat blink-cnt)
    (setf stones (blink stones)))
  (length stones))

(defun solve (input)
  (do-blink (parse input) 75))

(solve *test-input*)
(solve *input*)
