# @author Andrii Ivasiv
# Monday, 25 May, 2020
# Hebbian learning rule.  Writing my own Perceptron - trying to detect number 5.
import random

#dataset to study (numbers from 0 to 9)
num0 = list('111101101101111')
num1 = list('001001001001001')
num2 = list('111001111100111')
num3 = list('111001111001111')
num4 = list('101101111001001')
num5 = list('111100111001111')
num6 = list('111100111101111')
num7 = list('111001001001001')
num8 = list('111101111101111')
num9 = list('111101111001111')
#list of numbers
nums = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]
#different types of number 5
num51 = list('111100111000111')
num52 = list('111100010001111')
num53 = list('111100011001111')
num54 = list('110100111001111')
num55 = list('110100111001011')
num56 = list('111100101001111')

#initialize weights with value 0 or weights = [0 for i in range(15)]
weights = []
for i in range(15):
    weights.append(0)

#selecting the bias - if sum equals or larger than set value to 1
bias = 7


# function to calculate sum and compare it to bias - one step of nn working
def proceed(number):
    # calculate the net
    net = 0
    for i in range(15):
        net += int(number[i]) * weights[i]

    # is it larger than bias? (yes - we suppose, that number is 5. No - other number)
    return net >= bias

# Decrease weights if network made mistake and showed 1
def decrease(number):
    for i in range(15):
        # is entrance active
        if int(number[i]) == 1:
            # decrease value for 1
            weights[i] -= 1

# Increasing weights if network made mistake and showed 0
def increase(number):
    for i in range(15):
        # is entrance active
        if int(number[i]) == 1:
            # increase value for 1
            weights[i] += 1


# Training our network (10 000 times)
for i in range(10000):
    # Generate random number from 0 to 9
    option = random.randint(0, 9)

    # if number is not 5
    if option != 5:
        # If network showed True/1, this is a mistake - decrease value
        if proceed(nums[option]):
            decrease(nums[option])
    # If number is 5
    else:
        # If network showed False/0, than show that this number is what we need:
        if not proceed(num5):
            increase(num5)

# Show weights
print(weights)

# Test
print("0 is 5? ", proceed(num0))
print("1 is 5? ", proceed(num1))
print("2 is 5? ", proceed(num2))
print("3 is 5? ", proceed(num3))
print("4 is 5? ", proceed(num4))
print("6 is 5? ", proceed(num6))
print("7 is 5? ", proceed(num7))
print("8 is 5? ", proceed(num8))
print("9 is 5? ", proceed(num9), '\n')

# Test
print("Is 5? ", proceed(num5))
print("Is 5 - 1? ", proceed(num51))
print("Is 5 - 2? ", proceed(num52))
print("Is 5 - 3? ", proceed(num53))
print("Is 5 - 4? ", proceed(num54))
print("Is 5 - 5? ", proceed(num55))
print("Is 5 - 6? ", proceed(num56))