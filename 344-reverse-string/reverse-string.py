class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        p1 = 0
        p2 = len(s) - 1
        middle = len(s) // 2
        
        while p1 < middle:
            temp_end = s[p2]
            temp_frond = s[p1]
            s[p1] = temp_end
            s[p2] = temp_frond
            p1+=1
            p2-=1
        return s