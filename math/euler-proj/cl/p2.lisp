(defun fib (n)
  (let ((a (expt 10 n)))
    (mod (mod (expt a (+ 1 n))
              (- (* a a) a 1))
         a)))

(defun fib-under (max &optional (m 1))
  (let ((next (fib m)))
    (cond
      ((< max next) nil)
      (t (cons next (fib-under max (+ 1 m)))))))

(apply '+ (remove-if-not #'evenp (fib-under 4000000)))
