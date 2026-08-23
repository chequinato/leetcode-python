from typing import Tuple


def is_anagram(s: str, t: str) -> bool:
    """
    Checks whether two strings are valid anagrams.

    Uses hash maps to count the frequency of each character.

    Args:
    s (str): First string.
    t (str): Second string.

    Returns:
    bool: True if the strings are anagrams, otherwise False.
    """
    if len(s) != len(t):
        return False

    count_s: dict[str, int] = {}
    count_t: dict[str, int] = {}

    for char in s:
        if char in count_s:
            count_s[char] += 1
        else:
            count_s[char] = 1

    for char in t:
        if char in count_t:
            count_t[char] += 1
        else:
            count_t[char] = 1

    return count_s == count_t


if __name__ == "__main__":
    # Example usage
    s = "anagram"
    t = "nagaram"

    result = is_anagram(s, t)

    print(f"Is anagram: {result}")