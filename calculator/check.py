# import from py module in same folder
from arithmetic import *

def input_and_parameter_check():
    """Ask for user input, and confirms it has the correct number of parameters."""
    while True:
        user_input = raw_input(">> ")
        user_input = user_input.rstrip()
        tokens = user_input.split(" ")
        correct_num_items = {"+":3,"-":3,"*":3,"/":3,"square":2,"cube":2,"pow":3,"mod":3, "q":1}
        if tokens[0] == "+":
            if len(tokens) >=3:
                return tokens
            else: 
                print "You entered the wrong number of parameters. Enter Again."
        elif len(tokens) != correct_num_items[tokens[0]]:
            print "You entered the wrong number of parameters. Enter Again."
        else:
            return tokens

def use_arithmetic_functions(to_calculate):
    """Takes in the user input (parameters), calls the function, and provides the answer."""  
    dict_of_functions = {"+": add,"-":subtract,"*": multiply,"/":divide,"square":square,"cube":cube,"pow":power,"mod":mod}
    if to_calculate[0] == "+":
        for ix in range(1,len(to_calculate)):
            to_calculate[ix] = float(to_calculate[ix])
        print (  dict_of_functions[to_calculate[0] ]  (to_calculate[1:])    )
    elif len(to_calculate) == 3:
        print (dict_of_functions[to_calculate[0]](float(to_calculate[1]), float(to_calculate[2])))
    elif len(to_calculate) == 2:
        print (dict_of_functions[to_calculate[0]](float(to_calculate[1])))


def main():
    """calls to the function for user to enter input, allows for quitting, 
    and recognizes invalid input (not a list of parameters)"""

    while True:
        try:
            input_for_arthimetic_funct = input_and_parameter_check()        #get input
            if input_for_arthimetic_funct[0] =="q":
                break
            else:
                use_arithmetic_functions(input_for_arthimetic_funct)        # perform the arthimetec function+
        except:
            print "enter a valid input"


if __name__ == "__main__":
    main()