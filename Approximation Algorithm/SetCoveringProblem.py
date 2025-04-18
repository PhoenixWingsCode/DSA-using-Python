def set_cover(universe, subsets):
    """
    Greedy algorithm to solve the Set Covering Problem.
    
    Parameters:
    universe (set): The set of all elements that need to be covered.
    subsets (list of sets): A list of subsets of the universe.
    
    Returns:
    list of sets: A list of subsets that together cover the universe.
    """
    covered = set()
    cover = []
    
    while covered != universe:
        subset = max(subsets, key=lambda s: len(s - covered))
        cover.append(subset)
        covered |= subset
    
    return cover

# Example usage
universe = {1, 2, 3, 4, 5}
subsets = [{1, 2, 3}, {2, 4}, {3, 4}, {4, 5}, {5}]
solution = set_cover(universe, subsets)

print("Selected subsets for covering the universe:")
for s in solution:
    print(s)