# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        L=0
        R=n
        while L <= R:
            mid = (L+R ) // 2
            if guess(mid) == 0: # problem statement says that 0 means I guessed the answer
                return mid
            elif guess(mid) < 0: # -1 means number my guess is higher than target 
                R=mid-1 # so, lower right pointer by moving it to mid -1 
            else:
                L=mid+1
            
            
        
        