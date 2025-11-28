"""
17. Letter Combinations of a Phone Number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Given a string containing digits from 2-9 inclusive, return all possible 
letter combinations that the number could represent.

A mapping of digits to letters (just like on the telephone buttons) is given.
Note that 1 does not map to any letters.

Time Complexity: O(4^n) where n is the length of digits
Space Complexity: O(n) for recursion stack
"""

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone = {
            '2': 'abc', '3': 'def', '4': 'ghi',
            '5': 'jkl', '6': 'mno', '7': 'pqrs',
            '8': 'tuv', '9': 'wxyz'
        }
        
        result = []
        
        def backtrack(idx: int, path: str) -> None:
            if idx == len(digits):
                result.append(path)
                return
            
            for letter in phone[digits[idx]]:
                backtrack(idx + 1, path + letter)
        
        backtrack(0, "")
        return result


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    digits1 = "23"
    print(f"Input: digits='{digits1}'")
    print(f"Output: {solution.letterCombinations(digits1)}")
    # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    
    # Test case 2
    digits2 = ""
    print(f"Input: digits='{digits2}'")
    print(f"Output: {solution.letterCombinations(digits2)}")  # []
    
    # Test case 3
    digits3 = "2"
    print(f"Input: digits='{digits3}'")
    print(f"Output: {solution.letterCombinations(digits3)}")  # ["a","b","c"]
