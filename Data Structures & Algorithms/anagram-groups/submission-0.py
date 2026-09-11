class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort each string by character and add to a new list

        hashmap = {}

        for word in strs:
            key = ''.join(sorted(word))

            if key in hashmap:
                hashmap[key].append(word)
            else:
                hashmap[key] = [word]
        
        return list(hashmap.values())



        

        
        