measurements = []
saved = [5, 7.5]
beep = True
import winsound

print("")
print("The Amazing Foot Adder")
print("")
print('To start a new measurement, type "n" or "new" in the "Feet" prompt.')
print('To undo the last measurement, type "u" or "undo" in the "Feet" prompt')
print('To save your current total and start a new measurement, type "s" or "save" in the "Feet" prompt')
print('to total your saved measurements, type "t" or "total" in the "Feet" prompt')
print('To clear your saved numbers, type "c" or "clear" in the "Feet" prompt')
print('There is a beep after each entry. type "b" or "beep" in the "Feet" prompt to enable or disable it.')
print("")
print("Begin entering your measurements below.")
print("")

def Fractionize(size):
    a, b = float("." + size).as_integer_ratio()
    fraction = str(str(a) + "/" + str(b))
    if b == 1:
        fraction = ""
    return fraction


def Filter(input):
    x = filter(str.isdigit, input)
    number = "".join(x)
    return number
def Convert(number):
    feet = number // 12
    inches = number - feet * 12
    inches = str(inches).split(".")
    feet = str(feet).split(".")
    return str(feet[0] + "' - " + inches[0] + " " + Fractionize(inches[1]) + '"')


def PrintTotal(measurements):
    if len(measurements) == 0:
        print("No Measurements.")
        return
    total = 0
    for x in measurements:
        total += x
    feet = total // 12
    inches = total - feet * 12
    inches = str(inches).split(".")
    feet = str(feet).split(".")
    print("Measurements (in inches): ", measurements)
    print("Total: " + feet[0] + "' - " + inches[0] + " " + Fractionize(inches[1]) + '"')
    return total


def AddMeasurements(measurements):
    feet = input("Feet: ")
    if feet == '':
        feet = "0"
    if "n" == str(feet).lower()[0]:
        print("New measurement started.")
        return []
    if "u" == str(feet).lower()[0]:
        print("Previous entry deleted.")
        measurements = measurements[:-1]
        PrintTotal(measurements)
        print("")
        return list(measurements)
    if "s" == str(feet).lower()[0]:
        global saved
        saved.append(PrintTotal(measurements))
        print("Value added to saved")
        print("Current Saved Values: ", saved)
        return
    if "t" == str(feet).lower()[0]:
        print("Totalling saved measurements:")
        PrintTotal(saved)
        return
    if "b" == str(feet).lower()[0]:
        if beep:
            print("Beep disabled")
            global beep
            beep = False
            return
        else:
            print("Beep Enabled")
            beep = True
            return
    if "c" == str(feet).lower()[0]:
        saved = []
        print("Saved numbers cleared.")
        return
    feet = Filter(feet)
    try:
        feet = int(feet)

        inches = input("Inches: ")
        if inches == '':
            inches = "0"
        inches = Filter(inches)
        inches = int(inches)

        eighths = input("eighths: ")
        if eighths == '':
            eighths = "0"
        eighths = Filter(eighths)
        eighths = int(eighths)

    except:
        print("enter a valid number")
        winsound.PlaySound("*", winsound.SND_ALIAS)
        return measurements
    inches += (feet * 12) + (eighths / 8)
    measurements.append(inches)

    PrintTotal(measurements)
    return measurements


while True:
    measurements = AddMeasurements(measurements)
    if beep == True:
        winsound.Beep(440, 100)
    print("")