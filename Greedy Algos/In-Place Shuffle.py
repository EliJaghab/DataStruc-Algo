# Fisher-Yates Algorithm

import random


def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)


def shuffle(the_list):
    lastInd = len(the_list) - 1
    while lastInd > 0:
        randInd = get_random(0, lastInd)
        temp = the_list[lastInd]
        the_list[lastInd] = the_list[randInd]
        the_list[randInd] = temp
        lastInd -= 1

# O(n) time
# O(1) space


sample_list = [1, 2, 3, 4, 5]
print('Sample list:', sample_list)

print('Shuffling sample list...')
shuffle(sample_list)
print(sample_list)
