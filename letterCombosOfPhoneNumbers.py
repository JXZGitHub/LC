class Solution:
    """
    Given a digit string, return all possible letter combinations that the number could represent.
    2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"

    Input:Digit string "23"
    Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

    Order between each combination does not matter.
    """
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = []

        mapping = ['', '', "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        self.rowRecurse(mapping, digits, 0, '', result)
        return result

    def rowRecurse(self, mapping, digits, level, currCombo, result):
        if level == len(digits):
            result.append(currCombo)
        else:
            letters = mapping[int(digits[level])]
            for l in letters:
                self.rowRecurse(mapping, digits, level + 1, currCombo + l, result)