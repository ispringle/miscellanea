(require "prime" "prime.lisp")

(loop for i in (prime:sieve 2000000) sum i)
