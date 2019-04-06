# -*- coding: utf-8 -*-
# AUTHOR = "tylitianrui"


class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: The sum of a and b
    """

    def aplusb(self, a, b):
        # write your code here
        carry = 1
        while carry:
            s = a ^ b
            carry = 0xFFFFFFFF & ((a & b) << 1)
            carry = -(~(carry - 1) & 0xFFFFFFFF) if carry > 0x7FFFFFFF else carry
            a = s
            b = carry
        return a


if __name__ == '__main__':
    solution = Solution()
    print(solution.aplusb(1, 2))
    print(solution.aplusb(1, -2))
