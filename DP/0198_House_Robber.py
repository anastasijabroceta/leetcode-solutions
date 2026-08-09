from typing import List


"""class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp=[0]*len(nums)
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i]=max(dp[i-1],nums[i]+dp[i-2])
        return dp[-1]"""
#0(1):
class Solution:
    def rob(self, nums):
        previous_two = 0
        previous_one = 0

        for money in nums:
            current = max(
                previous_one,
                money + previous_two
            )

            previous_two = previous_one
            previous_one = current

        return previous_one
if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3, 1]
    print(sol.rob(nums))

