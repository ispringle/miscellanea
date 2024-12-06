(uiop:define-package aoc24.day.six
  (:use #:cl #:iter)
  (:import-from #:aoc24
   :get-input)
  (:import-from #:aoc24.utils
   :list=))
(in-package #:aoc24.day.six)

(defparameter *test-input* "....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...")

(defparameter *input* (get-input 6))

(defun char-coords (l c)
  (iter outer
    (for y below (length l))
    (iter
      (for x below (length (nth y l)))
      (if (char= c (nth x (nth y l)))
          (in outer (collect (list x y)))))))

(defun add-coors (a b)
  (list
   (+ (car a) (car b))
   (+ (cadr a) (cadr b))))

(defun nearest (loc coors direction)
  (let ((order-by (case direction
                    ((:north :east) #'>)
                    (t #'<)))
        (point-lookup (case direction
                        ((:north :south) #'car)
                        (t #'cadr)))
        (compare (case direction
                   ((:north :south) #'cadr)
                   (t #'car))))
    (car (sort
          (remove-if-not
           #'(lambda (coor)
               (and (equal (funcall point-lookup loc)
                           (funcall point-lookup coor)) 
                    (funcall order-by (funcall compare loc)
                             (funcall compare coor))))
           coors)
          (lambda (a b)
            (funcall order-by (funcall compare a)
                     (funcall compare b)))))))

(defun next-coor (loc coors direction)
  (let ((offset (case direction
                  (:north '(0 1))
                  (:south '(0 -1))
                  (:east '(1 0))
                  (:west '(-1 0))))
        (next (nearest loc coors direction)))
    (and next
         (add-coors offset next))))

(defun diff-coords (a b)
  (+ (abs (- (car a) (car b)))
     (abs (- (cadr a) (cadr b)))))

(defun coors-between (a b)
  (let* ((fst (car (sort (list a b) (lambda (i j)
                                      (if (equal (car i) (car j))
                                          (< (cadr i) (cadr j))
                                          (< (car i) (car j)))))))
         (lst (if (list= fst a) b a)))
    (iter outer (for x from (car fst) to (car lst))
      (iter (for y from (cadr fst) to (cadr lst))
        (in outer (collect (list x y)))))))
(coors-between '(4 6) '(4 1))

(defun make-bounding-box (coors)
  (list 0 (1- (length (car coors))) (1- (length coors)) 0))

(defun nearest-edge (loc bounding direction)
  (case direction
    (:north (list (car loc) (car bounding)))
    (:south (list (car loc) (nth 2 bounding)))
    (:east (list (nth 3 bounding) (cadr loc)))
    (:west (list (nth 1 bounding) (cadr loc)))))

(defun solve (input)
  (let* ((grid 
           (mapcar #'(lambda (s) (coerce s 'list)) (str:lines input)))
         (objects (char-coords grid #\#))
         (guard (car (char-coords grid #\^)))
         (dir :north)
         (next (next-coor guard objects dir))
         (bounding (make-bounding-box grid)))
    (iter
      (while next)
      (nconcing (coors-between guard next) into steps)
      (after-each (setf guard next
                        dir (case dir
                              (:north :west)
                              (:west :south)
                              (:south :east)
                              (:east :north))
                        next (next-coor guard objects dir)))
      (finally (return (length (remove-duplicates (nconc
                                                   steps
                                                   (coors-between guard
                                                                  (nearest-edge guard bounding
                                                                                dir)))
                                                  :test #'aoc24.utils:list=)))))))

(solve *test-input*)
(solve *input*)

