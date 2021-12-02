#lang racket

(define i (file->list "input.txt"))

(foldl 
  (λ (xs acc)
     (if (< (first xs) (second xs)) (+ 1 acc ) acc))
  0 (map list (append (list (car i)) (reverse (cdr (reverse i)))) i))

(foldl
  (λ (xs acc)
     (if (< (first xs) (second xs)) (+ 1 acc ) acc))
  0 (map list (reverse (drop (reverse i) 3)) (drop i 3)))
