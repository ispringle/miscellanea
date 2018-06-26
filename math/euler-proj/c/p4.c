#include <stdio.h>
#include <string.h>

#define TRUE 1
#define FALSE 0
int palindrome(int number) {
	int original, remainder, reverse = 0;
	original = number;
	while (number > 0) {
		remainder = number % 10;				//get digit from ones column
		reverse = reverse * 10 + remainder;		//move digits in reverse left one and add remainder
		number /= 10;							//move digits in number right one
	}
	if (original == reverse) {
		return TRUE;
	}
	else {
		return FALSE;
	}
}

int main () {
	int one = 999, two = 999, largest = 0, prod;
	for (one; one > 100; one--) {
		two = 999;
		for (two; two > 100; two--) {
			prod = one * two;
			if (palindrome(prod) == TRUE) {
				if (prod > largest) {
					largest = prod;
				}
			}
		}
	}
	printf("%d\n", largest);
	return 0;
}
