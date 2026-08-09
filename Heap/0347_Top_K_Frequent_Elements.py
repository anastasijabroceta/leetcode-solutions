import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter={}
        for num in nums:
            counter[num]=counter.get(num,0)+1 #ako kljuc ne postoji vraca se default 0
        heap=[]
        heapq.heapify(heap)

        for num,frequency in counter.items():
            heapq.heappush(heap,(-frequency,num))
        result=[]
        for _ in range(k):
            freq,num=heapq.heappop(heap)
            result.append(num)
        return result

if __name__ == "__main__":
    nums=[1,1,1,2,2,3]
    k=2
    print(Solution().topKFrequent(nums, k))
