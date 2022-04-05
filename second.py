from random import randint

x = randint(1, 100)
y = randint(1, 100)

sum = x + y

print("The first number is: ", x)
print("The second number is: ", y)

Answer = input("What is the sum of the numbers above? ")

if (int(Answer) == sum):
    print("You were right!")
else:
    print("Sorry, you were wrong")