import collections

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        
        data_value_dict = set(''.join(words))
        degree_value_dict = collections.Counter(data_value_dict)
        value_graph = collections.defaultdict(list)
        value_list = collections.deque()
        res = ''

        for pair in zip(words, words[1:]):
            for a, b in zip(*pair):
                if a != b:
                    value_graph[a].append(b)
                    degree_value_dict[b] += 1
                    break

        if not value_graph and len(words) == 2 and len(words[0]) > len(words[1]):
            
            return res

        for key, value in degree_value_dict.items():
            if value == 1:
                value_list.append(key)
        
        while value_list:
            temp_value = len(value_list)
            
            for _ in range(temp_value):
                temp_node = value_list.popleft()
                res += temp_node
                
                for neighbor in value_graph[temp_node]:
                    degree_value_dict[neighbor] -= 1
                    
                    if degree_value_dict[neighbor] == 1:
                        value_list.append(neighbor)
        
        if set(res) != data_value_dict:
            res = ''
        
        return res