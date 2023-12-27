def get_choice():
    while True:
        try:
            choice = int(input("Choose option: "))
            return choice
        except ValueError:
            print("Pleaset input number: ")

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please, we need positive integer")
        except ValueError:
            print("Pleaset input number: ")

def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            else:
                print("please, we need positive integer")
        except ValueError:
            print("Pleaset input number.")

