import platform
def detect():
    if platform.system() == "Windows":
        clear = "cls"
    else:
        clear = "clear"
    return clear
