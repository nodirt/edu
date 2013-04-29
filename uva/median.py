testCases = int(input())

for i in range(testCases):
	n, *s = [int(x) for x in input().split(' ')]
	s.sort()
	v = s[n//2]
	print(sum(abs(si - v) for si in s))

