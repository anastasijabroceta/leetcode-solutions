from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def dfs(row, col):
            # Ako smo izašli izvan matrice, zavrsi
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return

            # Ako je voda ili već posjećeno kopno zavrsi
            if grid[row][col] == "0":
                return

            # Označavamo trenutno kopno kao posjećeno.
            grid[row][col] = "0"

            # Obilazimo četiri susjedna polja.
            dfs(row - 1, col)  # gore
            dfs(row + 1, col)  # dole
            dfs(row, col - 1)  # lijevo
            dfs(row, col + 1)  # desno

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    islands += 1
                    dfs(row, col)

        return islands
if __name__ == "__main__":

    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]

    solution = Solution()

    print(solution.numIslands(grid))