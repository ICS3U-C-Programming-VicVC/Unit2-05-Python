global_variable = 15


def main():
    GlobalToLocal()
    GlobalToGlobal()


def GlobalToLocal():

    global_variable = 1
    second_variable = 15
    third_variable = global_variable + second_variable

    print(
        "LOCAL: global_variable + secound_variable = third_variable: {0} + {1} = {2}".format(
            global_variable, second_variable, third_variable
        )
    )


def GlobalToGlobal():

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
