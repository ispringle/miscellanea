(load "../utils.lisp")

(defun solve (file)
  (let ((pos 50) (cnt 0) (at0 0))
    (with-open-file (in file)
      (loop for ln = (read-line in nil) while ln
            for delta = (* (if (char= (char ln 0) #\L) -1 1)
                           (parse-integer (subseq ln 1)))
            for prev = pos
            do (incf pos delta)
               (incf cnt (+ (abs (- (floor prev 100) (floor pos 100)))
                            (abs (- (floor (1- prev) 100) (floor (1- pos) 100)))))
               (when (zerop (mod pos 100)) (incf at0))))
    (values at0 (/ cnt 2))))

(run-day solve "day1"
  ("P1 and P" () '(3 6)))
