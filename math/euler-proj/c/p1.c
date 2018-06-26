#include <stdio.h>

#define limit 1000

int main () {
	int sum = 0;
	for (int i = 3; i < limit; i++) {
		if (i % 3 == 0) {
		sum += i;
		}
		else if (i % 5 == 0) {
			sum += i;
		}
		else {
		}
	}
	printf("%d\n", sum);
	return 0;
}
