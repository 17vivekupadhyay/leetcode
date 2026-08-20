class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def time(k):
            x = 0
            for p in piles:
                x += ceil(p/k)
            return x

        front = 1
        back = max(piles)

        while front < back:
            mid = (front + back) // 2
            if time(mid) <= h:
                back = mid
            else:
                front = mid + 1
        return front