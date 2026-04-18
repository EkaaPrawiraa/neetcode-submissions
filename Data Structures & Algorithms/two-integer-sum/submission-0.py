class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for i,n in enumerate(nums):
            rest = target - n
            if n in temp:
                return [temp.get(n), i]
            temp[rest] = i
        return []