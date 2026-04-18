class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def dfs(index,path):
            if len(path)==len(nums):
                res.add(tuple(path))
                return
            for i in range(len(nums)):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                dfs(i,path)
                path.pop()
        dfs(0,[])
        return [list(r) for r in res]
        