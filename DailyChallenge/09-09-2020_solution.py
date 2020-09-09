class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(x) for x in version1.split('.')]
        v2 = [int(x) for x in version2.split('.')]

        # If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.
        small_len = min(len(v1), len(v2))
        for i in range(small_len):
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1

        if len(v1) == len(v2):
            return 0

        if len(v1) < len(v2):
            if [x for x in v2[small_len:] if x > 0]:
                return -1
            else:
                return 0
        else:
            if [x for x in v1[small_len:] if x > 0]:
                return 1
            else:
                return 0
