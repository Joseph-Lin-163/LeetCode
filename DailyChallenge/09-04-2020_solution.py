class Solution:
    # def get_segments_of_alpha(self, s):
    #     # Returns dict of a-z with value being first and last index where letter shows up
    #     # alpha = 'abcdefghijklmnopqrstuvwxyz'
    #     # return {alpha[idx]: val for idx, val in enumerate(zip(self.get_indexes_of_alpha(s), \
    #     #     [len(s) - x - 1 for x in self.get_indexes_of_alpha(s[::-1])])) if val[0] != -1}
    #     return [val for val in zip(self.get_indexes_of_alpha(s), \
    #         [len(s) - x - 1 for x in self.get_indexes_of_alpha(s[::-1])]) if val[0] != -1]
    #     # return d

    def get_indexes_of_alpha(self, s):
        # Returns list of a-z with first index of letter
        # -1 if letter not exists
        return [s.find(char) for char in 'abcdefghijklmnopqrstuvwxyz']

    def partitionLabels(self, S: str) -> List[int]:
#         # Get the maximum number of non-overlapping letters
#         # segments = self.get_segments_of_alpha(S)
#         segments = sorted(self.get_segments_of_alpha(S), key=lambda x: x[1])
#         # print(segments)

#         mark = 0
#         # Find the smallest end s.t. have end >= tuple[1] xor end <= all tuple[0]
#         # ...then set new starting point to end_idx + 1 of that letter, repeat
#         part_lengths = []
#         for i in range(len(S)):
#             if any([x[0] >= mark and x[0] <= i and x[1] > i for x in segments]):
#                 continue
#             part_lengths.append((i-mark)+1)
#             mark = i+1
#         return part_lengths
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        last_idxs = self.get_indexes_of_alpha(S[::-1])
        last_idxs = {alpha[i]: len(S) - last_idxs[i] - 1 for i in range(26) if last_idxs[i] != -1}
        print(last_idxs)

        start = 0
        end = 0
        part_lengths = []
        for i in range(len(S)):
            end = max(end, last_idxs[S[i]])
            if i == end:
                part_lengths.append((i-start) + 1)
                start = i+1

        return part_lengths
