class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        for i in range(1, 11):
            if 10**i > low:
                low_digits = i
                break
        for i in range(1,11):
            if 10**i > high:
                high_digits = i
                break

        def list_of_nums(digit_count, low_num=None, high_num=None):
            start = [1] + [0]*(digit_count - 1)
            for i in range(1,digit_count):
                start[i] = start[i-1] + 1
                if start[i] >= 10:
                    return []
            start = int(''.join([str(x) for x in start]))
            adder = int(''.join(['1']*digit_count))
            limit = [0]*(digit_count - 1) + [9]
            for i in range(digit_count-2,-1,-1):
                limit[i] = limit[i+1] - 1
            limit = int(''.join([str(x) for x in limit]))
            num_list = []
            if low_num != None:
                while start < low_num:
                    start += adder
                    if start > limit:
                        return []
                num_list.append(start)
                while True:
                    start += adder
                    if start > limit:
                        return num_list
                    else:
                        num_list.append(start)
            elif high_num != None:
                if start > high_num:
                    return []
                num_list.append(start)
                while True:
                    start += adder
                    if start > high_num or start > limit:
                        return num_list
                    else:
                        num_list.append(start)
            else:
                num_list.append(start)
                while True:
                    start += adder
                    if start > limit:
                        return num_list
                    else:
                        num_list.append(start)
        # get the nums
        low_num_list = list_of_nums(low_digits, low_num=low)
        high_num_list = list_of_nums(high_digits, high_num=high)
        if low_digits == high_digits:
            low_num_list = [x for x in low_num_list if x < high]
            high_num_list = [x for x in high_num_list if x > low]
            low_num_list.extend([x for x in high_num_list if x not in low_num_list])
            return low_num_list
        else:
            other_digit_list = []
            for i in range(low_digits+1, high_digits):
                other_digit_list.extend(list_of_nums(i))
            return low_num_list + other_digit_list + high_num_list
