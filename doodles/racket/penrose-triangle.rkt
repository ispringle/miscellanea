#lang racket
(require metapict)

(define extend-point
  (lambda (a b extn)
    "Extends line AB by extn, returns the point extended beyond b"
    (define ab (dist a b))
    (define calc (lambda (n1 n2) (+ n1 (* (/ (- n1 n2) ab) extn))))
    (pt (calc (pt-x b) (pt-x a)) (calc (pt-y b) (pt-y a)))))

(define find-point
  (lambda (a b ∠abc cw [bc (dist a b)])
    "Finds point C given A, B, the angle of ABC, and optionally the distance bc."
    (define ∠ab (atan (- (pt-y a) (pt-y b)) (- (pt-x a) (pt-x b))))
    (if cw
        (pt (+ (pt-x b) (* bc (cos (+ ∠ab ∠abc))))
            (+ (pt-y b) (* bc (sin (+ ∠ab ∠abc)))))
        (pt (+ (pt-x b) (* bc (cos (- ∠ab ∠abc))))
            (+ (pt-y b) (* bc (sin (- ∠ab ∠abc))))))))

(define (calculate-triangle centroid distance)
  "Calculates an equilateral triangle from a centroid and the distance from the centroid to any given point. This triangle's 'peak' will be point 'up'"
  (define a (pt+ centroid (pt 0 distance)))
  (define b (find-point a centroid (rad 120) #f distance))
  (define c (find-point a centroid (rad 120) #t distance))
  (list a b c))

(define points
  (lambda (pts [cnct --])
    (if (not (null? (cdr pts)))
        (cons (car pts) (cons cnct (points (cdr pts))))
        (car pts))))

(define scale 1)

(define centroid (pt 0 0))
(define inner-distance (* 5 scale))

(define inner-tri (calculate-triangle centroid inner-distance))
(match-define (list inner-a inner-b inner-c) inner-tri)
(define top-tri (calculate-triangle inner-a (* inner-distance 3)))
(match-define (list top-a top-b top-c) top-tri)
(define right-tri (calculate-triangle inner-b (* inner-distance 3)))
(match-define (list right-a right-b right-c) right-tri)

(define cross-width (dist inner-b top-b))

(define segment
  (let*
      ([a inner-c]
       [b right-a]
       [c (extend-point right-a right-b cross-width)]
       [d (extend-point right-c right-b cross-width)]
       [e (extend-point top-c top-a cross-width)]
       [f top-c]
       [g inner-c])
    (list a b c d e f g)))

(define win-max (* 40 scale))
(define win-min (* win-max -1))
(with-window (window win-min win-max win-min win-max)
  (draw
   (filldraw (curve (points segment)) "red" "black")
   (filldraw (rotatedd 120 (curve (points segment))) "blue" "black")
   (filldraw (rotatedd 240 (curve (points segment))) "green" "black")))