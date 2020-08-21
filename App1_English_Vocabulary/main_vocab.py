# Copyright (c) Andrii Ivasiv 
# August 20, 2020
#
# import json file with the structure word-meaning
# get the user input for the word -> make it to the correct structure
# show the correct meaning of the word to the user

import json
import difflib
from difflib import SequenceMatcher, get_close_matches

def show_word_to_user():
    #get the input from user
    data_from_json = read_json_file("App1_English_Vocabulary/data.json")
    user_input = get_the_input_from_user().lower()
        
    if user_input in data_from_json:    
        print(data_from_json[user_input])
    else:
        print('Word doesn`t exist. The closest match is: ', get_close_matches(user_input, data_from_json, n=1, cutoff = 0.6)[0])
        if input('Is this a word that you need? If so - type yes, else type no:') == 'yes':
            print(data_from_json[get_close_matches(user_input, data_from_json)[0]])
        else:
            show_word_to_user()
    
# parameters: path to the file;
# description: reading the json file with data for all words, 
# It`s better to read the file one time 
# and return all data instead of reading it each time
def read_json_file(pathToTheFile):
    with open(pathToTheFile, "r") as data_file:
        return json.load(data_file)

# parameters: none
# description: get the inpout from user. In our case the inpout 
# will be assigned as a word that user wants to get
def get_the_input_from_user():
    user_input = input('Please, enter the word that you would like to understand: ')
    return user_input

show_word_to_user()