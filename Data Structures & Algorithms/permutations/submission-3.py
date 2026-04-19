class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(path):
            if len(path) == len(nums):
                res.append(path.copy())
            for i in range(len(nums)):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                dfs(path)
                path.pop()
        dfs([])
        return res