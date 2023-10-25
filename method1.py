# write a function that return the number of "1" bits in a given string
class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n:
            result += n % 2  # increment if mod = 1, no increment if mod = 0
            n = n >> 1  # shifting bit to the right by 1
        return result
