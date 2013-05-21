def readWord():
	c = f.read(1)
	if c != '"':
		return None
	result = ""
	while True:
		c = f.read(1)
		if c == '"':
			break
		result += c
	f.read(1)
	return result
	
def triangleNumbers(max):
	x = 1
	i = 2
	while x < max:
		yield x
		x += i
		i += 1	

nums = set(triangleNumbers(15 * 26))

tcount = 0
with open('42.txt') as f:
	words = iter(readWord, None)
	for w in words:
		code = sum(ord(c) - ord('A') + 1 for c in w)
		if code in nums:
			tcount += 1
			print(w)
print(tcount)