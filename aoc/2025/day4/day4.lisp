(load "../utils.lisp")

(defun parse-grid (file)
  "Read file into a 2D character array."
  (with-open-file (in file)
    (let ((lines (loop for l = (read-line in nil)
                       while (and l (plusp (length l))) collect l)))
      (make-array (list (length lines) (length (first lines)))
                  :initial-contents lines))))

(defun count-neighbors (grid row col)
  "Count @ neighbors around (row, col)."
  (loop with rows = (array-dimension grid 0)
        with cols = (array-dimension grid 1)
        for dr from -1 to 1 sum
        (loop for dc from -1 to 1
              for nr = (+ row dr) for nc = (+ col dc)
              count (and (not (and (zerop dr) (zerop dc)))
                         (<= 0 nr (1- rows)) (<= 0 nc (1- cols))
                         (char= (aref grid nr nc) #\@)))))

(defun remove-accessible (grid)
  "Remove rolls with <4 neighbors, return count removed."
  (let ((removable nil))
    (dotimes (r (array-dimension grid 0))
      (dotimes (c (array-dimension grid 1))
        (when (and (char= (aref grid r c) #\@)
                   (< (count-neighbors grid r c) 4))
          (push (cons r c) removable))))
    (dolist (pos removable (length removable))
      (setf (aref grid (car pos) (cdr pos)) #\.))))

(defun solve (file &optional part2)
  "P1: accessible rolls. P2: total removable via iteration."
  (let ((grid (parse-grid file)))
    (if part2
        (loop for n = (remove-accessible grid) while (plusp n) sum n)
        (remove-accessible grid))))

(run-day solve "day4"
  ("P1" () 13)
  ("P2" (t) 43))
