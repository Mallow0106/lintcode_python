
def getStrList(input_str):
    if "[" in input_str:
        input_str = input_str.replace("[", '')
    if "]," in input_str:
        input_str = input_str.replace("],", '')
    if "]" in input_str:
        input_str = input_str.replace("]", '')
    return input_str.split(",")

def getIntList(input_str):
    return [ int(a) for a in getStrList(input_str)]
