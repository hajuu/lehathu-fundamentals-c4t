attempts=0
while True:
    response=input("Do you want to quit?(y/n): ")
    if response=="n":
        attempts+=1
    elif response=="y":
        break
    else:
        print("Please input y or n")
print("Exiting after",attempts,"attempts.")