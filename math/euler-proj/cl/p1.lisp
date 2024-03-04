;;; List all natural numbers below ~n~ that have a multiple of 3 or 5, then sum them.
(defun collect (n &optional (total 0))
  (let ((num (- n 1))
        (div-3-or-5-p (lambda (i) (or (zerop (mod i 3))
                                      (zerop (mod i 5))))))
    (cond
      ((= num 2) total)
      ((not (funcall div-3-or-5-p num)) (collect num total))
      ((funcall div-3-or-5-p num) (collect num (+ num total))))))
(collect 1000)
