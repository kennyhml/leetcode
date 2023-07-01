"""
You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.

The ith item is said to match the rule if one of the following is true:

ruleKey == "type" and ruleValue == typei.
ruleKey == "color" and ruleValue == colori.
ruleKey == "name" and ruleValue == namei.

Return the number of items that match the given rule.
"""

def countMatches(items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
    if ruleKey == "type":
        match_idx = 0
    elif ruleKey == "color":
        match_idx = 1
    else:
        match_idx = 2

    count = 0
    for item in items:
        if item[match_idx] == ruleValue:
            count += 1

    return count
