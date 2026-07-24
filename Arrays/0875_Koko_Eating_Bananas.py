import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        #the smallest value that works
        answer=right
        while left<=right:
            #current speed we are checking
            mid=(left+right)//2
            #calculate how many hours it takes to eat all bananas with current speed
            hours=0
            for pile in piles:
                hours+=math.ceil(pile/mid)
            if hours<=h:
                answer=mid
                right=mid-1
            else:
                left=mid+1
        return answer
if __name__ == '__main__':
    piles = [3, 6, 7, 11]
    h = 8
    print(Solution().minEatingSpeed(piles, h))
