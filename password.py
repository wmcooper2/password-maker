import random

dict1 = "/usr/share/dict/web2"
dict2 = "/usr/share/dict/web2a"
full_dict = []
desired_word_length = 4

with open(dict1, "r") as d:
    full_dict += d.readlines()

with open(dict2, "r") as d:
    full_dict += d.readlines()

words = []
for i in range(desired_word_length):
    words.append(random.choice(full_dict))

cleaned = [word.strip() for word in words]

# Spaces and hyphens are annoying
for index, word in enumerate(cleaned):
    if " " in word or "-" in word:
        #just take the first part
        cleaned[index] = word.split()[0]

camel_case = [word.capitalize() for word in cleaned]
random_num = lambda: random.randint(0, 9)
numbers_between = [word[:]+str(random_num()) for word in camel_case]
joined = "".join(numbers_between)


# Simple explanation to user
word_count = len(full_dict)
print(f"Using a wordlist of {word_count} words and adding numbers between them...")
possibilities = word_count ** desired_word_length
possibilities *= (10 ** 4)
print("There are {:e} possible combinations.".format(possibilities))
print("Your new password:\n\t", joined)
