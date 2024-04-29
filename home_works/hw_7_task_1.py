# Make a program that has some sentence (a string) on input
# and returns a dict containing all unique words as keys and the number of occurrences as values.


def sentence_to_dict(user_input):
    split_words = user_input.split()
    user_input_dict = {}
    for unique_word in split_words:
        if unique_word in user_input_dict:
            user_input_dict[unique_word] += 1
        else:
            user_input_dict[unique_word] = 1
    return user_input_dict


user = input("Provide a sentence: ")
result = sentence_to_dict(user)
print(result)






