from ast import List
import heapq


class Solution:
    def kthLargest(self, nums: List[int], k: int) -> int:
        heap=[]
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0] #na kraju je najmanji među k najvećih, što je upravo k-ti najveći.
if __name__ == '__main__':
    nums = [1, 3, 5, 6, 7]
    k = 2
    print(Solution().kthLargest(nums, k))

