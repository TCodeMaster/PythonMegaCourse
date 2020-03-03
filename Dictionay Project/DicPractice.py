import json
from difflib import get_close_matches

data = json.load(open("C:/Users/Tariq Ali\Desktop\Python - Sumurai/Dictionary Application/data.json"))

#take input from user
#lowercase the input
#if the word is incorrect return a suggestion with closest meaning
#ask with Y/N if the suggestion is correct and return the meaning

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        x = input("Did you mean %s instead? If Yes enter 'Y' if not 'N': " % get_close_matches(word, data.keys())[0])
        if x =='Y':
            return data[get_close_matches(word, data.keys())[0]]
        elif x == 'N':
            return "The word doesnot exist"
        else:
            return "Please select the correct option"
    else:
        return "The word doesn't exist"

data_input = input("Please enter the word: ")
y = (translate(data_input))

for j in y:
    print(j)

