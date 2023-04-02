#!/usr/bin/env python3

def return_evens(num_list):
    even_list = [i for i in num_list if i % 2 == 0]
    return even_list
    


def make_exclamation(sentence_list):
    exclamation_list = [(i + "!") for i in sentence_list]
    return exclamation_list


print(return_evens([0,1]))

print (make_exclamation(["Hello", "I'm doing great", "Python is fun"]))