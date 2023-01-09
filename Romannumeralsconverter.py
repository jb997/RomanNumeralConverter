import operator

def convert(number):
    numerals = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40,  "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}
    result = ""
    for entry in sorted(numerals.items(), key=operator.itemgetter(1), reverse=True):
        while number >= entry[1]:
            result += entry[0]
            number -= entry[1]
    return result



print convert(40)
print convert(149)
print convert(3)
print convert(4)
print convert(5)
print convert(6)
print convert(7)
print convert(9)
print convert(19)
print convert(24)
print convert(26)
print convert(29)
print convert(49)
print convert(50)
print convert(89)
print convert(399)
print convert(899)
