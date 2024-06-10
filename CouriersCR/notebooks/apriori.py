def generate_candidates(itemsets, k):
    candidates = []
    for i in range(len(itemsets)):
        for j in range(i + 1, len(itemsets)):
            if itemsets[i][:k-2] == itemsets[j][:k-2]:
                candidates.append(itemsets[i] + [itemsets[j][-1]])
    return candidates

def prune(itemsets, candidates, k):
    pruned_candidates = []
    for candidate in candidates:
        subsets = [candidate[:k-1]] + [candidate[:k-1][:i] + candidate[:k-1][i+1:] for i in range(k-1)]
        if all(subset in itemsets for subset in subsets):
            pruned_candidates.append(candidate)
    return pruned_candidates

def apriori(transactions, min_support):
    itemsets = [[item] for transaction in transactions for item in transaction]
    frequent_itemsets = []
    k = 2

    while itemsets:
        candidates = generate_candidates(itemsets, k)
        counts = {candidate: 0 for candidate in candidates}

        for transaction in transactions:
            for candidate in candidates:
                if set(candidate).issubset(set(transaction)):
                    counts[candidate] += 1

        frequent_itemsets.extend([itemset for itemset, count in counts.items() if count >= min_support])
        itemsets = prune(itemsets, candidates, k)
        k += 1

    return frequent_itemsets

# Example usage
transactions = [
    ['bread', 'milk', 'eggs'],
    ['bread', 'butter'],
    ['milk', 'butter'],
    ['bread', 'milk', 'butter'],
    ['bread', 'milk', 'eggs', 'butter']
]

min_support = 3

frequent_itemsets = apriori(transactions, min_support)
print(frequent_itemsets)