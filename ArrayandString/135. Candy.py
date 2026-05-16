class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        totalcandy = n
        i = 1
        while i < n:
            if ratings[i] == ratings[i - 1]:
                i += 1
                continue
            current_peak = 0
            while i < n and ratings[i] > ratings[i - 1]:
                current_peak += 1
                totalcandy += current_peak
                i += 1
            if i == n:
                return totalcandy

            current_valley = 0
            while i < n and ratings[i] < ratings[i - 1]:
                current_valley += 1
                totalcandy += current_valley
                i += 1
            totalcandy -= min(current_peak, current_valley)
        return totalcandy
