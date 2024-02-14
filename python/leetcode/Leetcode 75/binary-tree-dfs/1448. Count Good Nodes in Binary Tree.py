# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """Calculate the number of nodes that are the maximum value from root to the node"""

        def dfs(node, max_val):
            if not node:
                return 0
            max_val = max(max_val, node.val)
            return (
                (node.val >= max_val)
                + dfs(node.left, max_val)
                + dfs(node.right, max_val)
            )

        return dfs(root, root.val)

    def goodNodesIterative(self, root: TreeNode) -> int:
        """Calculate the number of nodes that are the maximum value from root to the node"""

        q = deque([(root, root.val)])

        count = 0
        while q:
            cur_node, max_val = q.popleft()

            if cur_node.val >= max_val:
                count += 1

            if cur_node.left is not None:
                q.append((cur_node.left, max(max_val, cur_node.val)))

            if cur_node.right is not None:
                q.append((cur_node.right, max(max_val, cur_node.val)))

        return count


if __name__ == "__main__":
    s = Solution()
    # [2,null,4,10,8,null,null,4]
    Tree = TreeNode(2, None, TreeNode(4, TreeNode(10, TreeNode(8), TreeNode(4))))

    print(s.goodNodes(Tree))
    print(s.goodNodesIterative(Tree))
