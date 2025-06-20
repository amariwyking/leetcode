from typing import List


def twoSum(self, numbers: List[int], target: int) -> List[int]:
    idx_left, idx_right  = 0, len(numbers) - 1

    # The naive solution is to use the same method as the basic Two Sum problem,
    # creating a dictionary of addends, and then searching the dictionary for a solution
    # That solution is 2*O(N) which simplifies to O(N)

    # The question now is how to exploit the fact that the list of integers is sorted

    # Let's say we have a target number 9 and a list [2, 7, 11, 15]
    # How does a sorted array help us cut down on time?
    # Well, during our initial



    # return each index (+1) as an integer list such as [ind_a, ind_b]
    return [idx_left, idx_right]

print(twoSum([2, 7, 11, 15], 9))
