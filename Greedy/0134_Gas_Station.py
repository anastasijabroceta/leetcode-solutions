from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        tank = 0
        start = 0
        for i in range(len(gas)):
            difference= gas[i] - cost[i]
            total += difference
            tank += difference
            if tank < 0:
                start = i + 1
                tank = 0
        if total<0:
            return -1
        return start
if __name__=="__main__":
    nums=[1,2,3,4,5]
    cost = [3, 4, 5, 1, 2]
    print(Solution().canCompleteCircuit(nums, cost))