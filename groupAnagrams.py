from collections import defaultdict
class Solution:
    """
    Given an array of strings, group anagrams together.

    For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
     Return:
    [
        ["ate", "eat", "tea"],
        ["nat", "tan"],
        ["bat"]
    ]
    Note: All inputs will be in lower - case.
    """
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = defaultdict(list)
        for s in strs:
            count = [0] * 26 #Occurences of each letter of a given string
            for c in s:
                count[ord(c)-ord('a')] +=1
            anagrams[tuple(count)].append(s)
        return list(anagrams.values())

    def groupAnagrams_sort(self, strs):
       """
       :type strs: List[str]
       :rtype: List[List[str]]
       """
       anagrams = defaultdict(list)
       for s in strs:
           sorted_s = ''.join(sorted(s))
           anagrams[sorted_s].append(s)
       return list(anagrams.values())

sol = Solution()
print (sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
sol = Solution()
print (sol.groupAnagrams_sort(["eat", "tea", "tan", "ate", "nat", "bat"]))