from typing import Optional


def is_palindrome(looking_str: Optional[str]) -> bool:
    if len(looking_str) <= 1:
        return True
    if looking_str[0] != looking_str[-1]:
        return False
    return is_palindrome(looking_str[1:-1])
