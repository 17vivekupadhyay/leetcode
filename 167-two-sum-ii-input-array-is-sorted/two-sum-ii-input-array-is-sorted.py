class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        front = 0
        back = len(numbers) - 1
        
        while front <= back:
            compare = numbers[front] + numbers[back]

            if  compare == target:
                return [front +1, back+1]

            if compare > target:
                back -= 1
            else:
                front += 1

        return [0,0]


        