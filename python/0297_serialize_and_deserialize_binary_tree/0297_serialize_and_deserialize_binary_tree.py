from typing import List, Optional
from collections import deque


"""
LeetCode 297: Serialize and Deserialize Binary Tree

Problem from LeetCode: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

Serialization is the process of converting a data structure or object into a sequence of bits so that 
it can be stored in a file or memory buffer, or transmitted across a network connection link to be 
reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your 
serialization/deserialization algorithm should work. You just need to ensure that a binary tree can 
be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do 
not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Example 1:
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Example 2:
Input: root = []
Output: []

Constraints:
- The number of nodes in the tree is in the range [0, 10^4]
- -1000 <= Node.val <= 1000
"""

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    """
    Serializes and deserializes a binary tree.
    Uses a preorder traversal approach with comma-separated values.
    """

    def serialize(self, root: Optional[TreeNode]) ->str:
        """
        Encodes a tree to a single string.
        
        Args:
            root: Root of the binary tree
            
        Returns:
            str: Serialized string representation of the tree
        """
        result = []

        def dfs(node):
            if not node:
                result.append('None')
                return
            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ','.join(result)

    def deserialize(self, data: str) ->Optional[TreeNode]:
        """
        Decodes your encoded data to tree.
        
        Args:
            data: Serialized string representation of the tree
            
        Returns:
            TreeNode: Root of the reconstructed binary tree
        """
        values = data.split(',')
        self.i = 0

        def dfs():
            if self.i >= len(values) or values[self.i] == 'None':
                self.i += 1
                return None
            node = TreeNode(int(values[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()


class CodecAlternative:
    """
    Alternative implementation using list processing.
    """

    def serialize(self, root: Optional[TreeNode]) ->str:
        """
        Encodes a tree to a single string.
        
        Args:
            root: Root of the binary tree
            
        Returns:
            str: Serialized string representation of the tree
        """

        def recserialize(root, string):
            if not root:
                string += 'None,'
            else:
                string += str(root.val) + ','
                string = recserialize(root.left, string)
                string = recserialize(root.right, string)
            return string
        return recserialize(root, '')

    def deserialize(self, data: str) ->Optional[TreeNode]:
        """
        Decodes your encoded data to tree.
        
        Args:
            data: Serialized string representation of the tree
            
        Returns:
            TreeNode: Root of the reconstructed binary tree
        """

        def recdeserialize(string_deque):
            if string_deque[0] == 'None':
                string_deque.popleft()
                return None
            root = TreeNode(int(string_deque[0]))
            string_deque.popleft()
            root.left = recdeserialize(string_deque)
            root.right = recdeserialize(string_deque)
            return root
        string_list = data.split(',')
        if string_list[-1] == '':
            string_list.pop()
        string_deque = deque(string_list)
        return recdeserialize(string_deque)


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    # Create a sample tree: [1,2,3,null,null,4,5]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    
    codec = Codec()
    
    # Serialize the tree
    serialized = codec.serialize(root)
    print(f"Serialized tree: {serialized}")
    
    # Deserialize back to a tree
    deserialized_root = codec.deserialize(serialized)
    
    # Verify by serializing again
    serialized_again = codec.serialize(deserialized_root)
    print(f"Serialized again: {serialized_again}")
    
    # Verify both serializations match
    print(f"Serializations match: {serialized == serialized_again}")
