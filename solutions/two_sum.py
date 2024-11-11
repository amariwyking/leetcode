# First intuition is to simply loop through the elements

def two_sum_naive(arr, target):
    left_ptr, right_ptr = 0, 1

    # check the rest of the array for an addend that will reach the sum
    # if nothing found move to the next index and check again

    for l_idx in range(len(arr)):
        for r_idx in range(len(arr)):
            if l_idx == r_idx:
                continue

            total = arr[l_idx] + arr[r_idx]

            print(total)

            if total == target:
                return [l_idx, r_idx]


# In order to optimize this algorithm, we would do best to minimize the number of comparisons
# By constructing a dictionary, we can keep track of all the numbers
# that we encountered on the first pass of the array
def two_sum(nums, target):
    addends = dict()

    for idx, num in enumerate(nums):
        if num in addends:
            if num + num == target:
                return [addends[num], idx]
        else:
            if target - num in addends:
                return [addends[target - num], idx]

            addends[num] = idx


print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))
