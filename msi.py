# Author   : Martin Užák <uzak+git@mailbox.org>
# Creation : 2024-03-11 09:47

"""
Given a list of numbers as input, return a tuple of the sum of all the
positive numbers as the first element. Second element is the count of the
negative numbers in the list.

If the input array is empty, return an empty array.
"""

numbers = [1,-2, 3, 5, 6, -1, 0]

def evalute(numbers):
    """Return a tuple of (pos_sum, neg_count) or
    return [] if `numbers` is empty"""
    if not numbers:
        return []

    pos_sum = 0
    neg_count = 0
    for number in numbers:
        if number > 0:
            pos_sum += number
        elif number < 0:
            neg_count += 1
    return (pos_sum, neg_count)


print(evalute(numbers))
print(evalute([]))
