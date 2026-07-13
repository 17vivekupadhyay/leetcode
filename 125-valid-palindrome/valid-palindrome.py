class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = "".join(char for char in s if char.isalnum()).lower()
        front = 0
        back = len(text)-1
        while front <= back:
            if text[front] != text[back]:
                return False
            else:
                front +=1
                back -= 1
        return True
            
        