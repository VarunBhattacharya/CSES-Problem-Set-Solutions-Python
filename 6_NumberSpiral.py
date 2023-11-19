class Solution:
    def numberSpiral(self, y, z):
        #diagonal position i.e.. y == z
        if y == z:
            return (y*y - (y-1))
        #row position is greater than column position i.e.. y > z
        elif y > z:
            if y%2 != 0:
                return (y*y - (y-1)) - (y-z)
            else:
                return (y*y - (y-1)) + (y-z)
        #col postion is greater than row position i.e.. z > y
        elif z > y:
            if z%2 != 0:
                return (z*z - (z-1)) + (z - y)
            else:
                return (z*z - (z-1)) - (z - y)
        return -1


#driver
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        y, z = list(map(int, input().split()))
        print(Solution().numberSpiral(y, z))
