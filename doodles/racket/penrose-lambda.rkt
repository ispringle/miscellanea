#lang racket
(require metapict)

(define extend-point
    (lambda (a b extn)
      "Extends line AB by extn, returns the point extended beyond b"
      (define calc (lambda (n1 n2) (+ n1 (* (/ (- n1 n2) (dist a b)) extn))))
      (pt (calc (pt-x b) (pt-x a)) (calc (pt-y b) (pt-y a)))))

(define find-point
    (lambda (a b ∠abc cw (bc (dist a b)))
      "Finds point C given A, B, the angle of ABC, and optionally the distance bc."
      (let ((∠ab (atan (- (pt-y a) (pt-y b)) (- (pt-x a) (pt-x b)))))
        (if cw
            (pt (+ (pt-x b) (* bc (cos (+ ∠ab ∠abc))))
                (+ (pt-y b) (* bc (sin (+ ∠ab ∠abc)))))
            (pt (+ (pt-x b) (* bc (cos (- ∠ab ∠abc))))
                (+ (pt-y b) (* bc (sin (- ∠ab ∠abc)))))))))

(define calculate-triangle
    (lambda (centroid distance)
      "Calculates an equilateral triangle from a centroid and the distance from
           the centroid to any given point. This triangle's 'peak' will be point 'up'"
      (let* ((a (pt+ centroid (pt 0 distance)))
             (b (find-point a centroid (rad 120) #f distance))
             (c (find-point a centroid (rad 120) #t distance)))
        (list a b c))))

(define points
    (lambda (pts (cnct --))
      (if (not (null? (cdr pts)))
          (cons (car pts) (cons cnct (points (cdr pts))))
          (car pts))))

(define loop-points
    (lambda (pts (cnct --))
      (cons (points pts) (cons cnct (car pts)))))

(define centroid (pt 0 0))              ; Centroid is the center of the inner-most triangle.
(define inner-distance 5)               ; This is the distance from the centroid to its vertices.

;; Define the points of the guide triangles.
;; These will be used to reference the points of the penrose shape.
(match-define (list inner-a inner-b inner-c)
              (calculate-triangle centroid inner-distance))
(match-define (list top-a top-b top-c)
              (calculate-triangle inner-a (* inner-distance 3)))
(match-define (list left-a left-b left-c)
              (calculate-triangle inner-c (* inner-distance 3)))
(match-define (list right-a right-b right-c)
              (calculate-triangle inner-b (* inner-distance 3)))

(define cross-width                     ; cross-width is the distance of the perpendicular intersection
    (dist inner-b top-b))           ; between triangle sides and is used to "extend" lines

(define left-segment
    (let*
        ((a inner-b)
         (b (extend-point inner-a inner-b cross-width))
         (c (extend-point b left-c cross-width))
         (d (extend-point left-b left-a cross-width))
         (e top-a)
         (f top-c))
      (list a b c d e f)))

(define right-segment
    (let*
        ((a inner-c)
         (b right-a)
         (c (extend-point right-a right-b cross-width))
         (d (extend-point right-c right-b cross-width))
         (e (extend-point d (extend-point top-c top-a cross-width) (* 2 cross-width)))
         (f (extend-point c b (* 3 cross-width)))
         (g (extend-point c b cross-width))
         (h top-c))
      (list a b c d e f g h)))

(define bottom-segment
    (let*
        ((a inner-a)
         (b right-a)
         (c (extend-point right-a right-b cross-width))
         (d (extend-point left-a left-c cross-width))
         (e (extend-point left-b left-c cross-width))
         (f left-b)
         (g inner-b))
      (list a b c d e f g)))

(define top-left-segment
    (let*
        ((a (extend-point right-b right-a cross-width))
         (b (extend-point right-a a (* 2 cross-width)))
         (d (extend-point inner-a left-a cross-width))
         (c (extend-point left-a d (* 2 cross-width))))
      (list a b c d)))

(define top-segment
    (let*
        ((a (extend-point right-b right-a (* 3 cross-width)))
         (b (extend-point inner-a left-a (* 3 cross-width)))
         (c (extend-point right-a a cross-width))
         (d (find-point b c (rad 120) #t cross-width)))
      (list a b c d)))

(define red (make-color* 157 31 36))
(define blue (make-color* 63 93 167))
(define line-color (make-color* 255 255 255))

(define win-max 45)
(define win-min -28)
(set-curve-pict-size 600 600)
(with-window (window win-min win-max win-min win-max)
  (penwidth 10 (draw
               (filldraw (curve (loop-points right-segment)) red line-color)
               (filldraw (curve (loop-points left-segment)) "white" line-color)
               (filldraw (curve (loop-points top-segment)) "white" line-color)
               (filldraw (curve (loop-points bottom-segment)) blue line-color)
               (filldraw (curve (loop-points top-left-segment)) blue line-color))))
