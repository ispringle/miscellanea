(uiop:define-package aoc24.day.eight
  (:use #:cl #:iterate #:let-plus)
  (:import-from #:aoc24
   :get-input)
  (:import-from #:str
   :lines)
  (:import-from #:alexandria
   :map-combinations))
(in-package #:aoc24.day.eight)

(defparameter *test-input* "............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............")

(defparameter *input* (get-input 8))

(defun parse (s)
  (iter
    (with ants = (make-hash-table :test #'equal))
    (with grid = (make-hash-table :test #'equal :size (length s)))
    (for line in (lines s)) (for row from 0)
    (iter (for col from 0) (for char in-string line)
          (let ((coord (complex row col)))
            (setf (gethash coord grid) t)
            (unless (char= char #\.) (push coord (gethash char ants)))))
    (finally (return (values ants grid)))))

(defun solve (input)
  (let+ (((&values ants grid) (parse input))
         (nodes (make-hash-table))
         (lines (make-hash-table)))
    (maphash #'(lambda (_ locs) (declare (ignore _))
               (map-combinations
                #'(lambda (pair)
                    (let+ ((diff (apply #'- pair)) ((p1 p2) pair))
                      (dolist (loc (list (+ p1 diff) (- p2 diff)))
                        (when (gethash loc grid)
                          (setf (gethash loc nodes) t)))
                      (maphash #'(lambda (loc _) (declare (ignore _))
                                   (when (zerop (imagpart (/ (- loc p1) diff)))
                                     (setf (gethash loc lines) t)))
                               grid)))
                locs :length 2))
             ants)
    (list (hash-table-count nodes)
          (hash-table-count lines))))

(time 
 (solve *input*))
