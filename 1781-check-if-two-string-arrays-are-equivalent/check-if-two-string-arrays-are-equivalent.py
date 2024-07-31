class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
  
        s1 = s2 = 0
        c1 = c2 = 0
        
        while True:
            char1 = word1[s1][c1]
            char2 = word2[s2][c2]
            
            if char1 != char2:
                return False
            
            c1+=1
            c2+=1
            
            # we have reached last character of the string element
            # so move to the next string element,
            # and start the count for the c pointer at 0
            if c1 == len(word1[s1]):
                s1 +=1
                c1 = 0
                
            if c2 == len(word2[s2]):
                s2 +=1
                c2 = 0
                
            # we have reached the end of both arrays
            if s1 == len(word1) and s2 == len(word2):
                return True
            elif s1 == len(word1) or s2 == len(word2):
                # there was an extra character if
                # only the end of one array was reached
                return False
            
                
        
    # T: O(n) 
    # S: O(1)
        
            
            
            
        