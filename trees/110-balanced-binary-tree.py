"""
110. Balanced Binary Tree
Easy

Given a binary tree, determine if it is height-balanced.

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:

Input: root = []
Output: true


Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104


"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # using global var similar to #543 for diameter
    def isBalancedSimple(self, root: TreeNode | None) -> bool:
        self.balanced = True

        def _height(node: TreeNode | None) -> int:
            """Returns height of subtree rooted at node by recursive DFS.

            Checks whether the tree is balanced during each recursive step by comparing the heights of subtrees.
            
            If unbalanced at any point, set the outer variable self.balanced to False.
            """
            if not node:
                return 0
            left = _height(node.left)
            right = _height(node.right)
            if abs(left - right) > 1:
                self.balanced = False
            return 1 + max(left, right)

        _height(root)
        return self.balanced

    # return 2 values in nested function
    def isBalanced(self, root: TreeNode | None) -> bool:
        def dfs(node: TreeNode | None) -> list:
            # return value is a list in the format: [is subtree rooted at node balanced?, height of node]
            if node is None:
                return [True, 0]
            left, right = dfs(node.left), dfs(node.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]

