def swap_case(myString):
    swappedString = ""
    for char in myString:
        if char.islower():
            swappedString += char.upper()
        elif char.isupper():
            swappedString += char.lower()
        else:
            swappedString += char
    return swappedString

def swap_caseFunction(myString):
    return myString.swapcase()

myString = 'HackerRank.com presents "Pythonist 2".'
result = swap_case(myString)
print(result)
print(swap_caseFunction(myString))