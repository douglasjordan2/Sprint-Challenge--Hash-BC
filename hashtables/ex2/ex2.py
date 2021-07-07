#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (
    HashTable,
    hash_table_insert,
    hash_table_remove,
    hash_table_retrieve,
    hash_table_resize
)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ht = HashTable(length)
    route = [None] * length

    # add each ticket to the hash table where key = starting location and value = destination
    for t in tickets:
        hash_table_insert(ht, t.source, t.destination)

    # begin at the first flight (first flight's starting location is None)
    current_flight = "NONE"

    # loop through the amount of flights we have
    for flight in range(length):
        # beginning with None (current_flight, our first flight), we retrieve the destination value of the starting location key in the hash table. we then set the destination in the proper place in the route
        route[flight] = hash_table_retrieve(ht, current_flight)

        # next we reset the current_flight value to the destination we just found. the destination becomes the new starting location, and the loop progresses by linking the starting location to its destination, and the destination to its next destination, and so on. 
        current_flight = route[flight]

    # since the indices of the for loop correspond to the starting location key in the hash table, the route should populate in the proper order simply by retreiving the proper destination from the hash table. then we just return the route
    return route
