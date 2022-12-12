with open("input.txt") as file:
	lines = file.read().splitlines()

sum = 0
for line in lines:
	firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
	
	char = ''
	for chr in firstpart:
		if chr in secondpart:
			char = chr
			break
	
	if char.isupper():
		offset = ord('A') - 27
	else:
		offset = ord('a') - 1
		
	sum += ord(char) - offset

print(sum)

sum = 0
for i in range(0, len(lines), 3):
	
	char = ''
	for chr in lines[i]:
		if chr in lines[i+1] and chr in lines[i+2]:
			char = chr
			break
		
	if char.isupper():
		offset = ord('A') - 27
	else:
		offset = ord('a') - 1
		
	sum += ord(char) - offset
	
print(sum)