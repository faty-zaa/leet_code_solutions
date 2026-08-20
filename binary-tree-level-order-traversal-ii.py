# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        output_lst = []
        while queue:
            size = len(queue)
            output = []
            for _ in range(size):
                q = queue.popleft()
                output.append(q.val)
                if q.left:
                    queue.append(q.left)
                if q.right:
                    queue.append(q.right)
            if output:
                output_lst.append(output)
        output_lst.reverse()
        return output_lst