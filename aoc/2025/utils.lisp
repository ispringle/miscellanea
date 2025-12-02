;; Shared AOC utilities

(defmacro run-day (solve-fn day &rest parts)
  "Run tests and solutions for a day. Each part is (name args expected).
   Files are inferred as {day}-test.txt and {day}.txt.
   Args are additional arguments to solve-fn beyond the file."
  `(let ((test-file (concatenate 'string ,day "-test.txt"))
         (real-file (concatenate 'string ,day ".txt")))
     ,@(loop for (name args expected) in parts
             collect `(let ((test-result (multiple-value-list (,solve-fn test-file ,@args))))
                        (when (= (length test-result) 1)
                          (setf test-result (first test-result)))
                        (format t "Test ~a: ~a~%" ,name test-result)
                        (if (equal test-result ,expected)
                            (let ((result (multiple-value-list (,solve-fn real-file ,@args))))
                              (when (= (length result) 1)
                                (setf result (first result)))
                              (format t "~a: ~a~%" ,name result))
                            (format t "~a: SKIPPED - test failed (expected ~a)~%" ,name ,expected))))))
