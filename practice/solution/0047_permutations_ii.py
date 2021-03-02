class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        self.res = []
        
        self.dfs(0, sorted(candidates), target, [])
        
        return self.res
    
    def dfs(self, start, candidates, target, value_list):
        if target < 0:
            
            return
        
        if not target:
            self.res.append(value_list)
            
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
                
            self.dfs(i + 1, candidates, target - candidates[i], value_list + [candidates[i]])