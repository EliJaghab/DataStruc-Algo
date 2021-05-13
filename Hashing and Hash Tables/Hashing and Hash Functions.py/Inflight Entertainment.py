def twoMoviesForFlight(movieLengths, flightLength):
    seenMovies = set()

    for firstMovie in movieLengths:
        secondMovie = flightLength - firstMovie
        # If complement not in set, add firstMovie
        if secondMovie in seenMovies:
            return True
        seenMovies.add(firstMovie)

    return False


# O(n) time
# O(n) space
