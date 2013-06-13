import random

def random_order(array):
	n = len(array)
	for i in xrange(n - 1):
		j = random.randint(i, n - 1)
		array[i], array[j] = array[j], array[i]


def main():
	def run(array):
		random_order(array)
		print(array)

	run(range(5))
	run(range(5))


if __name__ == '__main__':
	main()