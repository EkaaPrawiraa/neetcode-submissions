class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(index, path):
            res.append(path.copy())
            for i in range(index, len(nums)):
                path.append(nums[i])
                dfs(i+1, path)
                path.pop()

        dfs(0,[])
        return res
        