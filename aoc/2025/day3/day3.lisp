(load "../utils.lisp")

(defun largest-n-digit (line n)
  "Find largest n-digit number by greedy digit selection."
  (let ((len (length line)) (result 0) (pos 0))
    (dotimes (i n result)
      (let ((best-digit 0) (best-pos pos))
        (loop for j from pos to (- len (- n i))
              for d = (digit-char-p (char line j))
              when (> d best-digit) do (setf best-digit d best-pos j))
        (setf result (+ (* result 10) best-digit) pos (1+ best-pos))))))

(defun solve (file n)
  (with-open-file (in file)
    (loop for line = (read-line in nil) while line
        sum (largest-n-digit line n))))

(run-day solve "day3"
  ("P1" (2) 357)
  ("P2" (12) 3121910778619))
