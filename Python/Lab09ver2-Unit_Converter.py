def main():
    distance = int(input("What is the distance in feet? \n"))
    unit = str(input("What is the unit [ft][mi][m][yd][in]or[km]? \n"))
    if unit == 'ft':
        print(float(distance))
    elif unit == 'mi':
        print(float(distance * 0.000189394))
    elif unit == 'km':
        print(float(distance * 0.0003048))
    elif unit == 'm':
        print(float(distance * 0.3048))
    elif unit == 'yd':
        print(float(distance) * 0.333333)
    elif unit == 'in':
        print(float(distance) * 12)
    else:
        print("INVALID RESPONSE")
main()