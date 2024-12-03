(ql:quickload 'str)

(defparameter test-input
  "7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9")

(defparameter input (uiop:read-file-string "input/two.txt"))

(defun list= (l1 l2 &optional (test #'equal))
  (loop for i in l1
        for j in l2
        always (funcall test i j)))

(defun within-range (l min max)
  (loop for i from 0 below (1- (length l))
        always (let* ((current (nth i l))
                      (next (nth (1+ i) l))
                      (diff (abs (- current next))))
                 (and (<= min diff) (>= max diff)))))

(defun is-safep (report)
  (when (and (or (list= report (sort (copy-seq report) #'<))
               (list= report (sort (copy-seq report) #'>)))
           (within-range report 1 3))
      t))

(defun solve (input)
  (let* ((reports (mapcar #'(lambda (line)
                              (mapcar #'parse-integer (str:words line)))
                          (str:lines input)))
         (safe-reports (loop for report in reports
                             count (is-safep report) into no-dampening
                             count (or (is-safep report)
                                       (loop for i from 0 below (length report)
                                             thereis (is-safep (concatenate 'list
                                                                        (subseq report 0 i)
                                                                        (subseq report (1+ i)))))) into with-dampening
                             finally (return (list no-dampening with-dampening)))))
    safe-reports))

(solve input)
