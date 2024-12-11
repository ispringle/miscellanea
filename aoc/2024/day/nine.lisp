(uiop:define-package aoc24.day.nine
  (:use #:cl #:iterate)
  (:import-from #:aoc24
   :get-input))
(in-package #:aoc24.day.nine)

(defparameter *test-input* "2333133121414131402")

(defparameter *input* (get-input 9))

(defun split-chars-to-int (s)
  (map 'list #'digit-char-p s))

(defun parse (input)
  (coerce  (let ((block-id 0))
             (iter (for (file space) on (split-chars-to-int input) by #'cddr)
               (nconcing (nconc  (make-list file :initial-element block-id)
                                 (when space (make-list space :initial-element #\.))))
               (incf block-id)))
           'vector ))

(defun frag (disk)
  (iter
    (for blk index-of-vector disk downto 0)
    (for val = (aref disk blk))
    (for nxt = (position #\. disk))
    (when (and  (numberp val) (> blk nxt))
      (rotatef (aref disk blk) (aref disk nxt))))
  disk)

(defun gen-checksum (disk)
  (iter
    (for val in-vector disk)
    (for pos from 0)
    (when (numberp val)
      (sum (* pos val)))))

(defun file-size (disk file-id)
  "Calculate the size of a file with given ID"
  (count file-id disk))

(defun find-free-space (disk start-pos needed-size)
  "Find leftmost contiguous free space of needed-size starting from start-pos"
  (iter outer
    (for pos from 0 below start-pos)
    (when (eql (aref disk pos) #\.)   ; Changed to eql for character comparison
      (let ((space-size 0))
        (iter 
          (for i from pos below (length disk))
          (while (and (< space-size needed-size)
                     (eql (aref disk i) #\.)))  ; Changed to eql here too
          (incf space-size)
          (finally 
            (when (>= space-size needed-size)
              (return-from outer pos))))))))

(defun move-file (disk file-id target-pos)
  "Move an entire file to target position"
  (let* ((size (file-size disk file-id))
         (old-positions (iter (for i from 0 below (length disk))
                            (when (eql (aref disk i) file-id)
                              (collect i)))))
    (iter (for pos in old-positions)
          (setf (aref disk pos) #\.))
    (iter (for i from target-pos below (+ target-pos size))
          (setf (aref disk i) file-id)))
  disk)

(defun defrag (disk)
  "New fragmentation approach moving whole files"
  (let ((max-id (reduce #'max (remove-if-not #'numberp disk))))  ; Changed to handle characters
    (iter (for file-id from max-id downto 0)
          (let* ((file-pos (position file-id disk))
                 (size (file-size disk file-id))
                 (target-pos (find-free-space disk file-pos size)))
          (when (and file-pos target-pos)
            (move-file disk file-id target-pos))))
    disk))

(defun solve (input)
  (list
   (gen-checksum (frag (parse input)))
   (gen-checksum (defrag (parse input)))))

(solve *input*)
(print (solve *input*))
