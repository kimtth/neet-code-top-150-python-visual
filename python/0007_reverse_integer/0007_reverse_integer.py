from typing import List, Optional

"""
LeetCode Reverse Integer

Problem from LeetCode: https://leetcode.com/problems/reverse-integer/

Description:
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21
"""

class Solution:

    def reverse(self, x: int) ->int:
        """
        Reverse the digits of a 32-bit signed integer.
        
        Args:
            x: The integer to reverse
            
        Returns:
            int: The reversed integer, or 0 if the result would overflow
        """
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0
        while x != 0:
            pop = x % 10
            x //= 10
            if rev > INT_MAX // 10 or rev == INT_MAX // 10 and pop > 7:
                return 0
            rev = rev * 10 + pop
        return sign * rev

    def reverse_pythonic(self, x: int) ->int:
        """
        Alternative implementation using Python's string conversion and slicing.
        
        Args:
            x: The integer to reverse
            
        Returns:
            int: The reversed integer, or 0 if the result would overflow
        """
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1
        sign = -1 if x < 0 else 1
        rev = sign * int(str(abs(x))[::-1])
        if rev < INT_MIN or rev > INT_MAX:
            return 0
        return rev

    def reverse_clean(self, x: int) ->int:
        """
        A cleaner approach without separating sign handling.
        Note: This method handles Python's floor division semantics correctly.
        
        Args:
            x: The integer to reverse
            
        Returns:
            int: The reversed integer, or 0 if the result would overflow
        """
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1
        
        # Handle negative numbers by working with absolute value
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0
        
        while x != 0:
            digit = x % 10
            x //= 10
            
            # Check for overflow before multiplying
            if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and digit > 7):
                return 0
            
            rev = rev * 10 + digit
        
        result = sign * rev
        
        # Final overflow check for negative result
        if result < INT_MIN or result > INT_MAX:
            return 0
            
        return result


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    x1 = 123
    result1 = solution.reverse(x1)
    print(f"Example 1: {x1} -> {result1}")  # Expected output: 321
    
    # Example 2
    x2 = -123
    result2 = solution.reverse(x2)
    print(f"Example 2: {x2} -> {result2}")  # Expected output: -321
    
    # Example 3
    x3 = 120
    result3 = solution.reverse(x3)
    print(f"Example 3: {x3} -> {result3}")  # Expected output: 21
    
    # Test overflow case
    x4 = 1534236469
    result4 = solution.reverse(x4)
    print(f"Overflow test: {x4} -> {result4}")  # Expected output: 0 (would overflow)
    
    # Compare implementations
    print("\nUsing alternative implementations:")
    print(f"Pythonic method for {x1}: {solution.reverse_pythonic(x1)}")
    print(f"Clean method for {x2}: {solution.reverse_clean(x2)}")
