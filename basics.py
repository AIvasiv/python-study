import datetime;

#*****************************
#calculating list average
def calculateListAverage(list):
    average = 0.0
    for i in list:
        average += i
    average = average / len(list)
    print (average)
    
#*****************************
#testing the strings concatenation
def test_string_concatenation():
    user_input_string = input("Please, enter your name: ")
    message1 = f"Hello {user_input_string}"
    message2 = "Hello %s" % (user_input_string)
    print(message1) 


#*****************************
#basic function for user inputs editing
def build_user_inputs():
    lis_of_all_user_inputs = []
    while(True):
        temp_string = input('Please, enter the message: ').capitalize()
        user_input = temp_string
        if(temp_string[len(temp_string)-1] != '.' or temp_string[len(temp_string)-1] != '?' or temp_string[len(temp_string)-1] != '!'):
            temp_string += '.'
        lis_of_all_user_inputs.append(temp_string)
        if(user_input == '/end'):
            break
    return lis_of_all_user_inputs

#*****************************
#list comprehension basics
def delete_string_from_list(my_combined_list):
    return [iterator for iterator in my_combined_list if type(iterator)!=str]


build_user_inputs()
