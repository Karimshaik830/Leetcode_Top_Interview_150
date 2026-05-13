import random

class RandomizedSet:
    def __init__(self):
        self.val_to_index = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        self.nums.append(val)
        self.val_to_index[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False
        idx = self.val_to_index.pop(val)
        last_val = self.nums[-1]

        # Swap only if val is not the last element
        if idx != len(self.nums) - 1:
            self.nums[idx] = last_val
            self.val_to_index[last_val] = idx

        self.nums.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)