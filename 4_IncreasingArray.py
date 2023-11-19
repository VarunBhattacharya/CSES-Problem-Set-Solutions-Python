
class Solution:
    def increasingArray(self, n, arr):
        minMovesReq = 0
        for i in range(1, n):
            if arr[i] < arr[i-1]:
                minMovesReq += (arr[i-1] - arr[i])
                arr[i] += (arr[i-1] - arr[i])
        return minMovesReq


#driver
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(Solution().increasingArray(n, arr))
