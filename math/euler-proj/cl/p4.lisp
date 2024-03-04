(defun palindrome-p (a b)
  (equalp a (reverse b)))

(defun palindrome-int-p (a b)
  (labels ((to-list (n) (coerce (write-to-string n) 'list)))
    (palindrome-p (to-list a) (to-list b))))

(defun palindrome-multiples-below (n)
  (loop for i from n downto 0
        do (return  (loop for j from n downto 0
                          when (palindrome-int-p (* i j) (* i j))
                          collect (* i j)))))
(car (palindrome-multiples-below 999))
