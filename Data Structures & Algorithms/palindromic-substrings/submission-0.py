class Solution:
    def countSubstrings(self, s: str) -> int:
        # number of palindromic substrings 
        # can proceed with the idea that each number could hypothetically 
        # be the center of a palindrome

        # for odd numbers this works, for even u need to check 2 centers
        # a single character is also a palindrome
        count = 0
        #checking odd 
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

        print(count)

        for i in range(len(s)-1):
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

        




        return count



