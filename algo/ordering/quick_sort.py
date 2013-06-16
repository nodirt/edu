import test

def quick_sort(array):
    def sort(low, high):
        if low >= high:
            return
        p = array[low + (high - low) // 2]
        i = low
        j = high

        while i <= j:
            while array[i] < p:
                i += 1
            while array[j] > p:
                j -= 1

            if i <= j:
                array[i], array[j] = array[j], array[i]
                i += 1
                j -=1

        sort(low, j)
        sort(i, high)

    sort(0, len(array) - 1)


def main():
    test.test_sort(quick_sort)
    print('All tests passed')


if __name__ == '__main__':
    main()