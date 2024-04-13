print(f"Calculator")

sum = 0

while True:
    #1. Input
    f1 = input("How many minutes: ")
    f2 = input("How many seconds: ")

    #2. Process
    sum = int(f1)*60 + int(f2)

    #3. Output
    print(f"It should be = {sum} seconds ")
    res = input("Continue? (yes/no) : ")
    if res == "no" :
        print(f"Exit")
        break;
