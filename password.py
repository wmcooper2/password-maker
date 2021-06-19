import random
import sys
from pathlib import Path
from platform import system



def is_dict_file(file_name):
    if Path(file_name).exists() and Path(file_name).is_file():
        return True

#Check args for valid dictionaries
args = sys.argv[1:]
dictionaries = []
if system() == "Darwin":
    dictionaries = ["/usr/share/dict/web2", "/usr/share/dict/web2a"]
else:
    if len(args) > 0 :
        for dict_ in args:
            if is_dict_file(dict_):
                dictionaries.append(dict_)
    else:
        print("You need to specify at least one dictionary.")


#Assemble the word list
full_dict = []
desired_word_length = 4
for dict_ in dictionaries:
    with open(dict_, "r") as d:
        full_dict += d.readlines()

#Randomly select words
words = []
for i in range(desired_word_length):
    words.append(random.choice(full_dict))

#Strip the newline
cleaned = [word.strip() for word in words]

#Remove spaces and hyphens
for index, word in enumerate(cleaned):
    if " " in word or "-" in word:
        #just take the first part
        cleaned[index] = word.split()[0]

answer = input("Do you want to include symbols and numbers [y, n]? ")

#Satisfy common password requirements
cleaned = [word.capitalize() for word in cleaned]        #capitals

punctuation = ""
if answer.lower() == "y":
    random_num = lambda: random.randint(0, 9)                   #numbers
    nums = [word[:]+str(random_num()) for word in cleaned]
    punctuation = "!#$%&*+-:;<=>?@_~"
    punct = lambda: random.choice(punctuation)                  #symbols
    cleaned = [word[:]+punct() for word in nums]

#Join the words
joined = "".join(cleaned)

# Simple explanation to user
word_count = len(full_dict)
print(f"Using a wordlist of {word_count} words and adding numbers between them...")

if len(punctuation) > 0:
    possibilities = (word_count ** desired_word_length) * (len(punctuation)**(desired_word_length)) * (10 ** desired_word_length)
else:
    possibilities = (word_count ** desired_word_length) * (10 ** desired_word_length)

print("There are {:e} possible combinations.".format(possibilities))
print("Your new password:\n\t", joined)
