/*
This program will write output to b-fern.data This file will contain 10,000 coordinates that can then be plotted
with another program, such as gnuplot. Note, if using gnuplot, remove one line from the data file or comment out
lines 16 of 17 of the source. 
*/

#include <stdio.h>
#include <time.h>
#include <stdlib.h>

#define iterations 1000000

int main () {
	double coord[2][2];
	coord[0][0] = 0;
	coord[0][0] = 0;

	srand(time(NULL));

	FILE * fp;
	fp = fopen("b-fern.data", "w");
	//fprintf(fp, "X, Y\n");
	//fclose(fp);
	fp = fopen("b-fern.data", "a");

	for (int i = 0; i < iterations; i++) {
		double x = coord[0][0];
		double y = coord[0][1];

		fprintf(fp, "%f, %f\n", x, y);

		double probability = (double)rand() / (double)RAND_MAX;

		if (probability < 0.01) {								//stem
			coord[1][0] =  0.00 * x +  0.00 * y +  0.00;
			coord[1][1] =  0.00 * x +  0.16 * y +  0.00;
		}
		else if (probability < 0.86) {							//successivley smaller leaflets
			coord[1][0] =  0.85 * x +  0.04 * y +  0.00;
			coord[1][1] = -0.04 * x +  0.85 * y +  1.60;
		}
		else if (probability < 0.93) {							//Largest left-handed leaflet
			coord[1][0] =  0.20 * x + -0.26 * y +  0.00;
			coord[1][1] =  0.23 * x +  0.22 * y +  1.60;
		}
		else {													//Largest right-handed leaflet
			coord[1][0] = -0.15 * x +  0.28 * y +  0.00;
			coord[1][1] =  0.26 * x +  0.24 * y +  0.44;
		}

		coord[0][0] = coord[1][0];
		coord[0][1] = coord[1][1];
	}
	return 0;
}

