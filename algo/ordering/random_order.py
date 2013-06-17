import random

def random_order(array):
    """Fisher–Yates shuffle changes array element order randomly

    Complexity:
        Time: O(n)
        Space: O(1)

    Description:
        Wikipedia: http://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle
        Cormen [1]: section 5.3, page 126

    History:
        Authors: Fisher, R.A.; Yates, F. (1948)
        Improved by Richard Durstenfeld in 1964, popularized by Donald E. Knuth 
        in volume 2 of his book The Art of Computer Programming.
    """

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