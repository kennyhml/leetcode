
ROMAN_TO_VALUE = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
SPECIALS = {
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900
}

def roman_to_int(s: str) -> int:

    total = 0
    for roman_num, val in SPECIALS.items():
        if not roman_num in s:
            continue
        total += s.count(roman_num) * val
        s = s.replace(roman_num, "")

    return total + sum(ROMAN_TO_VALUE[c] for c in s)