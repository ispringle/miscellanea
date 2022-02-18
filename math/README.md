# math

This is a collection of various _things_ that are in some shape or fashion
mathematical in nature... it's a loose term.

## Directory of Files

### [b-fern][0] Contains a C and Python 3 implementation of the Barnsley Fern
fractal. 

 - The C program will create a file "b-fern.data" which contains the data
   points opf the fern, which can be piped into GNU Plot or another plotting
   software
 - The Python program also exports to a file called "b-fern-py.data", however a
   line can be uncommented to plot the fern in Matplotlib. This is commented
   out as GNU Plot is significantly quicker (by multiple minutes at very large
   data sizes)

### [Euler Projects][1] Contains a directory for C and Python answers to
various Euler Projects. The version is significantly lacking. The Python
directory contains a subdirectory for Python2 and Python 3. Python 2 has more
answers, but they are older code and poorly written. The Python 3 directory is
somewhat of a refactoring of my Python 2 answers. A number of the answers
depend on personal math libraries which are locted in a the /lib/ directory. As
long as you include /lib/* all answers should work in Python 3.

![Muh 1337 rank](https://projecteuler.net/profile/pard68.png)

 [0]: https://github.com/pard68/miscellanea/tree/master/math/b-fern
 [1]: https://github.com/pard68/miscellanea/tree/master/math/euler-proj
