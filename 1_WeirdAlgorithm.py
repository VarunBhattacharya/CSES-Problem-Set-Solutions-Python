class Solution:
    def weirdAlgorithm(self, n):
        res = f"{str(n)} "
        while(n != 1):
            if n%2 == 0:
                n = int(n/2)
            else:
                n = n*3 + 1
            res += str(n) + " "
        return res


#driver
if __name__ == "__main__":
    n = int(input())
    print(Solution().weirdAlgorithm(n))
