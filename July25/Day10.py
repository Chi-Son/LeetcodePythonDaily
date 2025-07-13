# 2410. Maximum Matching of Players With Trainers
class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        players.sort(reverse=True)
        trainers.sort(reverse=True)
        i,j=0
        count=0
        while i<len(players) and j<len(trainers):
            if(players[i]<=trainers[j]):
                count+=1
                j+=1
            i+=1 
        return count 