import heapq

class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: List[int]
        """
        
        data_value_dict = {}
        visit_value_dict = set()
        value_pq = []
        res = [0] * len(workers)
        
        for i in range(len(workers)):
            value_list = []
            
            for j in range(len(bikes)):
                temp_value = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
                value_list.append((temp_value, i, j))
                
            data_value_dict[i] = sorted(value_list, reverse=True)
            
        for key, value in data_value_dict.items():
            temp_value = value.pop()
            heapq.heappush(value_pq, temp_value)
            
        while len(visit_value_dict) < len(workers):
            cost, worker, bike = heapq.heappop(value_pq)
            
            if not bike in visit_value_dict:
                res[worker] = bike
                visit_value_dict.add(bike)
            else:
                temp_value = data_value_dict[worker].pop()
                heapq.heappush(value_pq, temp_value) 
                
        return res