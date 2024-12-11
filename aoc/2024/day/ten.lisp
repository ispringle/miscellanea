(uiop:define-package aoc24.day.ten
  (:use #:cl #:iterate)
  (:import-from #:aoc24
   :get-input)
  (:import-from #:str
   :lines))
(in-package #:aoc24.day.ten)

(defparameter *test-input* "89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732")

(defparameter *input* (get-input 10))

(defun parse (s)
  (let ((grid (make-hash-table :test #'equalp)))
    (iter (for row-string in (lines s))
          (for row from 0)
          (iter (for char in-string row-string)
                (for col from 0)
                (for height = (digit-char-p char))
                (when height  ; Skip any non-digit characters
                  (setf (gethash (complex row col) grid) height))))
    grid))

(defun neighbors (pos)
  (list (+ pos #C(1 0))   ; down
        (+ pos #C(-1 0))  ; up
        (+ pos #C(0 1))   ; right
        (+ pos #C(0 -1)))) ; left

(defun find-peaks-from-trailhead (grid start)
  (let ((peaks (make-hash-table :test #'equalp))
        (visited (make-hash-table :test #'equalp)))
    (labels ((dfs (pos)
               (let ((current-height (gethash pos grid)))
                 (when (= current-height 9)
                   (setf (gethash pos peaks) t))
                 (iter (for next in (neighbors pos))
                       (for next-height = (gethash next grid))
                       (when (and next-height
                                (= next-height (1+ current-height))
                                (not (gethash next visited)))
                         (setf (gethash next visited) t)
                         (dfs next))))))
      (setf (gethash start visited) t)
      (dfs start))
    (hash-table-count peaks)))

(defun solve (input)
  (let* ((grid (parse input))
         (trailheads (iter (for (pos height) in-hashtable grid)
                          (when (zerop height)
                            (collect pos)))))
    (iter (for start in trailheads)
          (sum (find-peaks-from-trailhead grid start)))))

(solve *input*)
