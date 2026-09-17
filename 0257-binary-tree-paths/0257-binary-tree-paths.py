# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        ans = []
        def findPath(root, path):
            if root is None:
                return
            path += str(root.val)
            if root.left is None and root.right is None:
                ans.append(path)
                return
            path += "->"
            findPath(root.left, path)
            findPath(root.right, path)

        findPath(root, "")
        return ans
        