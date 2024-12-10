(uiop:define-package aoc24.day.nine
  (:use #:cl #:iterate)
  (:import-from #:aoc24
   :get-input))
(in-package #:aoc24.day.nine)

(defparameter *test-input* "2333133121414131402")

(defparameter *input* (get-input 9))

(defun split-chars-to-int (s)
  (map 'list #'digit-char-p s))

(defun parse (input)
  (coerce  (let ((block-id 0))
             (iter (for (file space) on (split-chars-to-int input) by #'cddr)
               (nconcing (nconc  (make-list file :initial-element block-id)
                                 (when space (make-list space :initial-element #\.))))
               (incf block-id)))
           'vector ))

(defun frag (disk)
  (iter
    (for blk index-of-vector disk downto 0)
    (for val = (aref disk blk))
    (for nxt = (position #\. disk))
    (when (and  (numberp val) (> blk nxt))
      (rotatef (aref disk blk) (aref disk nxt))))
  disk)

(defun gen-checksum (disk)
  (let ((idx -1))
    (reduce #'(lambda (prv val)
                (incf idx)
                (+ prv (* idx val)))
            (fset:filter #'numberp disk)
            :initial-value 0)))

(defun solve (input)
  (gen-checksum (frag (parse input))))

(solve *test-input*)
(solve *input*)
