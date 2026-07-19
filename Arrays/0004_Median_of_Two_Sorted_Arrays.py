"""
LeetCode #4 - Median of Two Sorted Arrays

Difficulty: Hard

Topics:
- Array
- Binary Search
- Divide and Conquer

Approach 1:
- Spojiti oba niza.
- Sortirati spojeni niz.
- Ako je broj elemenata neparan, vratiti srednji element.
- Ako je broj elemenata paran, vratiti prosek dva srednja elementa.

Time Complexity:
O((m+n) log(m+n))

Space Complexity:
O(m+n)
"""
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        merged = nums1 + nums2
        merged.sort()

        n = len(merged)

        if n % 2 == 1:
            return float(merged[n // 2])

        middle_right = n // 2
        middle_left = middle_right - 1

        return (merged[middle_left] + merged[middle_right]) / 2
"""
LeetCode #4 - Median of Two Sorted Arrays

Difficulty: Hard

Topics:
- Array
- Binary Search
- Divide and Conquer

Approach:
- Binary search is performed on the shorter array.
- Both arrays are partitioned into left and right parts.
- A valid partition satisfies:
    max_left1 <= min_right2
    max_left2 <= min_right1
- For an odd total number of elements, the median is the largest
  element on the left side.
- For an even total number of elements, the median is the average
  of the largest left element and the smallest right element.

Time Complexity:
O(log(min(m, n)))

Space Complexity:
O(1)
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(A) > len(B):
            A, B = B, A
        l,r = 0, len(A) - 1

        while True:
            i=(l+r)//2 #A
            j=half-i-2 #B

            Aleft=A[i] if i>=0 else float('-inf')
            Aright=A[i+1] if i+1<len(A) else float('inf')
            Bleft=B[j] if j>=0 else float('-inf')
            Bright=B[j+1] if j+1<len(B) else float('inf')

            #partition is correct
            if Aleft<=Bright and Bleft<=Aright:
                #odd
                if total%2:
                    return min(Aright,Bright)
                #even
                return (max(Aleft,Bleft)+min(Aright,Bright))/2
            elif Aleft>Bright:
                r=i-1
            else:
                l=i+1



if __name__ == "__main__":
    solution = Solution()

    print(solution.findMedianSortedArrays([1, 3], [2]))
    print(solution.findMedianSortedArrays([1, 2], [3, 4]))
