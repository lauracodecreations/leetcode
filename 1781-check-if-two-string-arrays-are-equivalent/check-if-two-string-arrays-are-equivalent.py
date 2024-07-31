class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        i = j = 0
        word1_total = "".join(word1)
        word2_total = "".join(word2)
        
        if word1_total == word2_total:
            return True
        else:
            return False

            
        