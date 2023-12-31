# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# # Looping through dictionaries:
# for (key, value) in student_dict.items():
#     # Access key and value
#     pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# # Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     # Access index and row
#     # Access row.student or row.score
#     pass

# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# with open("Nato_alphabet/nato_phonetic_alphabet.csv") as f:
#     data = f.readlines()
# data = [n.strip().split(",") for n in data]
# data_dict = {n[0]: n[1] for n in data[1:]}
# print(data_dict)
# or
import pandas as pd


data = pd.read_csv("Nato_alphabet/nato_phonetic_alphabet.csv")
# {new_key:new_value for (index, row) in df.iterrows()}
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(data_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# word = input("Enter a word: ").upper()
# output_list = [data_dict[letter] for letter in word]
# print(output_list)

# Raise exception when the user input sth that is not a alphabet.
# while True:
#     try:
#         word = input("Enter a word: ").upper()
#         output_list = [data_dict[letter] for letter in word]
#         print(output_list)
#     except KeyError:
#         print("Sorry,only letters in the alphabet please.")

# But this not good.
# It is better to create a function, and when we got an error, we print sth and repeat the function to give the user another chance to input sth.


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [data_dict[letter] for letter in word]
    except KeyError:
        print("Sorry,only letters in the alphabet please.")
        generate_phonetic() # look here
    else:
        print(output_list)


generate_phonetic()
