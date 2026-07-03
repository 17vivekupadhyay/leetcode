class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        front = 1
        back = max(piles)
        result = back

        while front <= back:
            mid = (front + back) // 2
            hours = sum((p + mid - 1) // mid for p in piles)

            if hours <= h:
                result = mid
                back = mid - 1
            else:
                front = mid + 1

        return result
        