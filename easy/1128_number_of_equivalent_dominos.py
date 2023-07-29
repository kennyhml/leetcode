"""
Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if 
and only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can 
be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

 
EXPLANATION:

Finding matching dominos is easy because we can just sort them and use that property as a key to find
common dominos based on the criteria, the hard part is coming up with the fact that the combinations
of a number of common dominos is n * (n - 1) // 2 where n is the number of domino occurrences, because
for each occurrence we can make n * (n - 1) combinations and then we need to divide it by 2 because
2 values make up one combination
"""


def numEquivDominoPairs(dominoes: list[list[int]]) -> int:

    seen = {}
    for domino in dominoes:
        key = tuple(sorted(domino))
        seen[key] = seen.get(key, 0) + 1

    return sum(n * (n - 1) // 2 for n in seen.values())