from ast import List


class Solution(object):
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest_sum = nums[0] + nums[1] + nums[2]
        nums.sort()

        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if abs(current_sum-target) < abs(closest_sum-target):
                    closest_sum = current_sum
                if current_sum==target:
                    return current_sum
                if current_sum<target:
                    left += 1
                else:
                    right -= 1
        return closest_sum
if __name__=="__main__":
    nums = [-1,2,1,-4]
    target = 1
    print(Solution().threeSumClosest(nums, target))

