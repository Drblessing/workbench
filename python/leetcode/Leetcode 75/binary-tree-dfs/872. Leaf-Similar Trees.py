# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """Return True if the leaf sequence of two binary trees are the same"""

        def dfs(node: TreeNode, leaves: list[int]) -> list[int]:
            if not node:
                return leaves
            if not node.left and not node.right:
                leaves.append(node.val)
            leaves = dfs(node.left, leaves)
            leaves = dfs(node.right, leaves)
            return leaves

        return dfs(root1, []) == dfs(root2, [])
