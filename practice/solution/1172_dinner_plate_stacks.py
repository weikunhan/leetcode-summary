import heapq

class DinnerPlates(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        
        self.capacity_value = capacity
        self.value_pq = [] 
        self.value_stack = [] 

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        
        while self.value_pq and self.value_pq[0] < len(self.value_stack) and len(self.value_stack[self.value_pq[0]]) == self.capacity_value:
            heapq.heappop(self.value_pq)
        
        if not self.value_pq:
            heapq.heappush(self.value_pq, len(self.value_stack))
            
        if self.value_pq[0] == len(self.value_stack):
            self.value_stack.append([])
            
        self.value_stack[self.value_pq[0]].append(val)
            
    def pop(self):
        """
        :rtype: int
        """
        
        temp_value = -1
        
        while self.value_stack and not self.value_stack[-1]:
            self.value_stack.pop()
            
        if self.value_stack and self.value_stack[-1]:
            heapq.heappush(self.value_pq, len(self.value_stack) - 1)
            temp_value = self.value_stack[-1].pop()
        
        return temp_value

    def popAtStack(self, index):
        """
        :type index: int
        :rtype: int
        """
        
        temp_value = -1
        
        if index < len(self.value_stack) and self.value_stack[index]:
            heapq.heappush(self.value_pq, index)
            temp_value = self.value_stack[index].pop()

        return temp_value
        

# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)