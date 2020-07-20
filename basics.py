import datetime;

#print(dir(int))
#help(int.real)

my_list = [1.1, 1.2, 1.3]
#print(dir(list))

def calculateListAverage(list):
    average = 0.0
    for i in list:
        average += i
    average = average / len(list)
    print (average)
    
calculateListAverage(my_list)
