class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        
        sign = 1
        value_dict = {}
        res = ''
        
        if numerator % denominator == 0:
            res = str(numerator//denominator)
            
            return res
        
        if numerator * denominator < 0:
            sign = -1
            
        carry, remainder = divmod(abs(numerator),abs(denominator))     
        res = str(carry)
            
        if sign == -1:
            res = '-' + res
            
        if remainder:
            res += '.'
            
        value_dict[remainder] = len(res)
        
        while remainder:
            carry, remainder = divmod(remainder * 10, abs(denominator))
            res += str(carry)
            
            if remainder in value_dict:
                res = res[:value_dict[remainder]] + '(' + res[value_dict[remainder]:] + ')'
                
                return res
                
            value_dict[remainder] = len(res)
            
        return res