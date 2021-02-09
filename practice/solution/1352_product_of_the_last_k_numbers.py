class ProductOfNumbers(object):

    def __init__(self):
        
        self.value_list = [1]
        

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        
        if not num:
            self.value_list = [1]
        else:
            temp_value = self.value_list[-1] * num
            self.value_list.append(temp_value)

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        
        temp_value = 0
        
        if k >= len(self.value_list):
            
            return temp_value
        
        temp_value = self.value_list[-1] / self.value_list[-k - 1]
        
        return temp_value
        

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)