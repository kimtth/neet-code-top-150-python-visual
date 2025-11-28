"""
1. Two Sum
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the 
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may 
not use the same element twice.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}  # value -> index
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in hashmap:
                return [hashmap[complement], i]
            
            hashmap[num] = i
        
        return []


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Input: nums={nums1}, target={target1}")
    print(f"Output: {solution.twoSum(nums1, target1)}")  # [0, 1]
    
    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    print(f"Input: nums={nums2}, target={target2}")
    print(f"Output: {solution.twoSum(nums2, target2)}")  # [1, 2]
    
    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    print(f"Input: nums={nums3}, target={target3}")
    print(f"Output: {solution.twoSum(nums3, target3)}")  # [0, 1]
