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

(define (loop-points pts [cnct --])
  (cons (points pts) (cons cnct (car pts))))

(define scale 1)

(define centroid (pt 0 0))
(define inner-distance (* 5 scale))

(define inner-tri (calculate-triangle centroid inner-distance))
(match-define (list inner-a inner-b inner-c) inner-tri)
(define top-tri (calculate-triangle inner-a (* inner-distance 3)))
(match-define (list top-a top-b top-c) top-tri)
(define left-tri (calculate-triangle inner-c (* inner-distance 3)))
(match-define (list left-a left-b left-c) left-tri)
(define right-tri (calculate-triangle inner-b (* inner-distance 3)))
(match-define (list right-a right-b right-c) right-tri)

(define cross-width (dist inner-b top-b))

(define left-segment
  (let*
      ([a inner-b]
       [b (extend-point inner-a inner-b cross-width)]
       [c (extend-point b left-c cross-width)]
       [d (extend-point left-b left-a cross-width)]
       [e top-a]
       [f top-c]
       [g inner-b])
    (list a b c d e f g)))

(define right-segment
  (let*
      ([a inner-c]
       [b right-a]
       [c (extend-point right-a right-b cross-width)]
       [d (extend-point right-c right-b cross-width)]
       [e (extend-point d (extend-point top-c top-a cross-width) (* 2 cross-width))]
       [f (extend-point c b (* 3 cross-width))]
       [g (extend-point c b cross-width)]
       [h top-c]
       [i inner-c])
    (list a b c d e f g h i)))

(define bottom-segment
  (let*
      ([a inner-a]
       [b right-a]
       [c (extend-point right-a right-b cross-width)]
       [d (extend-point left-a left-c cross-width)]
       [e (extend-point left-b left-c cross-width)]
       [f left-b]
       [g inner-b])
    (list a b c d e f g)))

(define top-left-segment
  (let*
      ([a (extend-point right-b right-a cross-width)]
       [b (extend-point right-a a (* 2 cross-width))]
       [d (extend-point inner-a left-a cross-width)]
       [c (extend-point left-a d (* 2 cross-width))])
    (list a b c d)))

(define top-segment
  (let*
      ([a (extend-point right-b right-a (* 3 cross-width))]
       [b (extend-point inner-a left-a (* 3 cross-width))]
       [c (extend-point right-a a cross-width)]
       [d (find-point b c (rad 120) #t cross-width)])
    (list a b c d)))

(define red (make-color* 157 31 36))
(define blue (make-color* 63 93 167))

(define win-max (* 60 scale))
(define win-min (* win-max -1))
(with-window (window win-min win-max win-min win-max)
  (draw
   (filldraw (curve (points right-segment)) red "black")
   (filldraw (curve (points left-segment)) "white" "black")
   (filldraw (curve (points top-segment)) "white" "black")
   (filldraw (curve (points bottom-segment)) blue "black")
   (filldraw (curve (points top-left-segment)) blue "black")))