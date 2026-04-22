class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letnum = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz",
        }
        res = []
        def dfs(index,path: str):
            if len(path) == len(digits):
                res.append(path)
                return
            for chi in letnum[digits[index]]:
                dfs(index+1,path + chi)

        if digits:
            dfs(0,"")
        return res

