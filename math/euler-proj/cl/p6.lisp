(require "utils" "./utils.lisp")

(defun sum-square-difference (n)
  (- (** (utils:? n))
     (utils:sum (mapcar #'utils:** (utils:1-to n)))))

(sum-square-difference 100)
