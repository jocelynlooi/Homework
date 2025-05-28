class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def divide(ans_list,word):
            if len(word) == 0:
                ans.append(ans_list)
                return
            for i in range(1,len(word)+1):
                if word[:i] == word[:i][::-1]:
                    divide(ans_list+[word[:i]],word[i:])
        divide([],s)
        return ans

