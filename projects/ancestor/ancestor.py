class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

# bft search with queue from lecture

def earliest_ancestor(ancestors, starting_node):
    # declare the earliest potential ancestor variable
    oldest_ancestor = -1
    # create a dictionary to hold lookups dictionary
    relationships = {}
    # for each parent child relationship in ancestors:
    for pc_pair in ancestors:
        # if the child is not in our lookup dictionary
        if pc_pair[1] not in relationships:
            # add it as a set for better performance
            relationships[pc_pair[1]] = set()
            relationships[pc_pair[1]].add(pc_pair[0])
        # if a child exists
        else:
            # add it to our dict
            relationships[pc_pair[1]].add(pc_pair[0])
    # queue to track our progress through the bft
    plan_to_visit = Queue()
    # enqueue the starting_node
    plan_to_visit.enqueue(starting_node)
    # get the neighbors and rerun this function
    while plan_to_visit.size() > 0:
        # if there's something in the queue, run it
        current_node = plan_to_visit.dequeue()
        # if it is a child
        if current_node in relationships:
            # get the parents
            parents = relationships[current_node]
            # if the parent is a child, enqueue the parents
            for parent in parents:
                plan_to_visit.enqueue(parent)
        # no parents found, input is earliest ancestor
        else:
            # if we have visited any other nodes, return the one we are looking at last
            if current_node != starting_node:
                oldest_ancestor = current_node
    return oldest_ancestor