# 1353. Maximum Number of Events That Can Be Attended
# Sort Endday , x2 for
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