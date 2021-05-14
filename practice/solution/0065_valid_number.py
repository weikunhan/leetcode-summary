class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """

        value_list = [{'blank': 0, 'sign': 1, 'digital': 2, '.': 3}, # 0
                      {'digital': 2, '.': 3},                        # 1
                      {'digital': 2, '.': 4, 'e': 5, 'blank': 8},    # 2
                      {'digital': 4},                                # 3
                      {'digital': 4, 'e': 5, 'blank': 8},            # 4
                      {'sign': 6, 'digital': 7},                     # 5
                      {'digital': 7},                                # 6
                      {'digital': 7, 'blank': 8},                    # 7
                      {'blank': 8}]                                  # 8
        count = 0
        res = False
        
        for char in s:
            if char in '0123456789':
                char = 'digital'
            elif char in ' ':
                char = 'blank'
            elif char in '+-':
                char = 'sign'
            elif char in 'eE':
                char = 'e'
            else:
                pass

            if not char in value_list[count]:
                
                return res
            
            count = value_list[count][char]
            
        if not count in [2, 4, 7, 8]:
            
            return res
        else:
            res = True
            
        return res