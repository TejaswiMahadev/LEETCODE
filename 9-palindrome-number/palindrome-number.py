class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False  
        original = x
        reverse_number = 0

        while x > 0:
            digit = x % 10
            x = x // 10
            reverse_number = reverse_number * 10 + digit

        return original == reverse_number
