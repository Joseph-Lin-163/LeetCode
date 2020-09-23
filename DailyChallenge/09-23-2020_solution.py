class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
#         len_trip = len(gas)
#         potential_starts = [idx for idx,val in enumerate(zip(gas, cost)) if val[0] >= val[1]]
#         # potential_starts = [i for i in range(len_trip) if gas[i] >= cost[i]]

#         gas_tank = 0

#         invalid_starts = []
#         for i in potential_starts:
#             if i in invalid_starts:
#                 continue
#             trip_idx = i
#             gas_i = i + 1
#             gas_tank = gas[i]
#             seen = []
#             for stops in range(len_trip):
#                 if i == len_trip:
#                     i = 0
#                 if gas_i == len_trip:
#                     gas_i = 0

#                 if i in potential_starts:
#                     seen.append(i)

#                 if gas_tank < cost[i]:
#                     break
#                 gas_tank = gas_tank - cost[i] + gas[gas_i]
#                 i += 1
#                 gas_i += 1
#             if i == len_trip:
#                 i = 0

#             if gas_tank < cost[i]:
#                 invalid_starts.extend(seen)
#                 continue
#             else:
#                 return trip_idx

#         return -1
#         len_trip = len(gas)
#         # gas = [gas[i] - cost[i] for i in range(len_trip)]
#         gas = [x - y for x, y in zip(gas, cost)]
#         if sum(gas) < 0:
#             return -1
#         potential_starts = [i for i in range(len_trip) if gas[i] >= 0]
#         invalid_starts = []
#         for start in potential_starts:
#             if start in invalid_starts:
#                 continue
#             trip_idx = start
#             gas_tank = 0

#             seen = []
#             for stop in range(len_trip):
#                 if start == len_trip:
#                     start = 0
#                 if start in potential_starts:
#                     seen.append(start)

#                 gas_tank += gas[start]
#                 if gas_tank < 0:
#                     break
#                 start += 1

#             if gas_tank < 0:
#                 invalid_starts.extend(seen)
#                 continue
#             else:
#                 return trip_idx

#         return -1

        # The idea is to get the largest "dip" in gas
        # and subsequently, the next stop would have to be very big, otherwise we can't overcome
        # the negative and then the algorithm would stop there.
        # So, we can safely assume that the next stop would have enough gas to
        # let the algorithm keep running
        # therefore we return r + 1 % len(gas)
        # of course, if summation of gas - cost < 0, return -1
        lowest = float('inf')
        net = 0
        for i in range(len(gas)):
            net += gas[i]-cost[i]
            if net < lowest:
                r,lowest = i, net

        return (r+1)%len(gas) if net >= 0 else -1
