(ql:quickload 'cl-ppcre)

(defparameter *test-input*
  "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))")

(defparameter input (uiop:read-file-string "input/three.txt"))

(defun solve (input)
  (let* ((re (ppcre:create-scanner "mul\\((\\d{1,3}),(\\d{1,3})\\)"))
         (do-mul (lambda (ops &aux (sum 0))
                   (ppcre:do-register-groups ((#'parse-integer x y)) (re ops sum)
                     (incf sum (* x y))))))
    (list
     (funcall do-mul input)
     (funcall do-mul (ppcre:regex-replace-all
                      "(?s)don't\\(\\).*?(?:do\\(\\)|//Z)"
                      input "")))))

(solve *test-input*)                    ; => (161 48)
(solve input)
