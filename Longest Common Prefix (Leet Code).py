class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=""
        continuation_bool=True
        prefix_len=1
        while continuation_bool:
            prefix=(strs[0])[0:prefix_len]
            for string in strs:
                if len(string)>=prefix_len:
                    if string[0:prefix_len]==prefix:
                        pass
                    else:
                        continuation_bool=False
                        prefix=(strs[0])[0:prefix_len-1]
                        break
                else:
                    continuation_bool=False
                    prefix=(strs[0])[0:prefix_len-1]
                    break
            prefix_len+=1
        return(prefix)