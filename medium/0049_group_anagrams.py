"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

EXPLANATION:

Not sure why this is listed medium, its far easier than lots of easy problems.

The only hurdle is fuguring out which words are anagrams to another word, how do we do that?
Luckily, anagrams have to consist of the same letters, just in a different order, so we could use
a set right? Sure two anagrams would have the same elements in their set representation, but
for this purpose we need something hashable, so a set isnt going to work.

Instead we just sort the word, if two words are anagrams they are the exact same when sorted.

So all we have to do is sort each word, the sorted word is the keyword for this anagram.
Then we check wheteher we have already seen another anagram with that keyword, if we have then
we can just add it to the group, otherwise we make a new group.
"""

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    groups = {}

    for word in strs:
        keyword = "".join(sorted(word))

        arr = groups.get(keyword)
        if arr is None:
            groups[keyword] = [word]
        else:
            arr.append(word)

    return groups.values()

