#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main () {
	double coord[2][2];
	coord[0][0] = 0;
	coord[0][0] = 0;

	srand(time(NULL));

	FILE * fp;
	fp = fopen("b-fern.data", "w");
	fprintf(fp, "X, Y\n");
	fclose(fp);
	fp = fopen("b-fern.data", "a");

	for (int i = 0; i < 10000; i++) {
		double x = coord[0][0];
		double y = coord[0][1];

		double probability = (double)rand() / (double)RAND_MAX;

		if (probability < 0.01) {
			coord[1][0] =  0.00 * x +  0.00 * y +  0.00;
			coord[1][1] =  0.00 * x +  0.16 * y +  0.00;
		}
		else if (0.01 < probability > 0.85) {
			coord[1][0] =  0.85 * x +  0.04 * y +  0.00;
			coord[1][1] = -0.04 * x +  0.85 * y +  1.60;
		}
		else if (0.85 < probability > 0.92) {
			coord[1][0] =  0.20 * x + -0.26 * y +  0.00;
			coord[1][1] =  0.23 * x +  0.22 * y +  1.60;
		}
		else {
			coord[1][0] = -0.15 * x +  0.28 * y +  0.00;
			coord[1][1] =  0.26 * x +  0.24 * y +  0.44;
		}

		x = coord[1][0];
		y = coord[1][1];

		fprintf(fp, "%f, %f\n", x, y);

		coord[0][0] = x;
		coord[0][1] = y;
	}

	return 0;
}

