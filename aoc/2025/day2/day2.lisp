;; https://en.wikipedia.org/wiki/Repdigit

(load "../utils.lisp")

;; d=digit-len, k=reps, m=multiplier, p=pattern
(defun solve (file kmax &aux (ht (make-hash-table)))
  (with-open-file (f file)
    (with-input-from-string (s (substitute #\Space #\, (substitute #\Space #\- (read-line f))))
      (loop for lo = (read s nil) while lo for hi = (read s) do
        (loop for d from 1 to 10 do (loop for k from 2 to kmax when (<= (* d k) 12) do
          (let ((m (/ (1- (expt 10 (* d k))) (1- (expt 10 d)))))
            (loop for p from (max (expt 10 (1- d)) (ceiling lo m)) to (min (1- (expt 10 d)) (floor hi m))
                  do (setf (gethash (* p m) ht) t))))))))
  (loop for id being the hash-keys of ht sum id))

(run-day solve "day2"
  ("P1" (2) 1227775554)
  ("P2" (15) 4174379265))
