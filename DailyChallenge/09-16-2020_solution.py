class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_len = len(format(max(nums), 'b'))
        bin_list = [format(i, '0'+str(max_len)+'b') for i in nums]
        ans = float('-inf')

        trie = {}
        for bin_num in bin_list:
            parent = trie
            for i in bin_num:
                parent[i] = parent.get(i, {})
                parent = parent[i]

        ans = 0
        for bin_num in bin_list:
            parent = trie
            potential_bin = ''
            for x in bin_num:
                to_find = '1' if x == '0' else '0'
                if to_find in parent:
                    potential_bin += to_find
                    parent = parent[to_find]
                else:
                    potential_bin += x
                    parent = parent[x]

            ans = max(ans, int(bin_num, 2) ^ int(potential_bin, 2) )
        return ans

        
