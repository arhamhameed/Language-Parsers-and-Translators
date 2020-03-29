import typing
from typing import List
from chomsky import read_grammar, convert_grammar

def parse(grammar_file_path: List[str], sentence: str) -> bool:
    """
    The code for Cocke-Younger-Kasami (CYK) algorithm is taken from this 
    source: https://github.com/RobMcH/CYK-Parser/blob/master/cyk_parser.py
    I added documentations to understand it better and removed the functions that were not required. 
    Also changed the code to align with the task requirements. 

    param: (1) the file path of CNF
           (2) the sentence that we are testing for recognizability by our Machine

    return: boolean value of True or False
    """

    # Imports the function from chomsky.py
    # Converts teh grammar list to CFG
    grammar = convert_grammar(grammar_file_path)
    new_string = sentence.split()
    length = len(new_string)
    matrix = [[[] for x in range(length)] for y in range(length)]

    for word in range(length):
        for rule in grammar:
            if rule[1] == "\'%s\'" % new_string[word]:
                matrix[0][word].append(rule[0])

    for words_to_consider in range(2, length + 1):
        for start_cell in range(0, length - words_to_consider + 1):
            for left_size in range(1, words_to_consider):
                right_size = words_to_consider - left_size
                for rule in grammar:
                    if [x for x in matrix[left_size - 1][start_cell] if x == rule[1]]:
                        if [x for x in matrix[right_size - 1][start_cell + left_size] if x == rule[2]]:
                            matrix[words_to_consider - 1][start_cell].append(rule[0])

    sentence = grammar[0][0]


    # Returns if the sentence is contained in a language or not
    if [n for n in matrix[-1][0] if n == sentence]:
        print("The sentence belongs to the language produced by the grammar :)")
        return True
    else:
        print("The sentence does not belongs to the language produced by the grammar :(")
        return False
