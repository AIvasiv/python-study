# @author Andrii Ivasiv
# Monday, 25 May, 2020
# Practice with linear approximation using Perceptron without actovation function

import random

# angle, variable near x in the formula y = kx + c
k = random.uniform(-5, 5)

c = random.uniform(-5, 5)

#Print starting coordinates of the line
print('Starting line: ', k, '* X + ', c)

# set of our points on the X:Y
data = {
    1: 2,
    2: 4.2,
    2.5: 5,
    3.8: 7.9,
    4: 9,
    6: 10.2,
    6.6: 13,
    7.2: 15.3,
    8: 17.1,
    8.5: 19.5
}

# the training speed
rate = 0.0001

# function to calculate y
def proceed(x):
    return x*k+c

#training our network
#1000 000 times
for i in range(100000):
    # Random coordinate of X
    x = random.choice(list(data.keys()))

    # Find Y
    true_result = data[x]

    # Find network answer
    out = proceed(x)

    # calculate delta
    delta = true_result - out

    # change weight near x like in the rule
    k += delta * rate * x

    # change the c
    c += delta * rate

# results
print('Ready line: ', k, '* X + ', c)