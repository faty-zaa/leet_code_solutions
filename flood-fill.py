from collections import deque
class Solution:
    def get_neigb(self, num, image):
        cols = len(image[0])
        rows = len(image)
        x = num[0]
        y = num[1]
        neighb = [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1)
        ]

        return [
            (nx, ny)
            for nx, ny in neighb
            if 0 <= nx < rows and 0 <= ny < cols
        ]

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        queue = deque([(sr, sc)])
        visited = {}
        # image_f = image.copy()
        i = 0
        num = image[sr][sc]
        while queue:
            q = queue.popleft()
            if q not in visited :
                if image[q[0]][q[1]] == num:
                    image[q[0]][q[1]] = color
                    visited[q] = True
                    neighb = self.get_neigb(q, image)
                    queue.extend(neighb)
        return image
            


        