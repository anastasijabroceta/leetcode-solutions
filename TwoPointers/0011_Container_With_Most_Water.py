"""
LeetCode #11 - Container With Most Water

Difficulty: Medium

Topics:
- Array
- Two Pointers
- Greedy

Approach:
- Postaviti jedan pokazivač na početak, a drugi na kraj niza.
- Izračunati površinu između trenutnih linija.
- Zapamtiti najveću pronađenu površinu.
- Pomeriti pokazivač koji se nalazi na nižoj liniji,
  jer ona ograničava visinu vode.

Time Complexity:
O(n)

Space Complexity:
O(1)
"""

"""Brute force O(n*n) solution"""
class Solution:
    def maxArea(self, height):
        max_area = 0

        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                width = j - i
                container_height = min(height[i], height[j])
                area = width * container_height

                max_area = max(max_area, area)

        return max_area
class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            container_height = min(height[left], height[right])
            area = width * container_height

            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
if __name__ == '__main__':
    print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
