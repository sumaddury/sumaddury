class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return(False)
        left_brackets=[]
        left_dict=("(","{","[")
        switchdict={")":"(","}":"{","]":"["}
        for bracket in s:
            if bracket in left_dict:
                left_brackets.append(bracket)
            elif len(left_brackets)>0:
                if switchdict[bracket]==left_brackets[len(left_brackets)-1]:
                    left_brackets.pop(len(left_brackets)-1)
                else:
                    return(False)
            else:
                return(False)
        if len(left_brackets)==0:
            return(True)
        else:
            return(False)