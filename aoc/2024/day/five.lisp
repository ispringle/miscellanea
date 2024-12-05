(uiop:define-package aoc24.day.five
  (:use #:cl #:iter)
  (:import-from #:aoc24
   :get-input))
(in-package #:aoc24.day.five)

(defparameter *test-input* "47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47")

(defparameter *input* (get-input 5))

(defun parse (s sep)
  (mapcar #'(lambda (line)
              (mapcar #'parse-integer (str:split sep line)))
          (str:lines s)))

(defun ordered-p (update sorter)
  (iter (for (a b) on update)    ; iterate pairwise
    (while b)                    ; while a is not the last number in the update
    (unless (funcall sorter a b) ; test if a precedes b in rules
      (return nil))              ; if a does not precde b, return nil
    (finally (return t))))       ; if the end of the update is reached, return t

(defun mid (l)
  (nth (/ (1- (length l)) 2) l))

(defun solve (input)
  (let* ((inpt (str:split "\\n\\n" input :regex t))
         (rules (parse (car inpt) "|"))
         (updates (parse (cadr inpt) ","))
         (sorter (lambda (a b) (member `(,a ,b) rules :test #'equal))))
    (iter (for update in updates)
      (if (ordered-p update sorter)
          (sum (mid update) into one)
          (sum (mid (sort update sorter)) into two))
      (finally (return (list one two))))))

(solve *input*)
