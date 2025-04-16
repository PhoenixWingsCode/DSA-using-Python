class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight

def bound(node, n, W, items):
    if node.weight >= W:
        return 0
    profit_bound = node.profit
    j = node.level + 1
    totweight = node.weight

    while j < n and totweight + items[j].weight <= W:
        totweight += items[j].weight
        profit_bound += items[j].value
        j += 1

    if j < n:
        profit_bound += (W - totweight) * items[j].ratio

    return profit_bound

class Node:
    def __init__(self, level, profit, weight, bound):
        self.level = level
        self.profit = profit
        self.weight = weight
        self.bound = bound

def knapsack_branch_and_bound(W, items):
    items.sort(key=lambda x: x.ratio, reverse=True)
    Q = []
    u = Node(-1, 0, 0, 0)
    v = Node(0, 0, 0, 0)
    maxProfit = 0
    u.bound = bound(u, len(items), W, items)
    Q.append(u)

    while Q:
        u = Q.pop(0)
        if u.level == -1:
            v.level = 0
        if u.level == len(items) - 1:
            continue
        v.level = u.level + 1
        v.weight = u.weight + items[v.level].weight
        v.profit = u.profit + items[v.level].value

        if v.weight <= W and v.profit > maxProfit:
            maxProfit = v.profit

        v.bound = bound(v, len(items), W, items)

        if v.bound > maxProfit:
            Q.append(v)

        v = Node(v.level, u.profit, u.weight, 0)
        v.bound = bound(v, len(items), W, items)

        if v.bound > maxProfit:
            Q.append(v)

    return maxProfit

# Example usage
items = [Item(10, 60), Item(20, 100), Item(30, 120)]
W = 50
print("Maximum profit is:", knapsack_branch_and_bound(W, items))
