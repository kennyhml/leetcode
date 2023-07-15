"""
Given an array of integers citations where citations[i] is the number of citations 
a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the 
maximum value of h such that the given researcher has published at least h papers 
that have each been cited at least h times.

EXPLANATION:

Easiest solution is sorting the array in descending order, we then iterate over it.
If the current element is smaller or equal to its index, we know that we found the
maximum citation count with that many papers (the h-index).

Imagine the following array, [3,0,6,1,5], sorted [6, 5, 3, 1, 0]

 0  1  2  3  4       0  1  2  3  4       0  1  2  3  4
[6, 5, 3, 1, 0]     [6, 5, 3, 1, 0]     [6, 5, 3, 1, 0]
 ↑                      ↑                      ↑
6 is not <= 1        5 is not <= 2     3 is <= 3, 3 is the result

Since the values are sorted and we want the biggest possible result, its pointless
looking further right since the citation will now always be smaller.

An edgecase would be an array like [1] where there wont be a numer smaller or equal to
its index. Which is why incase we didnt find the number while iterating we just return
the length of the array, since all citations will contribute to the h-index in that case.
"""

def hIndex(citations: list[int]) -> int:

    citations.sort(reverse=True)
    
    for i, citation in enumerate(citations):       
        if i >= citation:
            return i
    
    return len(citations)