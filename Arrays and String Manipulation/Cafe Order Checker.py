def firstComeFirstServed(takeOut, dineIn, servedOrders):
    takeOutInd = dineInInd = 0
    takeOutLength = len(takeOut) - 1
    dineInLength = len(dineIn) - 1

    for i in servedOrders:
        if takeOutInd <= takeOutLength and i == takeOut[takeOutInd]:
            takeOutInd += 1
        elif dineInInd <= dineInLength and i == dineIn[dineInInd]:
            dineInInd += 1
        else:
            return False

    # Check for Extra Orders at the End of the List
    if dineInInd != len(dineIn) or takeOutInd != len(takeOutInd):
        return False

    return True


# O(n) time
# O(1) space
