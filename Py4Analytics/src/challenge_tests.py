# Holds all the tests for the various challenges presented in the challenges notebook.
from termcolor import colored


def assert_equal(a, b, test_name="", hint=""):
    result = a == b
    if result:
        status = "pass"
        msg_color = "green"
    else:
        status = "fail"
        msg_color = "red"
    msg = colored(f"Test {test_name}: {status}" f"\tResult: {a}. Expected {b}.", msg_color)
    if not result:
        msg += "\t" + colored(f"{hint}", "red", "on_white", attrs=["bold"])
    print(msg)


def alphabet_sample():
    # This is the word for which you should be replacing the vowels
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # create a variable to hold the new set of letters
    letters = ""
    # for each letter in the word provided
    for l in alphabet:
        # if the letter is an `a` then add a captial `A` to the new set of letters
        if l == "a":
            letters = letters + "A"
        # otherwise if the letter is an `e` then add a capital `E` to the new set of letters
        elif l == "e":
            letters = letters + "E"
        # otherwise if the letter is an `i` then add a capital `I` to the new set of letters
        elif l == "i":
            letters = letters + "I"
        # otherwise if the letter is an `e` then add a capital `O` to the new set of letters
        elif l == "o":
            letters = letters + "O"
        # otherwise if the letter is an `e` then add a capital `U` to the new set of letters
        elif l == "u":
            letters = letters + "U"
        # otherwise add the current letter to the new set of letters
        else:
            letters = letters + l

    # print out the new string
    letters
