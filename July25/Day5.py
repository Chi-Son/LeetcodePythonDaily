# 1394.Find Lucky Integer in an Array
class Solution:
    def findLucky(self, arr):
        arr.sort()
        arr.reverse()
        count=1
        for i in range(len(arr)-1):
            if arr[i]==arr[i+1]:
                count+=1
            else:
                if(count==arr[i]):
                    return arr[i]
                count=1
        if count == arr[-1]:
            return arr[-1]
        return -1
ok= Solution()
print(ok.findLucky([2,2,3,4]))