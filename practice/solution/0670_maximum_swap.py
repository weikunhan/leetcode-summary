class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        value_list = list(str(num))
        value_dict = {}
        res = num
            
        for i in range(len(value_list)):
            value_dict[value_list[i]] = i 

        for i in range(len(value_list)):
            for j in reversed(range(int(value_list[i]) + 1, 10)):
                if str(j) in value_dict and value_dict[str(j)] > i:
                    # temp =  value_list[value_dict[str(j)]]
                    # value_list[value_dict[str(j)]] = value_list[i]
                    # value_list[i] = temp
                    value_list[value_dict[str(j)]], value_list[i] = value_list[i], value_list[value_dict[str(j)]]
                    res = int(''.join(value_list))

                    return res
                
        return res