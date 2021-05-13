# Hash Function
#       takes data and outputs a hash, fixed-size string or number

# Hash Collision
#       multiple files having the same hash value

# Dictionaries
#       list-like data structure with constant-time lookups
#       look up values based on keys, not just indices

# Hash Table or Dictionary
# Strengths:
# Fast Lookups - O(1) time on average
# Flexible Keys - most data types can be used as keys

# Weaknesses:
# Slow Worst-Case Lookups - O(n) for worst case
# Keys are unordered
# Single Directional Lookups - Looking up the value for a key takes O(1) time
#           But looking up the key for a value takes O(n)

# Python Dictionary
light_bulb_to_hours_of_light = {
    'incandescent': 1200,
    'compact fluorescent': 10000,
    'LED': 50000,
}


# Sets
# Set is like a hashmap except it only stores keys, without values

light_bulbs = set()

light_bulbs.add('incandescent')
light_bulbs.add('compact fluorescent')
light_bulbs.add('LED')

'LED' in light_bulbs  # True
'halogen' in light_bulbs  # False
