from multiprocessing.connection import answer_challenge
from typing import List


class Solution:


        def longestConsecutive(self, nums: List[int]) -> int:

            if not nums:
                return 0

            seen = set()

            for num in nums:
                seen.add(num)

            longest = 0

            for num in seen:

                # Da li je ovo početak sekvence?
                if num - 1 not in seen:

                    current = num
                    length = 1

                    while current + 1 in seen:
                        current += 1
                        length += 1

                    longest = max(longest, length)

            return longest
if __name__ == "__main__":
    sol = Solution()

    nums = [0,3,7,2,5,8,4,6,0,1]
    ans = sol.longestConsecutive(nums)

    print(ans)



