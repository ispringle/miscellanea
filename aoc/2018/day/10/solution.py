from input import stars

def plotStars(stars, align):
	#star_map = [[' '] * (align[2] + 1) for i in range(align[3] + 1)]
	star_map = [[' '] * 200 for i in range(400)]
	for x, y, vx, vy in stars:
		star_map[y + align[0] * vy - align[3]][x + align[0] * vx - 250 - align[2]] = '█'
	for star in star_map:
		if '█' in star:
			print(''.join(star))

def partOne(stars):
	lowest = [0, 1000000000, 0, 0]
	for i in range(max(x for x, _, _, _ in stars) - min(x for x, _, _, _ in stars)):
		min_x = min([x + i * vx for x, y, vx, vy in stars])
		min_y = min([y + i * vy for x, y, vx, vy in stars])
		max_x = max([x + i * vx for x, y, vx, vy in stars])
		max_y = max([y + i * vy for x, y, vx, vy in stars])
		bounding_x = max_x - min_x 
		bounding_y = max_y - min_y
		bounding_avg = bounding_x + bounding_y
		if bounding_avg < lowest[1]:
			lowest[0] = i
			lowest[1] = bounding_avg
			lowest[2] = bounding_x
			lowest[3] = bounding_y
	return lowest

alignment = partOne(stars)
plotStars(stars, alignment)
print(alignment)

