class Solution:
    """
    @param: : An integer
    @param: : An integer
    @return: An integer denote the count of digit k in 1..n
    """

    def digitCounts(self, k, n):
        k = str(k)
        s = 0
        for i in range(n+1):
            s += str(i).count(k)
        return s
