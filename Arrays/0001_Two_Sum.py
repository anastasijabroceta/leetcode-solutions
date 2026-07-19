"""
LeetCode #1 - Two Sum

Difficulty: Easy

Topics:
- Array
- HashMap

Approach 1:
Brute Force
Time: O(n²)
Space: O(1)

Approach 2:
HashMap
Time: O(n)
Space: O(n)
"""

class SolutionBruteForce:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


class SolutionHashMap:
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i