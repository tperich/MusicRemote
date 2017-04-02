import platform
def detect():
    if platform.system() == "Windows":
        return "cls"
    else:
        return "clear"
