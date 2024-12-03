(uiop:define-package aoc24.day.two
  (:use #:cl)
  (:import-from #:str
   :lines :words)
  (:import-from #:aoc24.utils
   :list= :within-range))
(in-package #:aoc24.day.two)

(defparameter *test-input*
  "7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9")

(defparameter *input* (uiop:read-file-string "input/two.txt"))

(defun is-safep (report)
  (when (and (or (list= report (sort (copy-seq report) #'<))
               (list= report (sort (copy-seq report) #'>)))
           (within-range report 1 3))
      t))

(defun solve (input)
  (let* ((reports (mapcar #'(lambda (line)
                              (mapcar #'parse-integer (words line)))
                          (lines input)))
         (safe-reports (loop for report in reports
                             count (is-safep report) into no-dampening
                             count (or (is-safep report)
                                       (loop for i from 0 below (length report)
                                             thereis (is-safep (concatenate 'list
                                                                        (subseq report 0 i)
                                                                        (subseq report (1+ i)))))) into with-dampening
                             finally (return (list no-dampening with-dampening)))))
    safe-reports))

(solve *input*)
