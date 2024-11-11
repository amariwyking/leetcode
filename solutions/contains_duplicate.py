from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    # The identity of every element in the list must be checked, therefore the minimum time complexity is O(n)
    nums_seen = set()

    for num in nums:
        if num in nums_seen:
            return True

        nums_seen.add(num)

    return False


print(contains_duplicate([1, 2, 3, 1]))
print(contains_duplicate([1, 2, 3, 4]))
print(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
