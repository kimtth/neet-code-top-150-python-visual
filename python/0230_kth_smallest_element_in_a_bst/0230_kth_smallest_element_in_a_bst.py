"""
230. Kth Smallest Element in a BST
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Given the root of a binary search tree, and an integer k, return the kth 
smallest value (1-indexed) of all the values of the nodes in the tree.

Time Complexity: O(H + k) where H is the height of the tree
Space Complexity: O(H) for the stack
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Inorder traversal gives sorted order in BST.
        Use iterative approach with a stack.
        """
        stack = []
        current = root
        count = 0
        
        while stack or current:
            # Go to leftmost node
            while current:
                stack.append(current)
                current = current.left
            
            # Process node
            current = stack.pop()
            count += 1
            
            if count == k:
                return current.val
            
            # Move to right subtree
            current = current.right
        
        return -1  # k is larger than tree size
    
    def kthSmallestRecursive(self, root: Optional[TreeNode], k: int) -> int:
        """Alternative recursive solution with early termination."""
        self.count = 0
        self.result = None
        
        def inorder(node):
            if not node or self.result is not None:
                return
            
            inorder(node.left)
            
            self.count += 1
            if self.count == k:
                self.result = node.val
                return
            
            inorder(node.right)
        
        inorder(root)
        return self.result


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: [3,1,4,null,2], k=1
    #     3
    #    / \
    #   1   4
    #    \
    #     2
    root1 = TreeNode(3)
    root1.left = TreeNode(1)
    root1.right = TreeNode(4)
    root1.left.right = TreeNode(2)
    
    print(f"Tree: [3,1,4,null,2], k=1")
    print(f"Output: {solution.kthSmallest(root1, 1)}")  # 1
    
    # Test case 2: [5,3,6,2,4,null,null,1], k=3
    #       5
    #      / \
    #     3   6
    #    / \
    #   2   4
    #  /
    # 1
    root2 = TreeNode(5)
    root2.left = TreeNode(3)
    root2.right = TreeNode(6)
    root2.left.left = TreeNode(2)
    root2.left.right = TreeNode(4)
    root2.left.left.left = TreeNode(1)
    
    print(f"Tree: [5,3,6,2,4,null,null,1], k=3")
    print(f"Output: {solution.kthSmallest(root2, 3)}")  # 3
