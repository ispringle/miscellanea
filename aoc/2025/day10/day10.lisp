(load "../utils.lisp")

(defun split-str (s sep)
  "Split string by separator character."
  (loop with start = 0 for i from 0 below (length s)
        when (char= (char s i) sep)
          collect (subseq s start i) into parts and do (setf start (1+ i))
        finally (return (nconc parts (list (subseq s start))))))

(defun parse-target (s)
  "Parse [.##.] into list of 0s and 1s."
  (let ((a (position #\[ s)) (b (position #\] s)))
    (when (and a b)
      (map 'list (lambda (c) (if (eql c #\#) 1 0)) (subseq s (1+ a) b)))))

(defun parse-buttons (s)
  "Parse (x,y,z) groups before { into list of index lists."
  (let ((brace (position #\{ s)))
    (when brace (setf s (subseq s 0 brace))))
  (loop with pos = 0
        for start = (position #\( s :start pos) while start
        for end = (position #\) s :start start)
        collect (mapcar #'parse-integer
                        (remove "" (split-str (subseq s (1+ start) end) #\,)
                                :test #'string=))
        do (setf pos (1+ end))))

(defun parse-joltage (s)
  "Parse {3,5,4,7} into list of integers."
  (let ((a (position #\{ s)) (b (position #\} s)))
    (when (and a b)
      (mapcar #'parse-integer
              (remove "" (split-str (subseq s (1+ a) b) #\,)
                      :test #'string=)))))

(defun min-presses-p1 (target buttons)
  "Find min button presses for Part 1 (toggle lights)."
  (let ((nl (length target)) (nb (length buttons)) (best nil))
    (dotimes (mask (ash 1 nb) best)
      (let ((lights (make-array nl :initial-element 0)))
        (loop for btn in buttons for i from 0 when (logbitp i mask) do
          (dolist (j btn)
            (setf (aref lights j) (logxor (aref lights j) 1))))
        (when (equal (coerce lights 'list) target)
          (let ((cnt (logcount mask)))
            (setf best (if best (min best cnt) cnt))))))))

(defun min-presses-p2 (buttons targets)
  "Find min button presses for Part 2 using Gaussian elimination."
  (let* ((m (length targets)) (n (length buttons))
         (mat (make-array (list m (1+ n)) :initial-element 0))
         (tgt (coerce targets 'vector))
         (btns (coerce buttons 'vector)))
    (loop for j below n do
      (dolist (i (aref btns j)) (when (< i m) (setf (aref mat i j) 1))))
    (loop for i below m do (setf (aref mat i n) (aref tgt i)))
    (let ((pivots nil) (pr 0))
      (loop for c below n while (< pr m) do
        (let ((fr (loop for r from pr below m
                        when (/= (aref mat r c) 0) return r)))
          (when fr
            (when (/= fr pr)
              (loop for k to n do (rotatef (aref mat pr k) (aref mat fr k))))
            (let ((pv (aref mat pr c)))
              (loop for k to n do
                (setf (aref mat pr k) (/ (aref mat pr k) pv))))
            (loop for r below m when (/= r pr) do
              (let ((f (aref mat r c)))
                (when (/= f 0)
                  (loop for k to n do
                    (decf (aref mat r k) (* f (aref mat pr k)))))))
            (push c pivots)
            (incf pr))))
      (setf pivots (nreverse pivots))
      (when (loop for r from (length pivots) below m
                  thereis (/= (aref mat r n) 0))
        (return-from min-presses-p2 nil))
      (let ((free (loop for c below n unless (member c pivots) collect c)))
        (if (null free)
            (let ((sol (make-array n :initial-element 0)))
              (loop for r from 0 for c in pivots do
                (setf (aref sol c) (aref mat r n)))
              (when (every (lambda (x) (and (integerp x) (>= x 0))) sol)
                (reduce #'+ sol)))
            (let ((bounds (mapcar (lambda (fc)
                                    (loop for i in (aref btns fc)
                                          when (< i m) minimize (aref tgt i)))
                                  free))
                  (best nil))
              (labels
                  ((srch (idx fv)
                     (if (>= idx (length free))
                         (let ((sol (make-array n :initial-element 0))
                               (rfv (reverse fv)))
                           (loop for fc in free for v in rfv
                                 do (setf (aref sol fc) v))
                           (loop for r from 0 for pc in pivots do
                             (setf (aref sol pc)
                                   (- (aref mat r n)
                                      (loop for fc in free for v in rfv
                                            sum (* (aref mat r fc) v)))))
                           (when (every (lambda (x)
                                          (and (rationalp x) (= x (floor x))
                                               (>= x 0)))
                                        sol)
                             (let ((s (reduce #'+ sol :key #'floor)))
                               (setf best (if best (min best s) s)))))
                         (loop for v to (or (nth idx bounds) 0)
                               do (srch (1+ idx) (cons v fv))))))
                (srch 0 nil))
              best))))))

(defun solve (file &optional (part 1))
  "Solve Day 10 for given part."
  (with-open-file (in file)
    (loop for line = (read-line in nil) while line
          for btns = (parse-buttons line)
          when (plusp (length line))
            sum (or (if (= part 1)
                        (min-presses-p1 (parse-target line) btns)
                        (min-presses-p2 btns (parse-joltage line)))
                    0))))

(run-day solve "day10"
  ("Part 1" (1) 7)
  ("Part 2" (2) 33))
