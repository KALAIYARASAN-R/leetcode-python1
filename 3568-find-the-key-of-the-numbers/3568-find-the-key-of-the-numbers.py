class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        s1 = f"{num1:04}"
        s2 = f"{num2:04}"
        s3 = f"{num3:04}"
        rs = 0
        for i in range (4):
            n1 = int(s1[i])
            n2 = int(s2[i])
            n3 = int(s3[i])
            rs = rs * 10 + min(n1, n2, n3)
        return rs
        