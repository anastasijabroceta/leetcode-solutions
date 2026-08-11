from ast import List
'''Move zeros to right'''


class Solution:
    def moveZeroes(self, nums):
        insert = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert], nums[i] = nums[i], nums[insert]
                insert += 1
if __name__ == "__main__":
    sol = Solution()
    nums = [0, 1, 0, 3, 12]
    sol.moveZeroes(nums)
    print(nums)
