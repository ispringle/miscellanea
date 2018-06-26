#include <stdio.h>

#define limit 4000000

int main (void) {
	long prev_fib = 1, cur_fib = 1, fib, sum = 0;

	for (fib = 0; fib < limit; fib = prev_fib + cur_fib) {
		prev_fib = cur_fib;
		cur_fib = fib;
		if (fib % 2 == 0) {
			sum += fib;
		}
	}
	printf("%ld\n", sum);
	return 0;
}

