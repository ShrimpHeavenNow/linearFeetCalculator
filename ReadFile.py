with open('measurements.txt') as f:
    measurements = [line.strip().split("'") for line in f]

def Fractionize(size):
    a, b = float("." + size).as_integer_ratio()
    fraction = str(str(a) + "/" + str(b))
    if b == 1:
        fraction = ""
    return fraction



def Convert(number):
    feet = number // 12
    inches = number - feet * 12
    inches = str(inches).split(".")
    feet = str(feet).split(".")
    return str(feet[0] + "' - " + inches[0] + " " + Fractionize(inches[1]) + '"')


def PrintTotal(_measurements):
    if len(_measurements) == 0:
        print("No Measurements.")
        return
    total = 0
    for x in _measurements:
        total += x
    totaled = Convert(total)
    print("Measurements (in inches): ", _measurements)
    print("Total: ", totaled)
    return total


def Filter(_input):
    x = filter(str.isdigit, _input)
    number = "".join(x)
    return number



print(measurements)