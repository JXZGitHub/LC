# Complete the function below.
# votes is a list of strs representing names receiving votes, return the winner (if there's a tie, the alphebetically last person wins).
from collections import Counter
def electionWinner(votes):
    tally = Counter(votes)
    ties = tally.most_common()
    names = []
    max_votes = float('-inf')
    for (n, c) in ties:
        if c >= max_votes:
            max_votes = c
            names.append(n)
        else:
            break

    return sorted(names)[-1]

