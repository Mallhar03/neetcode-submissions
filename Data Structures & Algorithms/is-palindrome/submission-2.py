class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = re.sub(r"[^a-zA-Z0-9]","",s)
        cleaned = cleaned.lower()
        right = len(cleaned) - 1
        left = 0
        while (left <= right):
            if cleaned[left] == cleaned[right]:
                left += 1
                right -= 1
            else : return False
        return True        