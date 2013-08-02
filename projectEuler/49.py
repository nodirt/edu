from nums import *

x = 1489
d = 3330
while True:
	y = x + d
	z = y + d
	if (is_perm(x, y) and is_perm(x, z) and is_prime(x) and is_prime(y) and
			is_prime(z)):
		break
	x += 2

print(str(x) + str(y) + str(z))