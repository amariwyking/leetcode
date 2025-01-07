from typing import List


# Naive O(n^2) solution
def product_of_array_except_self_naive(nums: List[int]) -> List[int]:
    products = []

    for i, num_i in enumerate(nums):
        product = 1

        for j, num_j in enumerate(nums):
            if j != i:
                product *= num_j

        products.append(product)

    return products


def product_except_self(nums: List[int]) -> List[int]:
    product = None

    left_products = []

    for idx in range(len(nums)):
        if idx == 0:
            product = 0
        elif idx == 1:
            product = nums[idx - 1]
        else:
            product *= nums[idx - 1]

        left_products.append(product)

    right_products = []

    for idx in reversed(range(len(nums))):
        if idx == len(nums) - 1:
            product = 0
        elif idx == len(nums) - 2:
            product = nums[len(nums) - 1]
        else:
            product *= nums[idx + 1]

        right_products.append(product)

    right_products.reverse()

    answers = []

    for idx in range(0, len(nums)):
        if idx == 0:
            answers.append(right_products[idx])
        elif idx == len(nums) - 1:
            answers.append(left_products[idx])
        else:
            answers.append(
                left_products[idx] * right_products[idx]
            )

    return answers


def product_except_delf_optimized(nums: List[int]) -> List[int]:
    # TODO: Reduce runtime by:
    #   (1) merging the loops for left and right products
    #   (2) simplifying logic by replacing the if-else tree
    pass


print(product_of_array_except_self_naive([1, 2, 3, 4]))
print(product_of_array_except_self_naive([-1, 1, 0, -3, 3]))
print(product_of_array_except_self_naive([-29, 1, 400, -3942, 62]))

print()

print(product_except_self([1, 2, 3, 4]))
print(product_except_self([-1, 1, 0, -3, 3]))
print(product_except_self([-29, 1, 400, -3942, 62]))

# print(product_of_array_except_self_naive([8, 2, 3, 4]))
# print(product_of_array_except_self([8, 2, 3, 4]))
