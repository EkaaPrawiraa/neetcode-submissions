class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        def dfs(index, path):
            res.add(tuple(path))
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                dfs(i+1,path)
                path.pop()
        dfs(0, [])
        return [list(r) for r in res]
        