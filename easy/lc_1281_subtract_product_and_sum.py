# 1281. Subtract the Product and Sum of digits of an Integer.


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp = n
        addition = 0
        product = 1
        
        while temp>0:
            rem = temp%10
            temp = temp//10
            addition = addition+rem
            product = product*rem

            subtract = product - addition
        
        return subtract