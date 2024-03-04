(defpackage #:utils
  (:use :cl)
  (:export :?
   :** :1-to
   :sum :dividesp))

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
