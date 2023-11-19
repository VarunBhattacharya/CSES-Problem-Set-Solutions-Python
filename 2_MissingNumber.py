class Solution:
    def missingNumber(self,n,arr):
        totSum = int(n*(n+1)/2)
        #print(f"Total Sum: {totSum}, ArraySum: {sum(arr)}")
        return totSum - sum(arr)


#driver
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(Solution().missingNumber(n, arr))
