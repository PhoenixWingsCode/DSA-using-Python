class climbStairs:
    def climbStrairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one

cs = climbStairs()
result = cs.climbStrairs(5)
print("Number of ways to climb 5 stairs is : ", result)