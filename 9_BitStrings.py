class Solution:
    def bitStrings(self, n):
        return pow(2, n) % (pow(10,9) + 7)

#driver
if __name__ == "__main__":
    n = int(input())
    print(Solution().bitStrings(n))
