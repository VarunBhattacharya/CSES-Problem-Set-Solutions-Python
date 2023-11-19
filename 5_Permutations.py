class Solution:
    def permutations(self, n):
        res = ""
        if n == 1:
            res = str(1)
        elif n <= 3:
            res = "NO SOLUTION"
        else:
            for i in range(2, n+1, 2):
                res += str(i) + " "
            for i in range(1, n+1, 2):
                res += str(i) + " "
        return res


#driver
if __name__ == "__main__":
    n = int(input())
    print(Solution().permutations(n))
