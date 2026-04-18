class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def dfs(path):
            if len(path)==len(nums):
                res.add(tuple(path))
                return
            for i in range(len(nums)):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                dfs(path)
                path.pop()
        dfs([])
        return [list(r) for r in res]
        