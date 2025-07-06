# 1865. Finding Pairs With a Certain Sum

class FindSumPairs(object):

    def __init__(self, nums1, nums2):
        self.nums1= nums1
        self.nums2=nums2 
        self.store={}
        for i in nums2:
            if i in self.store:
                self.store[i]+=1
            else:
                self.store[i]=1

    def add(self, index, val):
        oldva= self.nums2[index]
        newva=oldva+val
        self.store[oldva]-=1
        if newva in self.store:
            self.store[newva]+=1
        else:
            self.store[newva]=1
        self.nums2[index]=newva
        

    def count(self, tot):
        count = 0
        for num1 in self.nums1:
            ans= tot-num1
            if ans in self.store:
                count+=self.store[ans]
        return count
        