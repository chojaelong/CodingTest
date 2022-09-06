def solution(pos):
	x = 65 - ord(pos[0]) + 1
	y = int(pos[1])
	positions = [[1, 2], [2, 1], [-1, 2], [1, -2], [-2, 1], [2, -1], [-2, -1], [-1, -2]]
	count = 0
	array = []
	
	for mx, my in positions:
		if x + mx > 8 or x + mx < 1:
			continue
		if y + my > 8 or y + my < 1:
			continue
		
		array.append((x + mx, y + my))
		count += 1
	
	return count