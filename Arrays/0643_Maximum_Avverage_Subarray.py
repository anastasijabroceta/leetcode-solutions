class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_sum = sum(nums[:k])
        current_sum = max_sum

        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            '''-outcoming num + incoming num'''
            max_sum = max(max_sum, current_sum)

        return max_sum / k
if __name__=="__main__":
    nums = [1,12,-5,-6,50,3]
    k = 4
    print(Solution().findMaxAverage(nums, k))

