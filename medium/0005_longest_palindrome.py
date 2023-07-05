"""
Given a string s, return the longest palindromic substring in s.

EXPLANATION:

This was a really hard one, just as a reminder a palindrome is a string that is the same
when reversed, for example 'bab' or 'bb' or just a single character like 't'.

My first thought when I read palindrome was a two pointer technique where we slide towards the middle,
but I quickly realized that it would be extremely inefficient to catch all palindromes that way.

So whats another way to spot a palindrome efficiently when we dont slide in from the sides?
Right, we slide from the center outwards! So, the idea here is to iterate over every character and
then expand outwards from said character to see how much we can expand it until it is no longer a palindrome.

But when that code is submitted, we quickly notice it will fail, why? Because that solution assumes an
odd length palindrome, what if its even? For example: 'cbbd'. The correct answer would be 'bb', but we cant
find it because we check left and right for every character only.

Thats why we have to check odd and even length palindromes for every single character, we can do so by either
moving our left pointer one to the left, or the right pointer one to the right - it ultimately doesnt matter.

To make it more efficient, unlike alot of other solutions, I decided to store the current longest palindrome
purely in its slicing indices, performing a string operation every single time we update it would take a lot 
of performance.
"""
def longestPalindrome(s: str) -> str:
    longest = (0, 0)
    length = len(s)

    for i in range(len(s)):
        l = r = i

        while l >= 0 and r < length and s[l] == s[r]:
            l -= 1
            r += 1

        longest = max((l + 1, r), longest, key=lambda t: t[1] - t[0])

        l, r = i, i + 1
        while l >= 0 and r < length and s[l] == s[r]:
            l -= 1
            r += 1

        longest = max((l + 1, r), longest, key=lambda t: t[1] - t[0])

    l, r = longest
    return s[l:r]