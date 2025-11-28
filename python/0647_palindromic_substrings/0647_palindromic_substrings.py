"""
647. Palindromic Substrings
https://leetcode.com/problems/palindromic-substrings/

Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.

Time Complexity: O(n²)
Space Complexity: O(1)
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Expand around each center approach.
        For each position, expand outward checking for palindromes.
        Consider both odd and even length palindromes.
        """
        def countPalindromes(left: int, right: int) -> int:
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count
        
        total = 0
        for i in range(len(s)):
            # Odd length palindromes (single character center)
            total += countPalindromes(i, i)
            # Even length palindromes (between two characters)
            total += countPalindromes(i, i + 1)
        
        return total
    
    def countSubstringsDP(self, s: str) -> int:
        """Alternative DP solution."""
        n = len(s)
        count = 0
        
        # dp[i][j] = True if s[i:j+1] is palindrome
        dp = [[False] * n for _ in range(n)]
        
        # Single characters are palindromes
        for i in range(n):
            dp[i][i] = True
            count += 1
        
        # Check length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                count += 1
        
        # Check length 3 and above
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    count += 1
        
        return count


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    s1 = "abc"
    print(f"Input: s='{s1}'")
    print(f"Output: {solution.countSubstrings(s1)}")  # 3 (a, b, c)
    
    # Test case 2
    s2 = "aaa"
    print(f"Input: s='{s2}'")
    print(f"Output: {solution.countSubstrings(s2)}")  # 6 (a, a, a, aa, aa, aaa)
    
    # Test case 3
    s3 = "abba"
    print(f"Input: s='{s3}'")
    print(f"Output: {solution.countSubstrings(s3)}")  # 6 (a, b, b, a, bb, abba)
