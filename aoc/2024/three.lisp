(ql:quickload 'cl-ppcre)

(defparameter *test-input*
  "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))")

(defparameter input (uiop:read-file-string "input/three.txt"))

(defun solve (input)
  (let* ((re-ops (ppcre:create-scanner "(mul\\((\\d{1,3}),(\\d{1,3})\\)|do\\(\\))|don't\\(\\)"))
         (re-num (ppcre:create-scanner "\\d{1,3}"))
         (valid-ops (ppcre:all-matches-as-strings re-ops input))
         (include t)
         (parsed (mapcar #'(lambda (m)
                             (cond ((equal m "do()") (progn (setf include t) (list 0 include)))
                                   ((equal m "don't()") (progn (setf include nil) (list 0 include)))
                                   (t
                                    (list 
                                     (apply #'* (mapcar #'parse-integer (ppcre:all-matches-as-strings re-num m)))
                                     include))))
                         valid-ops))
         (one (reduce #'(lambda (sum pair)
                          (+ sum (car pair)))
                      parsed :initial-value 0))
         (two (reduce #'(lambda (sum pair)
                          (+ sum (if (cadr pair) (car pair) 0)))
                      parsed :initial-value 0)))
    (list one two)))

(solve *test-input*)                    ; => (161 48)
(solve input)
