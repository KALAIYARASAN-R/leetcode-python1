class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        else:
            division = dividend/divisor
            if division > 0:
                return floor(division)
            return ceil(division)



#this is understanding purpose
#In Python, ceil is a mathematical function provided by the math module, which stands for ceiling. The ceiling of a number is the smallest integer greater than or equal to that number.

#For example:

#The ceiling of 2.3 is 3.
#The ceiling of 3.9 is 4.
        