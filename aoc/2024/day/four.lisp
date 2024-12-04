(uiop:define-package aoc24.day.four
  (:use #:cl #:iterate)
  (:import-from #:aoc24
   :get-input)
  (:import-from #:str
   :lines))
(in-package #:aoc24.day.four)

(defparameter *test-input* "MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX")

(defparameter *input* (get-input 4))

(defun rotl (l)
  (mapcar #'reverse
          (apply #'mapcar #'list l)))

(defun word-forward-p (row word)
  (cond
    ((equal 0 (length word)) t)
    ((equal 0 (length row)) nil)
    ((char= (car word) (car row))
     (find-word-forward (cdr row) (cdr word)))))

(defun word-diaganol-p (grid word &optional (col 0))
  (cond
    ((equal 0 (length word)) t)
    ((equal 0 (length grid)) nil)
    ((equal 0 (length (car grid))) nil)
    ((>= col (length (car grid))) nil)
    ((char= (car word) (nth col (car grid)))
     (find-word-diaganol (cdr grid) (cdr word) (1+ col)))))

(defun tally-word (grid word)
  (cond
    ((not (char= (car word) (car (car grid)))) 0)
    ((and (word-forward-p (car grid) word)
          (word-diaganol-p grid word)) 2)
    ((or (word-forward-p (car grid) word)
         (word-diaganol-p grid word)) 1)
    (t 0)))

(defun subseq-2d (grid x y)
  (mapcar #'(lambda (row) (subseq row x)) (subseq grid y)))

(defun solve (input)
  (let* ((grid 
           (mapcar #'(lambda (s) (coerce s 'list)) (lines input)))
         (grid90 (rotl grid)) (grid180 (rotl grid90))
         (grid270 (rotl grid180)) (search-term '(#\X #\M #\A #\S)))
    (iter (for y below (length grid))
      (sum (iter (for x below (length (car grid)))
             (sum (iter (for g in (list grid grid90 grid180 grid270))
                    (sum (tally-word (subseq-2d g x y) search-term)))))))))

(solve *input*)
