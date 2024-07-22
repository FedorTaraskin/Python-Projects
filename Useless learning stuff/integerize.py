def mode1():
    num1 = float(input("Number: "))
    try:
            if num1 == int(num1):
                print("It is an integer in float form.")
            else:
                print("No, it is a float and should stay being so.")
    except ValueError:
            print("That's not even a number!")

def mode2():
    num1 = float(input("Number: "))
    try:
        if abs(num1 - int(num1)) < 1e-9: # Use a small threshold for comparison
            print("It is an integer in float form.")
        else:
            print("No, it is a float and should stay being so.")
    except ValueError:
        print("That's not even a number!")

mode = int(input("Enter 1 for AI's version, 2 for my original one: "))
if mode == 1:
    mode1()
elif mode == 2:
    mode2()
