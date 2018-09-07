# miscellanea (n)
 1. (countable) A miscellaneous collection of different things; a miscellany.<sup>[1][1]</sup>
 


## Directory of Files

### [dither][2]
An implementation of Floyd-Steinberg dithering. Outputs jpegs. Can be recompiled to change the number of colors, default is 8.

### [math][3]
Contains various math related programs and challengers.

#### [b-fern][4]
Contains a C and Python 3 implementation of the Barnsley Fern fractal. 

 - The C program will create a file "b-fern.data" which contains the data points opf the fern, which can be piped into GNU Plot or another plotting software
 - The Python program also exports to a file called "b-fern-py.data", however a line can be uncommented to plot the fern in Matplotlib. This is commented out as GNU Plot is significantly quicker (by multiple minutes at very large data sizes)

#### [Euler Projects][5]
Contains a directory for C and Python answers to various Euler Projects. The version is significantly lacking. The Python directory contains a subdirectory for Python2 and Python 3. Python 2 has more answers, but they are older code and poorly written. The Python 3 directory is somewhat of a refactoring of my Python 2 answers. A number of the answers depend on personal math libraries which are locted in a the /lib/ directory. As long as you include /lib/* all answers should work in Python 3.


 [1]: https://en.wiktionary.org/wiki/miscellanea#English "Wiktionary.com"
 [2]: https://github.com/pard68/miscellanea/tree/master/dither
 [3]: https://github.com/pard68/miscellanea/tree/master/math
 [4]: https://github.com/pard68/miscellanea/tree/master/math/b-fern
 [5]: https://github.com/pard68/miscellanea/tree/master/math/euler-proj
