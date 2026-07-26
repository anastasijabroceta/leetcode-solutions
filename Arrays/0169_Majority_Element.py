from ast import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        seen = {}
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1

        for i in seen:
            if seen[i] >= len(nums) /2:
                return i



if __name__ == '__main__':
    nums = [2,2,1,1,1,2,2]
    solution = Solution()
    print(solution.majorityElement(nums))