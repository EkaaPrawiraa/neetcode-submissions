class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        while l<r:
            left = numbers[l]
            right = numbers[r]
            print(left,right)
            if (left + right) == target:
                return [l+1,r+1]
            elif (left + right ) < target:
                l +=1
            else:
                r -=1
