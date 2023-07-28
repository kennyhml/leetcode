"""
Given a sentence text (A sentence is a string of space-separated words) in the following format:

First letter is in upper case.
Each word in text are separated by a single space.
Your task is to rearrange the words in text such that all words are rearranged in an increasing 
order of their lengths. If two words have the same length, arrange them in their original order.

Return the new text following the format shown above.

EXPLANATION:

I decided to go with an approach where I parse the data and then reconstruct the sentence from that,
which works and is efficient, but for some reason the default python sorting by length already retains
the original order if two elements have the same length, so the solution can be much more trivial.
"""


def longArrangeWords(text: str) -> str:
    data = {}
    res = ""
    for i, word in enumerate(text.split()):
        length = len(word)
        if length in data:
            data[length].append((word, i))
        else:
            data[length] = [(word, i)]

    for length, words in sorted(data.items(), key=lambda x: x[0]):
        if len(words) > 1:
            words.sort(key=lambda w: w[1])

        for word in words:
            if not res:
                res += f"{word[0].title()}"
            else:
                res += f" {word[0].lower()}"

    return res


def shortArrangeWords(text: str) -> str:
    return " ".join(sorted(text.split(), key=len)).capitalize()
