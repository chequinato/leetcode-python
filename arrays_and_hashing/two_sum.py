﻿from typing import List, Optional, Tuple


def two_sum_brute_force(
    nums: List[int], target: int
) -> Optional[Tuple[int, int]]:
    """
    Brute force approach to find two indices whose values sum up to the target.

    Time Complexity:
    O(n²)

    Space Complexity:
    O(1)

    Args:
    nums (List[int]): List of integers.
    target (int): The target sum.

    Returns:
    Optional[Tuple[int, int]]: A tuple of indices if a solution is found,
    otherwise None.
    """
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return (i, j)

    return None


def two_sum_hash_map(
    nums: List[int], target: int
) -> Optional[Tuple[int, int]]:
    """
    HashMap approach to find two indices whose values sum up to the target.

    Time Complexity:
    O(n)

    Space Complexity:
    O(n)

    Args:
    nums (List[int]): List of integers.
    target (int): The target sum.

    Returns:
    Optional[Tuple[int, int]]: A tuple of indices if a solution is found,
    otherwise None.
    """
    numbers_seen: dict[int, int] = {}

    for i, number in enumerate(nums):
        complement = target - number

        if complement in numbers_seen:
            return (numbers_seen[complement], i)

        numbers_seen[number] = i

    return None


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9

    brute_force_result = two_sum_brute_force(nums, target)
    hash_map_result = two_sum_hash_map(nums, target)

    print(f"Brute Force result: {brute_force_result}")
    print(f"HashMap result: {hash_map_result}")