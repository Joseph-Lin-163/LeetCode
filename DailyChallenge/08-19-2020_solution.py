class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowels = set('aeiouAEIOU')
        # goat = []
        # for idx, data in enumerate(S.split(), start=1):
        #     if data[0] not in vowels:
        #         goat.append(data[1:] + data[0] + "ma" + "a" * idx)
        #     else:
        #         goat.append(data + "ma" + "a" * idx)
        
        # goat = [data[1:] + data[0] + "ma" + "a" * idx if data[0] not in vowels else data + "ma" + "a" * idx for idx, data in enumerate(S.split(), start=1) ]
        
        # return " ".join(goat)
        
        return " ".join([data[1:] + data[0] + "ma" + "a" * idx if data[0] not in vowels else data + "ma" + "a" * idx for idx, data in enumerate(S.split(), start=1) ])
                
