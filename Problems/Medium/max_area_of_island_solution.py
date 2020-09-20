class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        island_tracker = set()
        max_size = 0

        for idx, row in enumerate(grid):
            if 1 not in row:
                continue

            for one in [idx for idx, val in enumerate(row) if val == 1]:
                if (idx, one) in island_tracker:
                    continue

                # use a stack to gather up part of the island
                queue = deque([(idx, one)])
                island_tracker.add((idx,one))
                new_size = 0
                while queue:
                    coord = queue.pop()
                    new_size += 1

                    c0, c1 = coord[0], coord[1]

                    [(island_tracker.add((x,y)), queue.append((x,y))) for x,y in [(c0-1,c1),(c0+1,c1),(c0,c1-1),(c0,c1+1)] if (x,y) not in island_tracker and 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y]]

                max_size = max(max_size, new_size)

        return max_size
