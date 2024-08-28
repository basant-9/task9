def score (rounds):
    scoreboard = {}
    for player, score in rounds:
        scoreboard[player] = scoreboard.get(player,0) + score
    return scoreboard
rounds = [(1, 10), (2, 15), (3, -5), (1, 20), (2, -10),(1, 5), (2, 10), (1, 15)]
print(score(rounds))