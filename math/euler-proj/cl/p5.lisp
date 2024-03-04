(require "utils" "./utils.lisp")

(defun lcm-of (l &optional (res 1))
  "Returns smallest int that is lcm of all ints in l"
  (cond ((not l) res)
        (t (lcm-of (cdr l) (lcm res (car l))))))

(lcm-of (utils:1-to 20))