from platform import system
def clear():
    return ["clear", "cls"][system()=="Windows"]
