"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""
from arithmetic import *
import sys

def consume_input(entry):
    list1 = entry.split()
    return list1

def need_three_inputs(list2):
    input_length = len(list2)

    if input_length == 3:
        return True
    else:
        return False

def need_two_inputs(list2):
    input_length = len(list2)
    if input_length == 2:
        return True
    else:
        return False   

def evaluate(list2):
    operator = list2[0]
    length_test_3 = need_three_inputs(list2)
    length_test_2 = need_two_inputs(list2)
    if operator == "+":
        if length_test_3 == True:
            return add(int(list2[1]), int(list2[2]))
        else:
            return "Please input two numbers."
    
    elif operator == "-":
        if length_test_3 == True:
            return subtract(int(list2[1]), int(list2[2]))
        else:
            return "Please input two numbers."
    
    elif operator == "*":
        if length_test_3 == True:
            return multiply(int(list2[1]), int(list2[2]))
        else:
            return "Please input two numbers."
    
    elif operator == "/":
        if length_test_3 == True:
            return divide(int(list2[1]), int(list2[2]))
        else:
            return "Please input two numbers."
    
    elif operator == "square":
        if length_test_2 == True:
            return square(int(list2[1]))
        else:
            return "Please input only one number."
    
    elif operator == "cube":
        if length_test_2 == True:
            return cube(int(list2[1]))
        else:
            return "Please input only one number."
    
    elif operator == "pow":
        if length_test_3 == True:
            return power(int(list2[1]), int(list2[2]))
        else:
            return "Please input two numbers."
    
    elif operator == "mod":
        if length_test_3 == True:
            return mod(int(list2[1]), int(list2[2]))
        else:
            return "Please input two numbers."
    
    else:
        return "I don't understand!"


def main():
    while True:
        string = raw_input("> ")
        if string == "q":
           sys.exit()
        else:
            main_list = consume_input(string)
            output = evaluate(main_list)
            print output

if __name__ == '__main__':
    main()
