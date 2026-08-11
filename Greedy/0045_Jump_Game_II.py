from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            #Koliko najdalje možemo stici
            farthest = max(farthest, i + nums[i])

            if i == current_end:#Završili smo trenutni skok/zonu
                jumps += 1
                current_end = farthest

        return jumps
