import parse

with open("input.txt") as file:
	lines = file.read().splitlines()

pairs = list()
for line in lines:
	result = parse.parse("{}-{},{}-{}", line)
	pairs.append(((int(result[0]), int(result[1])), (int(result[2]), int(result[3]))))

special_pairs = 0
for pair in pairs:
	if pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]:
		special_pairs += 1
	elif pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]:
		special_pairs += 1
		
print(special_pairs)

special_pairs = 0
for pair in pairs:
	if pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][0]:
		special_pairs += 1
	elif pair[0][0] <= pair[1][1] and pair[0][1] >= pair[1][1]:
		special_pairs += 1
	elif pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]:
		special_pairs += 1
	elif pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]:
		special_pairs += 1
		
print(special_pairs)