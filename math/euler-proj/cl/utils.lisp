(defpackage #:utils
  (:use :cl)
  (:export :?
   :** :1-to
   :sum :dividesp
   :partition :window
   :dowindow))

(in-package #:utils)

(defun 1-to (n)
  (cond ((zerop n) nil)
        (t (cons n (1-to (- n 1))))))

(defun sum (l)
  "Sum list of ints"
  (cond ((not l) 0)
        (t (+ (car l) (sum (cdr l))))))

(defun ? (n)
  (sum (1-to n)))

(defun ** (n)
  (* n n))

(defun dividesp (a b)
  (zerop (mod a b)))

(defun partition (list size)
  (loop for window on list by #'(lambda (list)
                                  (nthcdr size list))
        collecting (subseq window 0 size)))

(defun window (thing size)
  (loop for window on thing
        while (nthcdr (1- size) window)
        collecting (subseq window 0 size)))

(defun dowindow (thing size func)
  (loop for window on thing
        while (nthcdr (1- size) window)
        collecting (apply func (subseq window 0 size))))
