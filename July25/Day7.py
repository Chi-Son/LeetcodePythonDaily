import heapq
# 1353. Maximum Number of Events That Can Be Attended
# Sort Endday , x2 for TLE
class Solution(object):
    def maxEvents(self, events):
        events.sort(key=lambda x:x[1])
        schedule=set()
        for start,end in events:
            for a in range(start,end+1):
                if a not in schedule:
                    schedule.add(a)
                    break
        return len(schedule)
# Sort Startday 
    def maxEvents(self, events):
        events.sort()
        total, i, n = 0, 0, len(events)
        heap = []

        day = 1
        while i < n or heap:
            while i < n and events[i][0] == day:
                heapq.heappush(heap, events[i][1])  
                i += 1
            while heap and heap[0] < day:
                heapq.heappop(heap)
            if heap:
                heapq.heappop(heap)
                total += 1
            day += 1
        return total