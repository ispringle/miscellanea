# My Implementation of Floyd-Steinberg Dithering in C

This program uses libgd to manipulate the file. 

Output is a jpeg. 

In `dither()` there is a variable, `i`, which can be altered to adjust the number of colors. Currently this is 
set to 7, meaning it will output 8 colors (0-7). Additionally, the output image is set to grayscale, that can be
changed by commenting out the line in main calling `gdImageGrayScale(image)`. 

Compiles with `gcc -w -lgd -o fsd fsd.c`
