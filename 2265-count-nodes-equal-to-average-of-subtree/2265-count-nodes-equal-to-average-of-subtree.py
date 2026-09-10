# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfSubtree(self, root):
        self.count=0
        def dfs(root):
            if not root:
                return (0,0)
            left_sum, left_count=dfs(root.left)
            right_sum, right_count=dfs(root.right)

            curr_sum=left_sum+right_sum+root.val
            curr_count=left_count+right_count+1

            if root.val==curr_sum//curr_count:
                self.count+=1
            return (curr_sum,curr_count)

        dfs(root)
        return self.count

            
        