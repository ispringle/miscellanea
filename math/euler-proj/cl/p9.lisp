(defun find-triplet (sum &optional (a 1))
  "Find Pythagorean triplet that sums to sum.
   A is the smallest number, it cannot exceed some fraction of sum.
   There might be a way to better optimzie this, but since this starts
   from the bottom it will encounter A before it encounters the top of
   the range. With our presumed A, calculate B. If B is an integer, then
   deduce C and return the triplet as a list."
  (cond ((> a (floor sum 2)) nil)
        (t (let ((b (* sum (/ (- (/ sum 2) a) (- sum a)))))
             (cond ((integerp b) (list a b (- sum a b)))
                   (t (find-triplet sum (+ a 1))))))))

(apply '* (find-triplet 1000))
