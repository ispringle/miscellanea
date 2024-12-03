(uiop:define-package aoc-system
  (:use #:cl #:uiop #:asdf))
(in-package #:aoc-system)

(defsystem "advent-of-code-2024"
  :version "0.0.1"
  :author "Ian S. Pringle"
  :mailto "ian@dapringles.com"
  :license "Unlicense"
  :depends-on ("str"
               "iterate"
               "fset"
               "cl-ppcre"
               "fn")
  :components ((:module "src"
                :components
                ((:file "main")
                 (:file "utils")))
               (:module "day"
                :depends-on ("src")
                :components #.(mapcar #'(lambda (p) (list :file (pathname-name p)))
                                      (directory-files (pathname-directory-pathname
                                                        (uiop/lisp-build:current-lisp-file-pathname))
                                                       "*.lisp"))))
  :description ""
  :in-order-to ((test-op (test-op "advent-of-code-2024/tests"))))

(defsystem "advent-of-code-2024/tests"
  :author "Ian S. Pringle"
  :license "Unlicense"
  :depends-on ("advent-of-code-2024"
               "rove")
  :components ((:module "tests"
                :components
                ((:file "main"))))
  :description "Test system for advent-of-code-2024"
  :perform (test-op (op c) (symbol-call :rove :run c)))
