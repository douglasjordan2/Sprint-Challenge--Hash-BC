#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (
    HashTable,
    hash_table_insert,
    hash_table_remove,
    hash_table_retrieve,
    hash_table_resize
)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    Answer = (None, None)

    # add weights to hash table where key = weight and value = index
    for i in range(length):
        hash_table_insert(ht, weights[i], i)

    # loop through values
    for val in range(length):
        # the first value is the current index in the for loop. we try to find the other value by searching the hash table for a value equal to the limit minus the first value
        other_val = hash_table_retrieve(ht, (limit - weights[val]))

        # if the other value exists in the hash table, then we've found both values
        if other_val is not None:
            # this condition checks which value is greater and sets the larger value as the first item in the answer
            if other_val > val:
                Answer = (other_val, val)
            else:
                Answer = (val, other_val)

            # both values are found, and the answer is returned
            return Answer

    # if none of the 2 weight values' sums equal the limit, the first condition is never met. the for loop ends, and we return None
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
