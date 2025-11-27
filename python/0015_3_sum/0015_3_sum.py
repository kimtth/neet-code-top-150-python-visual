from typing import List

"""
LeetCode 3Sum

Problem from LeetCode: https://leetcode.com/problems/3sum/

Description:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""

class Solution:
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        """
        Find all unique triplets in the array that sum to zero.
        
        Args:
            nums: Array of integers
            
        Returns:
            List[List[int]]: List of all unique triplets that sum to zero
        """
        if len(nums) < 3:
            return []
            
        # Sort the array to make it easier to handle duplicates
        nums.sort()
        result = []
        
        for i in range(len(nums) - 2):
            # Early exit: if the smallest number is positive, no triplet can sum to zero
            if nums[i] > 0:
                break
                
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            # Two-pointer approach for the remaining two elements
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    # Found a triplet
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for the second element
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    # Skip duplicates for the third element
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                        
                    left += 1
                    right -= 1
                    
        return result
    
    def three_sum_hash_set(self, nums: List[int]) -> List[List[int]]:
        """
        Alternative implementation using a hash set approach.
        
        Args:
            nums: Array of integers
            
        Returns:
            List[List[int]]: List of all unique triplets that sum to zero
        """
        res = set()  # Use set to avoid duplicate triplets
        nums.sort()
        
        for i in range(len(nums) - 2):
            # Early exit: if the smallest number is positive, no triplet can sum to zero
            if nums[i] > 0:
                break
                
            # Skip duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            # Use a hash set to find pairs
            seen = set()
            for j in range(i + 1, len(nums)):
                complement = -nums[i] - nums[j]
                if complement in seen:
                    # Store as tuple in set to avoid duplicates
                    res.add((nums[i], complement, nums[j]))
                seen.add(nums[j])
        
        # Convert back to list of lists
        return [list(triplet) for triplet in res]


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = solution.three_sum(nums1)
    print(f"Example 1: {nums1} -> {result1}")  # Expected output: [[-1,-1,2],[-1,0,1]]
    
    # Example 2
    nums2 = [0, 1, 1]
    result2 = solution.three_sum(nums2)
    print(f"Example 2: {nums2} -> {result2}")  # Expected output: []
    
    # Example 3
    nums3 = [0, 0, 0]
    result3 = solution.three_sum(nums3)
    print(f"Example 3: {nums3} -> {result3}")  # Expected output: [[0,0,0]]
    
    # Additional example
    nums4 = [-2, 0, 0, 2, 2]
    result4 = solution.three_sum(nums4)
    print(f"Example 4: {nums4} -> {result4}")  # Expected output: [[-2,0,2]]
