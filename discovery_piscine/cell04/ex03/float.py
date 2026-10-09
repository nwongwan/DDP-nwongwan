try:
    num = float(input("Give me a number: "))
    if num == int(num):
        print("The number is an integer.")
    else:
        print("The number is a decimal.")
except ValueError:
    pass