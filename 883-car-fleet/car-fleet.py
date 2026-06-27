class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = reversed(sorted(zip(position, speed)))
        stack = []
        fleet = 1

        for car in cars:
            t = (target - car[0]) / car[1]
            if not stack or t > stack[-1]:
                stack.append(t)

        return len(stack)

