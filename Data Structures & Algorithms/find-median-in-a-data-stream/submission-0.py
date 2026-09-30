import heapq

class MedianFinder:

    def __init__(self):
        self.left = []   # max heap (smaller half)
        self.right = []  # min heap (larger half)

    def addNum(self, num: int) -> None:

        # Put num in left first
        heapq.heappush(self.left, -num)

        # Make sure every left element <= every right element
        if self.left and self.right and -self.left[0] > self.right[0]:
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)

        # Balance sizes
        if len(self.left) > len(self.right) + 1:
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)

        elif len(self.right) > len(self.left):
            val = heapq.heappop(self.right)
            heapq.heappush(self.left, -val)

    def findMedian(self) -> float:

        if len(self.left) > len(self.right):
            return -self.left[0]

        return (-self.left[0] + self.right[0]) / 2