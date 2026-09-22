class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


        hashmap = {}
        maxfre = 0
        bestWin = 0
        l = 0
        for i in range(len(s)):
            # add the character frequency to the hashmap
            hashmap[s[i]] = 1 + hashmap.get(s[i], 0)
            maxfre = max(maxfre, hashmap[s[i]])

            while(i-l + 1) - maxfre > k:
                hashmap[s[l]] -= 1
                l+=1
            bestWin = max(bestWin, i-l + 1)
        return bestWin

        
        


        