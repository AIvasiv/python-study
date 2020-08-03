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

#testing the strings
user_input = input("Please, enter your name: ")
message1 = f"Hello {user_input}"
message2 = "Hello %s" % (user_input)
print(message1)


#*****************************
lis_of_all_user_inputs = []

while(user_input != '/end'):
    temp_string = input('Please, enter the message: ').capitalize()
    user_input = temp_string
    if(temp_string[len(temp_string)-1] != '.' or temp_string[len(temp_string)-1] != '?' or temp_string[len(temp_string)-1] != '!'):
        temp_string += '.'
    lis_of_all_user_inputs.append(temp_string)
print (lis_of_all_user_inputs)



