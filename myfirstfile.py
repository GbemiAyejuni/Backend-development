def multiply(a, b, c):
    return a*b*c

def print5times(text, i): # i represents the number of times you want the text repeated
    for n in range(i):
        print(text)

Result = multiply(1, 2, 3)
print("The multiplication of the three numbers is: " + str(Result))

print()

print5times("Mumswhocode", 5)