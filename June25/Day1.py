class Solution:
    def findLHS(self, nums):
        store = {}
        maxsum=0
        for num in nums:
            if num not in store:
                store[num]=1
            else:
                store[num]+=1
        for key in store:
            nextkey = key+1
            if nextkey in store:
                crsum =store[key]+store[nextkey]
                if crsum >maxsum:
                    maxsum=crsum
        return maxsum
solution= Solution()
print(solution.findLHS([1,3,2,2,5,2,3,7]))