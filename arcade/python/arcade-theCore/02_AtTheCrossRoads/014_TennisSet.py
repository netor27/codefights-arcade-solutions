def tennisSet(score1, score2):
    '''
In tennis, a set is finished when one of the players wins 6 games and the other one wins less than 5, or, if both players win at least 5 games, until one of the players wins 7 games.

Determine if it is possible for a tennis set to be finished with the score score1 : score2.
    '''
    winner = max(score1, score2)
    loser = min(score1, score2)
    
    return (winner == 6 and loser < 5) or (winner == 7 and 5 <= loser <= 6)

print(tennisSet(3, 6))
print(tennisSet(8, 5))