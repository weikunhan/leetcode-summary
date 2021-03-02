import collections

class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        
        value_dict = collections.Counter()
        value_stack = []
        word_value = ''
        sum_value = 0
        count = 0
        temp_value = 1 
        res = ''
        
        for char in formula[::-1]:
            if char == ")":
                if not sum_value:
                    value_stack.append(1)
                    temp_value *= 1
                else:
                    value_stack.append(sum_value)
                    temp_value *= sum_value
    
                sum_value = 0
                count = 0
            elif char.isupper():
                word_value += char
                
                if not sum_value:
                    value_dict[word_value[::-1]] += temp_value
                else:
                    value_dict[word_value[::-1]] += sum_value * temp_value
                    
                word_value = ""
                sum_value = 0
                count = 0
            elif char == "(":
                sum_value = value_stack.pop()
                temp_value //= sum_value
                sum_value = 0
                count = 0
            elif char.isdigit():
                sum_value += int(char) * (10 ** count)
                count += 1
            elif char.islower():
                word_value += char
                
        for key, value in sorted(value_dict.items()):
            if value > 1:
                res += key + str(value)
            else:
                res += key
                
        return res