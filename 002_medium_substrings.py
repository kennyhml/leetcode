"""
Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring:
------------
A player gets +1 point for each occurrence of the substring in the string .

For Example:
------------
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.


minion_game has the following parameters:

string: the string to analyze

string: the winner's name and score, separated by a space on one line, or Draw if there is no winner
Input Format


EXPLANATION:
------------
Example string "BANANA", if we start by looking at substrings starting with "B",
we can just use the position of the B to figure out there are 6 substrings starting
with B because len(string) - index of B (0) == 6. Like: B, BA, BAN, BANA, BANAN, BANANA
And therefore the words give Stuart 6 points in total. We could create those substrings, 
but it's not necessary to create them, it's gonna be 6 just based on where the B is positioned in the string
"""
VOWELS = ["A", "E", "I", "O", "U"]

def minion_game(string):
    # set scores
    stuart_score = 0
    kevin_score = 0

    # get strings length
    str_length = len(string)
    
    # get index and character for each char
    for index, char in enumerate(string):
        # get possible combinations for the character
        combinations =  str_length - index

        # assign score to the right person
        if char in VOWELS:
            kevin_score += combinations
        else:
            stuart_score += combinations
    # print result
    if stuart_score > kevin_score:
        print("Stuart", stuart_score)
        
    elif stuart_score < kevin_score:
        print("Kevin", kevin_score)
                
    else:
        print("Draw")