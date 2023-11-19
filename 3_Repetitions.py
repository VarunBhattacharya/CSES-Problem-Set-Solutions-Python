
class Solution:
    def repetitions(self, s):
        pnt1, pnt2 = 0, 1
        maxLen = 1
        curLen = 1
        while (pnt1 < pnt2) and (pnt2 < len(s)):
            if s[pnt1] == s[pnt2]:
                curLen += 1
                pnt2 += 1
            else:
                curLen = 1
                pnt1 = pnt2
                pnt2 += 1
            maxLen = max(maxLen, curLen)
        return maxLen


#driver
if __name__ == "__main__":
    s = input()
    print(Solution().repetitions(s))
