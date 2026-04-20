class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] + 1 != 10:
                digits[i] += 1
                return digits
            digits[i] = 0
            if i == 0:
                return [1] + digits
if __name__ == '__main__':
    nums = [1,2,3]
    solution = Solution()
    print(solution.plusOne(nums))
    nums = [4,3,2,1]
    solution = Solution()
    print(solution.plusOne(nums))