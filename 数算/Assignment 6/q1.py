class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def back(num_list:List[int],ans_list):
            if not num_list:
                ans.append(ans_list)
                return
            for i in range(len(num_list)):
                back(num_list[:i]+num_list[i+1:],ans_list+[num_list[i]])
        back(nums,[])
        return ans
