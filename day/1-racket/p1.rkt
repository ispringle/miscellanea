#lang racket

(define i (file->list "input.txt"))
(foldl 
  (λ (xs acc)
     (if (< (first xs) (second xs)) (+ 1 acc ) acc))
  0 (map list (append (list (car i)) (reverse (cdr (reverse i)))) i))

(define t (list 1 2 3 4 5 6 7 8 9 10))
(print (for/sum ([x t] [y (drop t 3)] #:when (> y x))1))
