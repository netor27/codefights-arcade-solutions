'''
Elections are in progress!

Given an array of the numbers of votes given to each of the candidates so far, and an integer k equal to the number of voters who haven't cast their vote yet, find the number of candidates who still have a chance to win the election.

The winner of the election must secure strictly more votes than any other candidate. If two or more candidates receive the same (maximum) number of votes, assume there is no winner at all.
'''
def electionsWinners(votes, k):
    currentWinner = max(votes)    
    res = 0
    if k > 0:
        # If we have votes left, the ones with the max number of votes can win and also the ones that
        # their votes plus the votes left are greater than the currentWinner
        for i in range(len(votes)):
            if votes[i] + k > currentWinner:
                res += 1    
        return res
    
    else:
    # If we don't have any votes left, we can only have one winner or no winner at all.
    # If 2 or more have the max votes, theres no winner
        aux = 0
        for i in range(len(votes)):
            if votes[i] == currentWinner:
                aux += 1
                if aux > 1:
                    return 0
        return 1