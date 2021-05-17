def sort_scores(unsorted_scores, highest_possible_score):

    scoreCounts = [0] * (highest_possible_score + 1)

    for score in unsorted_scores:
        scoreCounts[score] += 1

    sortedScore = []

    for score in range(len(scoreCounts) - 1, -1, -1):
        count = scoreCounts[score]

        for time in range(count):
            sortedScore.append(score)

    return sortedScore

# Create a list of potential scores
# Add all the scores to the list of potential scores with the count of the score
# Create a new list based off the score and the count of the score in reverse range

# O(n) time
# O(n) space
