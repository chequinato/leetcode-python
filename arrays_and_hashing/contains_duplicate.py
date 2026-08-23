from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    """
    Checks whether a list contains any duplicate values.

    Uses a set to keep track of numbers already seen.

    Args:
    nums (List[int]): List of integers.

    Returns:
    bool: True if a duplicate is found, otherwise False.
    """
    numbers_seen = set()

    for number in nums:
        if number in numbers_seen:
            return True

        numbers_seen.add(number)

    return False


if __name__ == "__main__":
    # Example usage
    nums = [1, 2, 3, 1]
    result = contains_duplicate(nums)

    print(f"Contains duplicate: {result}")