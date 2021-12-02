; Import the racket language module
#lang racket

; read input file to a list
(define i (file->list "input.txt"))

;Part One
; fold left, a poor man's reduce.  foldl takes three inputs, a function, the
; initial value, and the list to iterate through.
(foldl 
  ; anon func, takes the current list value (in our case a pair of numbers) and
  ; fold's accumulator
  (λ (xs acc)
     ; if the first item in the pair (the previous reading) is less than the
     ; second item (the current reading) increment the accumulator by 1,
     ; otherwise just return the accumulator
     (if (< (first xs) (second xs)) (+ 1 acc ) acc))
  ; 0 is the initial value of the accumulator.
  0
  ; map over items in _two_ lists, running list on each and returning that new
  ; list of pairs in a new list.
  (map list
       ; we need a new list that has the _first_ value in the original list
       ; twice, and the _final_ value in the original list dropped. So we get
       ; the first value of i (car i) and then we get all but the last element
       ; of i. This is a little convoluted in Scheme/Racket, so we have to
       ; reverse the list, than tail it (getting all but the first value, which
       ; is now the last value of i) andthen we _unreverse_ the list to get it
       ; back in the original order, sans the last value
       (append (list (car i)) (reverse (cdr (reverse i))))
       i))

;Part Two
; This is nearly identical to part one, except we have to iterate over three
; fewer elements! This is given a floating window of '(a b c d), we will get
; back '(a b c) and '(b c d).  The values b and c are the same, so the thing
; that determines which value is greater is the first element of the previous
; window and the last element of the last window. Thus, we take input, zip
; together the two lists again, but this time one list starts at the 4th value
; and the other list is missing the last 3 values. Everything below is the same
; as above except where I have added additional comments.
(foldl
  (λ (xs acc)
     (if (< (first xs) (second xs)) (+ 1 acc ) acc))
  0 (map list
         ; Reverse the list, drop the three elements (which are now at the
         ; head, but were at the tail before) and then reverse the list to
         ; revert to the original order.
         (reverse (drop (reverse i) 3))
         ; Drop the first three elements
         (drop i 3)))
