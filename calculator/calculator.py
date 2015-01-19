
from arithmetic import *
import sys

def input_check(main_list):
    correct_entry_dict = {"+":3,"-":3,"*":3,"/":3,"square":2,"cube":2,"pow":3,"mod":3}

    if len(main_list) < correct_entry_dict[main_list[0]]:
        print "Incorrect number of inputs. Please add more."
        return False
    elif len(main_list) > correct_entry_dict[main_list[0]]:
        print "Incorrect number of inputs. Please remove some."
        return False
    else:
        return True

def evaluate(list2):
    operator = list2[0]
    dict_of_functions = {"+": add,"-":subtract,"*": multiply,"/":divide,"square":square,"cube":cube,"pow":power,"mod":mod}

    if operator in dict_of_functions:
        if len(list2) == 3:
            print dict_of_functions[operator](float(list2[1]), float(list2[2]))
        else:
            print dict_of_functions[operator](float(list2[1]))
    else:
        print "I don't understand! Please input valid operator."


def main():
    while True:
        string = raw_input("> ")
        if string == "q":
           sys.exit()
        else:
            main_list = string.split()
            if input_check(main_list) == True:
                evaluate(main_list) 
            else:
                continue

if __name__ == '__main__':
    main()
