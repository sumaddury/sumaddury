class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_string=str(x)
        len_x=len(x_string)
        if len_x % 2 == 0:
            median=int(len_x/2)
            if x_string[0:median]==(x_string[median:len_x])[::-1]:
                return(True)
            else:
                return(False)
        else:
            median=int(((len_x+1)/2)-1)
            if x_string[0:median]==(x_string[median+1:len_x])[::-1]:
                return(True)
            else:
                return(False)