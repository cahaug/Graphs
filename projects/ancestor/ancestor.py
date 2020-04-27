
def earliest_ancestor(ancestors, starting_node):
    oldest_ancestor = -1
    relatives = {}
    for parent_child_pair in ancestors:
        if parent_child_pair[1] == starting_node:
            if parent_child_pair[0] > oldest_ancestor:
                oldest_ancestor = parent_child_pair[0]
            relatives[parent_child_pair[0]] = parent_child_pair[1]
    for parent_child_pair in ancestors:
        if parent_child_pair[1] in relatives.keys():
            if parent_child_pair[0] > oldest_ancestor:
                oldest_ancestor = parent_child_pair[0]
            relatives[parent_child_pair[0]] = parent_child_pair[1]
    if len(relatives) > 0:
        oldest_ancestor = list(relatives.keys())[-1]
    print(relatives)
    

    return oldest_ancestor