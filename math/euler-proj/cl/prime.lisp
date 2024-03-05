(defpackage #:prime
  (:use :cl)
  (:export :sieve
   :factors :primep
   :next-prime :nth-prime
   :n-primes))

(in-package #:prime)

(require "utils" "utils.lisp")

(defparameter *known-primes* '(2 3 5))

(defun sieve (n)
  "Prime numbers sieve for odd numbers. 
   Returns a list with all the primes that are less than or equal to n."
  (let* ((limit (ash (- n 1) -1))
         (stop (ash (isqrt n) -1))
         (sieve (make-array (+ 1 limit) :element-type 'bit :initial-element 0)))
    (loop for i from 1 to limit
          for odd-number = (1+ (ash i 1))
          when (zerop (sbit sieve i))
            collect odd-number into values
          when (<= i stop)
            do (loop for j from (* i (1+ i) 2) to limit by odd-number
                     do (setf (sbit sieve j) 1))
          finally (return (cons 2 values)))))

(defun list-primep-until (limit)
  "Returns an array of t/nil for each number upto limit.
   If nth n is t, than n is prime, otherwise it's not.
   For example if you would like to know if 7 is prime:
   (aref (list-primep-until 7) 7)

   Note that the array includes limit, but might include more than limit.
   Do not assume that last is limit."
  (declare (type fixnum limit))
  (let ((rez (make-array (list (+ 1 limit)) :initial-element t)))
    (setf (aref rez 0) nil
          (aref rez 1) nil)
    (loop for base from 2 below (+ 1 (floor limit 2))
          do (let ((n (* base 2)))
               (loop
                 (if (<= n limit)
                     (progn (setf (aref rez n) nil)
                            (incf n base))
                     (return)))))
    rez))


(eval-when (:compile-toplevel :load-toplevel :execute))

(defun factors (n)
  "Calculate prime factors of n"
  (declare (type integer n))
  (labels ((next-candidate (cand)
             (cond ((= 2 cand) 3) 
                   (t (+ 2 cand))))
           (rec (n cand facs)
             (cond ((or (= n 1) (> cand n)) facs)
                   ((utils:dividesp n cand) (rec (/ n cand) cand (cons cand facs)))
                   (t (rec n (next-candidate cand) facs)))))
    (rec n 2 nil)))

(defun pseudo-primep (n)
  "Returns t if n is prime or pseudi-prime, otherwise nil.
   Based on Fermat's little theorem."
  (declare (type integer n))
  (let ((a (random n)))
    (= a (mod (expt a n) n))))

(defun primep-fermat (n &optional (tests-n 100))
  "Returns t if n is prime, otherwise nil."
  (declare (type integer n))
  (cond ((>= 1 n) nil)
        ((or (= 2 n)
             (= 3 n)) t)
        ((or (utils:dividesp n 2)
             (utils:dividesp n 3)) nil)
        (t (loop repeat tests-n
                 always (pseudo-primep n)))))

(defun primep-trial-div (n)
  "Check primality by trial-division."
  (declare (type integer n))
  (and (> n 1)
       (or (= n 2) (oddp n))
       (loop for i from 3 to (sqrt n) by 2
             never (zerop (rem n i)))))

(defun primep (n)
  "Check primality."
  (primep-trial-div n))

(defun next-prime (after)
  "Gets next prime number after number after"
  (declare (type integer after))
  (let ((next (if (evenp after) (+ 1 after) (+ 2 after))))
    (cond ((primep next) next)
          (t (next-prime next)))))

(defun nth-prime (n &optional (prime 2))
  "Gets the nth prime. For example (nth-prime 3) => 5"
  (declare (type integer n prime))
  (cond ((= 1 n) prime)
        (t (nth-prime (- n 1) (next-prime prime)))))

(defun n-primes (n &optional (prime 2))
  "Returns the first n primes."
  (declare (type integer n prime))
  (cond ((= 0 n) nil)
        (t (cons prime  (n-primes (- n 1) (next-prime prime))))))
