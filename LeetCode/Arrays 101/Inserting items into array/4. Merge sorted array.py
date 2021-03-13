# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        self.nums1 = nums1
        self.m = m
        self.nums2 = nums2
        self.n = n
        self.counter_i = 0
        self.counter_j = 0
        for i in range(len(self.nums1)):
            self.nums1[self.counter_i], self.nums2[self.counter_j] = min(self.nums1[self.counter_i], self.nums2[self.counter_j]), max(self.nums1[self.counter_i], self.nums2[self.counter_j])
