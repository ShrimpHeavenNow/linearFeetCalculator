with open('measurements.txt') as f:
    measurements = [line.strip().split("'") for line in f]


def Fractionize(size):
    a, b = float("." + size).as_integer_ratio()
    fraction = str(str(a) + "/" + str(b))
    if b == 1:
        fraction = ""
    return fraction


def Convert(number):
    _feet = number // 12
    _inches = number - _feet * 12
    _inches = str(_inches).split(".")
    _feet = str(_feet).split(".")
    return str(_feet[0] + "' - " + _inches[0] + " " + Fractionize(_inches[1]) + '"')


newMeasurements = []
for x in measurements:  # This whole section blows chunks, man. I know this could be more elegant.
    keep = True
    newx = []
    if len(x) == 1:
        newx = ['0']
    for y in x:
        newy = y
        if "-" in newy:
            newy = newy.replace("-", "")
        if '"' in newy:
            newy = newy.replace('"', "")
        newy = newy.strip()
        if len(x) == 2 and y == "":
            newy = "0"
        if len(newy) > 1 and newy[0].isdigit() == False:
            keep = False
        else:
            newx.append(newy)
    if keep:
        newMeasurements.append(newx)

while ["0", ""] in newMeasurements:  # This especially. There ought to be a way to not have this happen.
    newMeasurements.remove(["0", ""])

print(len(newMeasurements), "Entries")
total = 0
for x in newMeasurements:
    feet = 0
    inches = 0.0
    z = 0
    fractions = 0
    feet += int(x[0])
    print(feet, "feet")
    if "/" in x[1]:
        if " " in x[1]:
            z = x[1].split(" ")
            fractions = z[1].split("/")
            z = z[0]
        else:
            z = 0
            fractions = x[1].split("/")
        fractions = int(fractions[0]) / int(fractions[1])
    else:
        z = x[1]
    inches += int(z) + fractions
    print(inches, " inches")
    subtotal = inches + (feet * 12)
    total += inches + (feet * 12)
    print("subtotal: ", subtotal)
    print("total: ", total)

print("")
print("Grand Total: ")
print(Convert(total))
