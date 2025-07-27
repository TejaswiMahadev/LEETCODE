class Solution(object):
    def reverse(self,x):
        sign = -1 if x < 0 else 1
        x = abs(x)
        reverse_number = 0 

        while x > 0:
            digit = x % 10
            x = x // 10

            if reverse_number > (2147483647 - digit) //10:
                return 0
            reverse_number = reverse_number*10 + digit

        return sign * reverse_number
