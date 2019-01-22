string = "UDDDUDUU"
num = len(string)

def countingValleys(n,s):
    sea_level = 0
    valley_count = 0
    splitString = list(s)
    for i in range(0,num):
        if splitString[i] == "U":
            sea_level += 1
            if sea_level == 0:
                valley_count += 1
        elif splitString[i] == "D":
            sea_level -= 1
    print (valley_count)

countingValleys(num, string)