class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap = {}
        if len(s) != len(t):
            return False
            
        for letter in s:
            if letter in hashMap:
                hashMap[letter] += 1
            else:
                hashMap[letter] = 1

        for letter in t:
            if letter in hashMap:
                if hashMap[letter] == 0:
                    return False
                hashMap[letter] -= 1
            else:
                return False

        return True 