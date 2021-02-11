import collections

class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        
        visit_value_dict = set(deadends)
        value_list = collections.deque([('0000', 0)])
        data_value_dict = {}
        res = -1
        
        if '0000' in visit_value_dict:
            
            return res
        
        for i in range(10):
            data_value_dict[str(i)] = [str((i + 1) % 10), str((i - 1) % 10)]
            
        while value_list:
            temp_value = len(value_list)
            
            for _ in range(temp_value):
                state, cost = value_list.popleft()
                
                if state == target:
                    res = cost
                    
                    return res
                
                for i in range(4):
                    first_value = state[:i] + data_value_dict[state[i]][0] + state[i + 1:]
                    second_value = state[:i] + data_value_dict[state[i]][1] + state[i + 1:]
                    
                    for move in [first_value, second_value]:
                        if not move in visit_value_dict:
                            value_list.append((move, cost + 1))
                            visit_value_dict.add(move)
                            
        return res