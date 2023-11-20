import math

class Solution:
    def trailingZeros(self, n):
        kVal5 = math.floor(math.log(n, 5))
        res = 0
        for i in range(1, kVal5+1):
            res += math.floor(n / pow(5, i))
        return res

#driver
if __name__ == "__main__":
    n = int(input())
    print(Solution().trailingZeros(n))
