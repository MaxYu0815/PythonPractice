print("Movie length Calculator")

while True:
    # 1. Input
    film = input("Enter the name of your film: ")
    minutes = int(input("Enter the runtime of your film: "))
    
    # 2. Process
    hours = minutes // 60
    remaining_minutes = minutes % 60
    
    # 3. Output
    print(f"{film} will run = {hours} hours, {minutes} minutes. ")
    res = input("Continue to check the runtime of next film? (Yes/No): ")
    if res.lower() == "no":
        print("Exit")
        break
