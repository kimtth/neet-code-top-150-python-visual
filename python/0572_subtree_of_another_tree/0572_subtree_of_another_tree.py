from typing import Optional


"""
LeetCode Subtree of Another Tree

Problem from LeetCode: https://leetcode.com/problems/subtree-of-another-tree/

Description:
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values as subRoot and false otherwise.
A subtree of a binary tree is a tree that consists of a node in the original tree and all of this node's descendants.

Example 1:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
"""

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def is_subtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]
        ) ->bool:
        """
        Check if subRoot is a subtree of root.
        
        Args:
            root: Root of the main tree
            subRoot: Root of the potential subtree
            
        Returns:
            bool: True if subRoot is a subtree of root, False otherwise
        """
        if not root:
            return False
        if self._isSameTree(root, subRoot):
            return True
        return self.is_subtree(root.left, subRoot) or self.is_subtree(root.right, subRoot)

    def _isSameTree(self, s: Optional[TreeNode], t: Optional[TreeNode]) ->bool:
        """
        Check if two trees are identical.
        
        Args:
            s: Root of the first tree
            t: Root of the second tree
            
        Returns:
            bool: True if the trees are identical, False otherwise
        """
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val != t.val:
            return False
        return self._isSameTree(s.left, t.left) and self._isSameTree(s.
            right, t.right)

    def isSubtree_serialize(self, root: Optional[TreeNode], subRoot:
        Optional[TreeNode]) ->bool:
        """
        Check if subRoot is a subtree of root using serialization.
        
        Args:
            root: Root of the main tree
            subRoot: Root of the potential subtree
            
        Returns:
            bool: True if subRoot is a subtree of root, False otherwise
        """

        def serialize(node: Optional[TreeNode]) ->str:
            """Serialize a tree to a string."""
            if not node:
                return '#'
            return f',{node.val}{serialize(node.left)}{serialize(node.right)}'
        return serialize(subRoot) in serialize(root)

    def isSubtree_efficient(self, root: Optional[TreeNode], subRoot:
        Optional[TreeNode]) ->bool:
        """
        More efficient implementation avoiding redundant comparisons.
        
        Args:
            root: Root of the main tree
            subRoot: Root of the potential subtree
            
        Returns:
            bool: True if subRoot is a subtree of root, False otherwise
        """
        if not subRoot:
            return True
        if not root:
            return False

        def dfs_find(node: Optional[TreeNode], target: int) ->list:
            """Find all nodes with the value equal to target."""
            if not node:
                return []
            result = []
            if node.val == target:
                result.append(node)
            result.extend(dfs_find(node.left, target))
            result.extend(dfs_find(node.right, target))
            return result
        candidates = dfs_find(root, subRoot.val)
        for candidate in candidates:
            if self._isSameTree(candidate, subRoot):
                return True
        return False


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1: Create the main tree [3,4,5,1,2]
    root1 = TreeNode(3)
    root1.left = TreeNode(4)
    root1.right = TreeNode(5)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(2)
    
    # Create the subtree [4,1,2]
    subRoot1 = TreeNode(4)
    subRoot1.left = TreeNode(1)
    subRoot1.right = TreeNode(2)
    
    result1 = solution.is_subtree(root1, subRoot1)
    print(f"Example 1: {result1}")  # Expected output: True
    
    # Example 2: Create the main tree [3,4,5,1,2,null,null,null,null,0]
    root2 = TreeNode(3)
    root2.left = TreeNode(4)
    root2.right = TreeNode(5)
    root2.left.left = TreeNode(1)
    root2.left.right = TreeNode(2)
    root2.left.right.left = TreeNode(0)
    
    # Use the same subtree [4,1,2]
    result2 = solution.is_subtree(root2, subRoot1)
    print(f"Example 2: {result2}")  # Expected output: False
