def merge_meetings(meetings):

    # Sort Intervals by Start Time
    meetings.sort()

    # Initialize result with first meeting
    result = [meetings[0]]

    for currStart, currEnd in meetings[1:]:
        prevStart, prevEnd = result[-1]

        # If the current meeting overlaps with the last merged meeting
        # Use the later end time of the two (Overlap)
        # If the current start time is within the last meeting end time
        if (currStart <= prevEnd):
            result[-1] = (prevStart, max(prevEnd, currEnd))

        # No Overlap
        else:
            result.append(currStart, currEnd)

    return result


# Complexity
# O(nlogn) time
# Sorting the meetings takes up nlogn time, if the meetings were already sorted, this would be O(n) time
# O(n) space - worst case scenario, none of the meetings merge and a new list the same size as the input is created

# Greedy approach - builds up a solution by choosing the option that looks the best
