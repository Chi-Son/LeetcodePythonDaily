# 3439. Reschedule Meetings for Maximum Free Time I
class Solution:
    def maxFreeTime(self, eventTime, k, startTime, endTime):
        n=len(startTime)
        store=[0]*(n+1)
        for i in range(n):
            store[i+1]=store[i]+endTime[i+1]-startTime[i+1]
        for i in range(k-1,n):
            right= eventTime if i>=n else right=startTime[i+1]
            left =0 if i==k-1 else left= endTime[i-1]
            res= max(res,right -left-(store[i+1]-store[i-k+1]))
        return res