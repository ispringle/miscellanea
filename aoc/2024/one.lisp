(ql:quickload 'str)

(defvar test-input
  "3   4
4   3
2   5
1   3
3   9
3   3")

(defun solve (input)
  (let* ((lists (apply #'mapcar #'(lambda (&rest ns)
                                    (mapcar #'parse-integer ns))
                       (loop for line in (str:lines input)
                             collect (str:words line))))
         ;; Solves for part two first because `sort' is destructive
         (s2 (reduce #'+ (mapcar #'(lambda (n) (* n (count n (cadr lists)))) (car lists))))
         (s1 (reduce #'+ (mapcar #'(lambda (left right) (abs (- left right)))
                                 (sort (car lists) #'<)
                                 (sort (cadr lists) #'<)))))
    (list s1 s2)))

(solve (uiop:read-file-string "input/one.txt"))
(solve test-input)                      ; => (11 31)
