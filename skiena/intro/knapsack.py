
def knapsack(nums, target):
    nums.sort(reverse=True)

    def find(start, target):
        for i in range(start, len(nums)):
            x = nums[i]
            if x > target:
                continue
            elif x == target:
                return [x]
            else:
                child = find(i + 1, target - x)
                if child:
                    return [x] + child

        return None

    return find(0, target)



for target in range(0, 50):
    subset = knapsack([1, 2, 4, 5, 9, 10], target)
    if subset:
        print('%s: %s' % (target, subset))