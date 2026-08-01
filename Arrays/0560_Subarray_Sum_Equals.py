class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count={0: 1}
        prefix_sum=0
        count=0
        for num in nums:
            prefix_sum+=num
            needed_sum=prefix_sum-k
            if needed_sum in prefix_count:
               count+=prefix_count[needed_sum]
            prefix_count[prefix_sum]=(prefix_count.get(prefix_sum,0)+1)
        return count
if __name__ == '__main__':
    nums = [1, 2, 3]
    k = 3
    solution = Solution()
    print(solution.subarraySum(nums, k))

