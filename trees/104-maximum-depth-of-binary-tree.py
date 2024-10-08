"""
104. Maximum Depth of Binary Tree
Easy

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
 
Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:

Input: root = [1,null,2]
Output: 2

 
Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100


"""

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepthDfs(self, root: TreeNode) -> int:
        """Calculate max depth through recursive DFS."""
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepthBfs(self, root: TreeNode) -> int:
        """Calculate max depth through BFS."""
        if not root:
            return 0
        q = deque([root])
        depth = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.enqueue(node.left)
                if node.right:
                    q.enqueue(node.right)
            depth += 1
        return depth

    def maxDepthDfsIterative(self, root: TreeNode) -> int:
        """Calculate max depth through iterative DFS."""
        stack = [(root, 1)]
        result = 0
        while stack:
            node, depth = stack.pop()
            if node:
                result = max(result, depth)
                stack.append((node.right, depth + 1))
                stack.append((node.left, depth + 1))
        return result
