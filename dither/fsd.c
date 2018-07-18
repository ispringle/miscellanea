/* My C implementation of Floyd-Steinberg Dithering. [Wikipedia's][1] psuedocode is shown below: 

for each y from top to bottom
   for each x from left to right
      oldpixel  := pixel[x][y]
      newpixel  := find_closest_palette_color(oldpixel)
      pixel[x][y]  := newpixel
      quant_error  := oldpixel - newpixel
      pixel[x + 1][y    ] := pixel[x + 1][y    ] + quant_error * 7 / 16
      pixel[x - 1][y + 1] := pixel[x - 1][y + 1] + quant_error * 3 / 16
      pixel[x    ][y + 1] := pixel[x    ][y + 1] + quant_error * 5 / 16
      pixel[x + 1][y + 1] := pixel[x + 1][y + 1] + quant_error * 1 / 16

[1]: https://en.wikipedia.org/wiki/Floyd%E2%80%93Steinberg_dithering "Floyd-Steinberg Dithering - Wikipedia"
*/

#include <gd.h>
#include <stdio.h>
#include <math.h>

gdImagePtr dither(gdImagePtr image);
gdImagePtr set_east(gdImagePtr image, int x, int y, int err_r, int err_g, int err_b);
gdImagePtr set_northwest(gdImagePtr image, int x, int y, int err_r, int err_g, int err_b);
gdImagePtr set_north(gdImagePtr image, int x, int y, int err_r, int err_g, int err_b);
gdImagePtr set_northeast(gdImagePtr image, int x, int y, int err_r, int err_g, int err_b);

int main (int argc, char* argv[]) {
	if (argc < 2) {
		printf("Please include a file to apply dithering to.\n");
		return 1;
	}
	if (gdSupportsFileType(argv[1], "true") == 0) {
		printf("Unsupported file type.\n");
		return 1;
	}
	gdImagePtr image = gdImageCreateFromFile(argv[1]);
	
	image = dither(image);
	gdImageGrayScale(image);

	gdImageFile(image, "out.jpg");

	return 0;
}

gdImagePtr dither(gdImagePtr image) {
	int max_X = gdImageSX(image), max_Y = gdImageSY(image), i = 3;
	for (int y = 0; y < max_Y; y++) {
		for (int x = 1; x < max_X; x++) {
			int tc = gdImageTrueColorPixel(image, x, y);
			int old_r = gdTrueColorGetRed(tc);
			int old_g = gdTrueColorGetGreen(tc);
			int old_b = gdTrueColorGetBlue(tc);
			int new_r = round(old_r / (255 / i)) * (255 / i);
			int new_g = round(old_g / (255 / i)) * (255 / i);
			int new_b = round(old_b / (255 / i)) * (255 / i);
			
			gdImageSetPixel(image, x, y, gdTrueColorAlpha(new_r, new_g, new_b, 0));
			
			int err_r = old_r - new_r;
			int err_g = old_g - new_g;
			int err_b = old_b - new_b;
			
			image = set_east(image, x, y, err_r, err_g, err_b);
			image = set_northwest(image, x, y, err_r, err_g, err_b);
			image = set_north(image, x, y, err_r, err_g, err_b);
			image = set_northeast(image, x, y, err_r, err_g, err_b);
		}
	}

	return image;
}

gdImagePtr set_east(gdImagePtr image, int x, int y, int err_r, int err_g, int err_b){
	x += 1;
	
	if (x >= gdImageSX(image)) {return image;}
	
	int tc = gdImageTrueColorPixel(image, x, y);
	int old_r = gdTrueColorGetRed(tc);
	int old_g = gdTrueColorGetGreen(tc);
	int old_b = gdTrueColorGetBlue(tc);
	
	int new_r = old_r + err_r * 7/16;
	int new_g = old_g + err_g * 7/16;
	int new_b = old_g + err_g * 7/16;
	
	gdImageSetPixel(image, x, y, gdTrueColorAlpha(new_r, new_g, new_b, 0));
	
	return image;
}

gdImagePtr set_northwest(gdImagePtr image, int x, int y, int err_r, int err_g, int err_b){
	x -= 1;
	y += 1;
	
	if (x < 0) {return image;}
	if (y >= gdImageSY(image)) {return image;}
	
	int tc = gdImageTrueColorPixel(image, x, y);
	int old_r = gdTrueColorGetRed(tc);
	int old_g = gdTrueColorGetGreen(tc);
	int old_b = gdTrueColorGetBlue(tc);
	
	int new_r = old_r + err_r * 3/16;
	int new_g = old_g + err_g * 3/16;
	int new_b = old_g + err_g * 3/16;
	
	gdImageSetPixel(image, x, y, gdTrueColorAlpha(new_r, new_g, new_b, 0));
	
	return image;
}

gdImagePtr set_north(gdImagePtr image, int x, int y, int err_r, int err_g, int err_b){
	y += 1;
	
	if (y >= gdImageSY(image)) {return image;}
	
	int tc = gdImageTrueColorPixel(image, x, y);
	int old_r = gdTrueColorGetRed(tc);
	int old_g = gdTrueColorGetGreen(tc);
	int old_b = gdTrueColorGetBlue(tc);
	
	int new_r = old_r + err_r * 5/16;
	int new_g = old_g + err_g * 5/16;
	int new_b = old_g + err_g * 5/16;
	
	gdImageSetPixel(image, x, y, gdTrueColorAlpha(new_r, new_g, new_b, 0));
	
	return image;
}

gdImagePtr set_northeast(gdImagePtr image, int x, int y, int err_r, int err_g, int err_b){
	x += 1;
	y += 1;
	
	if (x >= gdImageSX(image)) {return image;}
	if (y >= gdImageSY(image)) {return image;}
	
	int tc = gdImageTrueColorPixel(image, x, y);
	int old_r = gdTrueColorGetRed(tc);
	int old_g = gdTrueColorGetGreen(tc);
	int old_b = gdTrueColorGetBlue(tc);
	
	int new_r = old_r + err_r * 5/16;
	int new_g = old_g + err_g * 5/16;
	int new_b = old_g + err_g * 5/16;
	
	gdImageSetPixel(image, x, y, gdTrueColorAlpha(new_r, new_g, new_b, 0));
	
	return image;
}
