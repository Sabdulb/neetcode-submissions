class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        if nums:
            self.nums = nums
        else:
            self.nums = []
        self.nums.sort()
        self.nums.reverse()

    def add(self, val: int) -> int:
        i = 0
        while i < len(self.nums):
            if val >= self.nums[i]:
                break
            else:
                i += 1
        self.nums.insert(i, val)
        print(self.nums)
        return self.nums[self.k - 1]