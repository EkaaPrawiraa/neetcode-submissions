class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        res, _ = zip(*counter.most_common(k))
        return list(res)
