class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        stops = {}
        cur = 0
        for val in trips:
            latest_stop = val[1]
            end_stop = val[2]
            new_people = val[0]
            stops_tmp = [x for x in stops if x <= latest_stop]
            for stop in stops_tmp:
                cur -= stops[stop]
                stops.pop(stop, None)

            cur += new_people
            stops[end_stop] = stops.get(end_stop, 0) + new_people
            if cur > capacity:
                return False

        return True
            
