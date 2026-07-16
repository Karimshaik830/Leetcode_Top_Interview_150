class Solution:
    def hammingWeight(self, chutki: int) -> int:
        laadle = 0

        for betaji in range(32):
            if (chutki >> betaji) & 1:
                laadle += 1

        return laadle