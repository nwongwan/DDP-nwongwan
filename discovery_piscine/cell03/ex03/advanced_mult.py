import sys

if len(sys.argv) > 1:
    print("none")
else:
    table = 0

    while table <= 10:
        i = 0
        result = f"Table de {table}:"

        while i <= 10:
            result += f" {table * i}"
            i += 1

        print(result)
        table += 1