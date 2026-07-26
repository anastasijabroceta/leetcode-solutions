
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        seen = {}
        for str in strs:
            sorted_str = ''.join(sorted(str))
            if sorted_str in seen:
                ans[seen[sorted_str]].append(str)
            else:
                seen[sorted_str] = len(ans)
                ans.append([str])
        return ans

if __name__ == "__main__":
    sol = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    ans = sol.groupAnagrams(strs)
    print(ans)


