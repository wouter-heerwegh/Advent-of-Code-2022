with open("input.txt") as file:
	lines = file.read().splitlines()


moves = [(line[0],line[2]) for line in lines]

sum = 0
for move in moves:
	opponent_move = ord(move[0]) - ord('A')
	my_move = ord(move[1]) - ord('X')
	
	result = (my_move - opponent_move + 1) % 3 * 3
	
	sum += (my_move + 1) + result
	
print(sum)

sum = 0
for move in moves:
	opponent_move = ord(move[0]) - ord('A')
	my_move = (opponent_move + (ord(move[1]) - ord('X')) - 1) % 3
	
	result = (my_move - opponent_move + 1) % 3 * 3	
	sum += (my_move + 1) + result
	
print(sum)