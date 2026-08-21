class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def time(k):
            day = 1
            load = 0
            for w in weights:
                if load + w > k:
                    day += 1
                    load = w
                else:
                    load += w
            return day
        
        front = max(weights)
        back = sum(weights)

        while front < back:
            mid = (front + back) // 2
            
            if time(mid) <= days:
                back = mid
            else:
                front = mid + 1

        return front
            