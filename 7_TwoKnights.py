class Solution:
    def twoKnights(self, n):
        res = []
        for i in range(1, n+1):
            res.append(int((pow(i, 2)* (pow(i,2) - 1)) / 2) - 4*(i-2)*(i-1))
        return res

#driver
if __name__ == "__main__":
    n = int(input())
    result = Solution().twoKnights(n)
    for i in result:
        print(i)
