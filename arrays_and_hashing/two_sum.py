﻿
from typing import List, Optional, Tuple

def two_sum(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
    """
    Brute force approach to find two indices such that their corresponding values sum up to the target.
    
    Args:
    nums (List[int]): List of integers.
    target (int): The target sum.
    
    Returns:
    Optional[Tuple[int, int]]: A tuple of indices if a solution is found, otherwise None.
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n): # arguments: start, end, finish
            if nums[i] + nums[j] == target: 
                return (i, j)
    return None


if __name__ == "__main__":
    # Example usage
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    if result:
        print(f"Indices found: {result}")
    else:
        print("No solution found.")