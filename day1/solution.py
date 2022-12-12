with open("input.txt") as file:
	lines = file.read().splitlines()
	
max_elf = 0
current_elf = 0
for line in lines:
	if line == '':
		max_elf = max(current_elf, max_elf)
		current_elf = 0
	else:
		current_elf += int(line)

max_elf = max(current_elf, max_elf)

# solution 1
print(max_elf)

sums = list()
current_elf = 0
for line in lines:
	if line == '':
		sums.append(current_elf)
		current_elf = 0
	else:
		current_elf += int(line)

sums.append(current_elf)

sums.sort(reverse=True)
print(sums[0] + sums[1] + sums[2])