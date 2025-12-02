#!/usr/bin/env -S sbcl --script
;; AOC 2025 runner - run any day's solution from root directory
;; Usage: sbcl --script run.lisp <day>
;;    or: ./run.lisp <day>

(defun usage ()
  (format t "Usage: sbcl --script run.lisp <day>~%")
  (format t "       ./run.lisp <day>~%~%")
  (format t "Examples:~%")
  (format t "  sbcl --script run.lisp 1~%")
  (format t "  ./run.lisp 2~%")
  (sb-ext:exit :code 1))

(defun run-day (day)
  (let* ((day-dir (format nil "day~a" day))
         (lisp-file (format nil "day~a.lisp" day))
         (full-path (merge-pathnames lisp-file (make-pathname :directory `(:relative ,day-dir)))))
    (unless (probe-file day-dir)
      (format t "Error: Directory '~a' not found~%" day-dir)
      (sb-ext:exit :code 1))
    (unless (probe-file full-path)
      (format t "Error: Solution file '~a' not found~%" full-path)
      (sb-ext:exit :code 1))
    (format t "=== Running Day ~a ===~%" day)
    ;; Change to day directory so relative paths work
    (let ((*default-pathname-defaults* (truename (make-pathname :directory `(:relative ,day-dir)))))
      (load lisp-file))))

(let ((args (rest sb-ext:*posix-argv*)))
  (if (null args)
      (usage)
      (run-day (first args))))

