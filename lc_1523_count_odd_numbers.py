# LeetCode 1523: Count odd numbers in an interval

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = (high+1)//2 - (low//2)

        return count