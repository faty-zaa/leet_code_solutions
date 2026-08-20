# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return [0.0]
        queue = deque([root])
        output = []
        while(queue):
            size = len(queue)
            num = 0
            for _ in range(size):
                q = queue.popleft()
                num += q.val
                if q.left:
                    queue.append(q.left)
                if q.right:
                    queue.append(q.right)
            output.append((num / size))
        return output
        
