class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', s)
        cleaned_text = cleaned_text.lower()
        print(cleaned_text)
        return cleaned_text == cleaned_text[::-1]