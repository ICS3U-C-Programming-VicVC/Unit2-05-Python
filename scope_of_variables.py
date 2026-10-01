#!/usr/bin/env python3
# Created By: Victor V-C
# Date: 09 29, 2026
# This code demonstrates an example of scoping in coding

global_variable = 15

def main():
    # Calls both scope demo functions
    local_scope()
    global_scope()


def local_scope():

    # Demonstrates local variables

    global_variable = 1
    second_variable = 15
    third_variable = global_variable + second_variable

    print(
        "LOCAL: global_variable + secound_variable = third_variable: {0} + {1} = {2}".format(
            global_variable, second_variable, third_variable
        )
    )


def global_scope():

    # Demonstrates global variables

    global global_variable

    global_variable += 5
    second_variable = 15
    third_variable = global_variable + second_variable

    print(
        "GLOBAL: global_variable + secound_variable = third_variable: {0} + {1} = {2}".format(
            global_variable, second_variable, third_variable
        )
    )


if __name__ == "__main__":
    main()
