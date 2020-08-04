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

#*****************************
#calculate the average of user inputs - function with an arbitrary number of non-keyword arguments
def calculate_average(*args):
    return sum(args)/len(args)

#*****************************
#function that takes an infinite numbers of string parameters and returns a list containing all the strings in uppercase
#and sorted alphabetically
def my_function(*args):
    return [iterator.upper() for iterator in  sorted(args)]

#*****************************
#function with an arbitrary number of keyword arguments
def find_sum(**kwargs):
    return sum(kwargs.values())

#*****************************
#function reads the file and prints out the first 90 characters of content
def read_crop_file():
    with open("files/fruits.txt", "r") as myfile:
        content_file = myfile.read()
        print(content_file[:90])
        
#*****************************
#function that returns the number of occurances of first paramter in the file that is defined in second parameter
def read_crop_file2(string_var, filepath_var):
    i = 0
    with open(filepath_var, "r") as myfile:
        content_file = myfile.read()
        for iterator in content_file:
            if (iterator == string_var):
                i = i + 1
    return i

#*****************************
#function creates file from cropped string in previous function
def create_file_from_cropped():
    with open("first.txt", "w") as file_created:
        file_created.write(read_crop_file())

#*****************************
#function that opens and read the first file an d then appends text from the first file to the second one
def append_text_to_file():
    with open("bear1.txt", "r") as bear1_file:
        with open("bear2.txt", "a+") as bear2_file:
            bear2_file.write(bear1_file.read())
