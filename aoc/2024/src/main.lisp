(uiop:define-package aoc24
  (:use #:cl)
  (:import-from #:drakma
   :http-request :cookie-jar
   :cookie)
  (:export #:get-input))
(in-package #:aoc24)

;; (named-readtables:defreadtable
;;     :sugar
;;   (:merge :fn.reader))


(defun fetch-input (day)
  (let* ((uri (format nil "https://adventofcode.com/2024/day/~a/input" day))
         (cookie (make-instance 'cookie
			        :name "session"
			        :value (uiop:read-file-string "aoc-cookie")
                                :domain ".adventofcode.com"))
         (jar (make-instance 'cookie-jar
                             :cookies (list cookie)))
	 (response (multiple-value-list
		    (http-request
                     uri
                     :cookie-jar jar))))
    (if (= (second response) 200)
	(first response)
	nil)))

(defun save-and-return-file (contents filename)
  (with-open-file (buffer filename
                          :direction :output
                          :if-exists :supersede
                          :if-does-not-exist :create)
    (format buffer "~a" contents))
  contents)

(defun get-input (day)
  (let ((file (format nil "input/~a.txt" day)))
    (if (probe-file file)
        (uiop:read-file-string file)
        (save-and-return-file (fetch-input day) file))))

(get-input 3)
