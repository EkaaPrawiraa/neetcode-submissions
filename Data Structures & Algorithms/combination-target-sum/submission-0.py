class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(index, path, total):
            if total == target:
                res.append(path.copy())
                return
            for i in range(index, len(nums)):
                if total + nums[i] > target:
                    return
                path.append(nums[i])
                dfs(i, path, total + nums[i])
                path.pop()
        dfs(0, [],0)
        return res