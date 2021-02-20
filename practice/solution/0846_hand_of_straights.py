class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        
        value_dict = collections.Counter(hand)
        res = False
        
        for key in sorted(set(hand)):
            if value_dict[key] > 0:
                for i in reversed(range(W)):
                    value_dict[key + i] -= value_dict[key]
                    
                    if value_dict[key + i] < 0:
                        
                        return res
               
        res = True   
        
        return res