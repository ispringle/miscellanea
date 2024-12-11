(uiop:define-package aoc24.day.eleven
  (:use #:cl #:let-plus)
  (:import-from #:aoc24
   :get-input)
  (:import-from #:str
   :split))
(in-package #:aoc24.day.eleven)

(declaim (optimize (speed 3) (space 1) (debug 0)))

(defparameter *test-input* "125 17")

(defparameter *input* (get-input 11))

(defun parse (s)
  (mapcar #'parse-integer
          (split " " s :omit-nulls t)))

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

(defun count-stones-re (stone blinks total-blinks &optional (cache (make-hash-table :test 'equal)))
  (let ((cache-key (list stone blinks)))
    (or (gethash cache-key cache)
        (let ((result (cond 
                        ((= blinks total-blinks) 1)
                        ((zerop stone) (count-stones-re 1 (1+ blinks) total-blinks cache))
                        ((evenp (count-digits stone))
                         (let+ (((left right) (split-number stone)))
                           (+ (count-stones-re left (1+ blinks) total-blinks cache)
                              (count-stones-re right (1+ blinks) total-blinks cache))))
                        (t (count-stones-re (* stone 2024) (1+ blinks) total-blinks cache)))))
          (setf (gethash cache-key cache) result)
          result))))

(defun count-stones (stones total-blinks)
  (reduce #'+ (mapcar (lambda (n) (count-stones-re n 0 total-blinks)) 
                      stones)))

(defun solve (input)
  (let ((stones (parse input)))
    (list (count-stones stones 25)
          (count-stones stones 75))))

(solve *input*)
