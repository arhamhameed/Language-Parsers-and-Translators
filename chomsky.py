'''
The code I used to convert the Context Free Grammar to Chomsky Normal form is taken from this 
source: https://github.com/RobMcH/CYK-Parser/blob/master/grammar_converter.py
I added documentations to understand it better and removed the functions that were not required. 
Also changed the code to align with the task requirements. 
'''
import typing
from typing import List

def read_grammar(file_path: str) -> List[str]:
    """
    Reads in the given grammar file and splits it into separate lists for each rule.
    param: the file path to the grammar file
    return: the list of rules.
    """

    with open(file_path, 'r') as grammar_file:
        rules = grammar_file.readlines()
    return rules


def convert_grammar(grammar_file_path: str) -> List[List[str]]:
    """
    Converts a context-free grammar in the Chomsky Normal Form 
    param: the grammar_file_path
    return: A nested list where sublists contain a single rule
    """

    rules = read_grammar(grammar_file_path)
    grammar = []
    vert = "|"
    arrow = "->"

    # the for loop divides the left and right side of the arrow in two parts
    # the left side is stored in an array
    # the right side is further divided based on teh verticals
    for rule in rules:
        if "|" in rule:
            left, right = rule.split(arrow)
            left = [left.strip()]
            right_items = right.split(vert)
            for item in right_items:
                item_list = item.split()
                grammar.append(left + item_list)
        else:
            grammar.append(rule.replace(arrow, '').split())

    dictlist = {}
    unit_productions = []
    result = []
    index = 0

    for rule in grammar:
        new = []
        # Rule is in form A -> X, so back it up for later and continue with the next rule.
        if len(rule) == 2 and rule[1][0] != "'":
            unit_productions.append(rule)
            # looks if the rule already exists or not
            if rule[0] in dictlist:
                dictlist[rule[0]] += [rule[1:]]
            else:
                dictlist[rule[0]] = [rule[1:]]
            continue
        # Rule is in form A -> X B C [...] or A -> X a.
        elif len(rule) > 2:
            terminals = []
            for i in range(len(rule)):
                if rule[i][0] == "'":
                    terminals.append((rule[i], i))
            if terminals:
                for item in terminals:
                    # Create a new non terminal symbol and replace the terminal symbol with it.
                    # The non terminal symbol derives the replaced terminal symbol.
                    rule[item[1]] = str(rule[0]) + str(index)
                    new.append([str(rule[0]) + str(index), item[0]])
                index += 1
            while len(rule) > 3:
                new.append([str(rule[0]) + str(index), rule[1], rule[2]])
                rule = [rule[0]] + [str(rule[0]) + str(index)] + rule[3:]
                index += 1
        # Again looks if the rule already exists or not
        if rule[0] in dictlist:
            dictlist[rule[0]] += [rule[1:]]
        else:
            dictlist[rule[0]] = [rule[1:]]
        result.append(rule)
        if new:
            for new_rule in new:
                result.append(new_rule)

    # Handle the unit productions (A -> X)
    while unit_productions:
        rule = unit_productions.pop()
        if rule[1] in dictlist:
            for item in dictlist[rule[1]]:
                new_rule = [rule[0]] + item
                if len(new_rule) > 2 or new_rule[1][0] == "'":
                    result.append(new_rule)
                else:
                    unit_productions.append(new_rule)
                if rule[0] in dictlist:
                    dictlist[rule[0]] += [rule[1:]]
                else:
                    dictlist[rule[0]] = [rule[1:]]
    return result
