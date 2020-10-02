class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = [set() for _ in range(target + 1)]
        res[0].add(())
        for num in candidates:
            for off in range(0, target - num + 1):
                print("off: {}".format(off))
                for seq in res[off]:
                    res[num + off].add(seq + (num,))
        return res[target]
