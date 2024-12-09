(uiop:define-package aoc24.day.seven
  (:use #:cl)
  (:import-from #:aoc24
   :get-input)
  (:import-from #:str
   :lines :split))
(in-package #:aoc24.day.seven)

(defparameter *test-input* "190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20")

(defparameter *input* (get-input 7))

(defun length-of-int (int)
  (or (and (zerop int) 0)
      (1+ (floor (log int 10)))))

(defun ends-with (x y)
  (= (mod (- x y) (expt 10 (length-of-int y))) 0))

(defun remove-n (x n)
  (floor x (expt 10 (length-of-int n))))

(defun next-op (target numbers &optional (use-concat nil))
  (let ((n (car (last numbers)))
        (rest (butlast numbers)))
    (if (null rest)
        (equal n target)
        (or (when (zerop (mod target n)) (next-op (/ target n) rest use-concat))
            (when (and use-concat (ends-with target n))
              (next-op (remove-n target n) rest use-concat))
            (next-op (- target n) rest use-concat)))))

(defun check-eqs (calibrations &optional (use-concat nil))
  (apply #'+ (mapcar #'(lambda (test)
                         (if (apply #'next-op (append test (list use-concat)))
                             (car test)
                             0))
                     calibrations)))

(defun solve (input)
  (let ((in (mapcar #'(lambda (line)
                        (let* ((lines (split ": " line))
                               (total (parse-integer (car lines)))
                               (values (mapcar #'parse-integer (split " " (cadr lines)))))
                          (list total values)))
                    (lines input))))
    (list (check-eqs in)
          (check-eqs in t))))

(solve *test-input*)
(solve *input*)
