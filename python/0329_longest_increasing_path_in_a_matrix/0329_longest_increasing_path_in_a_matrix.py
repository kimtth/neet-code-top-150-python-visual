from typing import List
from collections import deque


"""
LeetCode Longest Increasing Path In A Matrix

Problem from LeetCode: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

Description:
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

Example 1:
Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:
Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

Example 3:
Input: matrix = [[1]]
Output: 1

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 2^31 - 1
"""

class Solution:

    def longest_increasing_path(self, matrix: List[List[int]]) ->int:
        """
        Find the length of the longest increasing path in the matrix.
        
        Args:
            matrix: 2D array representing the matrix
            
        Returns:
            int: Length of the longest increasing path
        """
        if not matrix or not matrix[0]:
            return 0
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(matrix), len(matrix[0])
        cache = [([0] * n) for _ in range(m)]

        def dfs(i, j):
            if cache[i][j] != 0:
                return cache[i][j]
            max_length = 1
            for di, dj in dirs:
                x, y = i + di, j + dj
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    max_length = max(max_length, 1 + dfs(x, y))
            cache[i][j] = max_length
            return max_length
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))
        return ans

    def longest_increasing_path_topological(self, matrix: List[List[int]]
        ) ->int:
        """
        Find the length of the longest increasing path using topological sort.
        
        Args:
            matrix: 2D array representing the matrix
            
        Returns:
            int: Length of the longest increasing path
        """
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        in_degree = [([0] * n) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] < matrix[
                        i][j]:
                        in_degree[i][j] += 1
        queue = deque()
        for i in range(m):
            for j in range(n):
                if in_degree[i][j] == 0:
                    queue.append((i, j))
        path_length = 0
        while queue:
            path_length += 1
            size = len(queue)
            for _ in range(size):
                i, j = queue.popleft()
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[
                        i][j]:
                        in_degree[ni][nj] -= 1
                        if in_degree[ni][nj] == 0:
                            queue.append((ni, nj))
        return path_length


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    matrix1 = [
        [9, 9, 4],
        [6, 6, 8],
        [2, 1, 1]
    ]
    result1 = solution.longest_increasing_path(matrix1)
    print(f"Example 1: {result1}")  # Expected output: 4
    
    # Example 2
    matrix2 = [
        [3, 4, 5],
        [3, 2, 6],
        [2, 2, 1]
    ]
    result2 = solution.longest_increasing_path(matrix2)
    print(f"Example 2: {result2}")  # Expected output: 4
    
    # Example 3
    matrix3 = [[1]]
    result3 = solution.longest_increasing_path(matrix3)
    print(f"Example 3: {result3}")  # Expected output: 1
    
    # Using topological sort approach
    print("\nUsing topological sort approach:")
    result4 = solution.longest_increasing_path_topological(matrix1)
    print(f"Example 1: {result4}")  # Expected output: 4
