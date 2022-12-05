"""9. Write a python program to create a function to check whether a number falls in a
given range."""

def falls():
    accp=int(input("Enter any number for guess the number in range or not ...:"))
    for i in range(1,101):
        if 1<= accp <=100:
            print("Yes You have fall between range .")
            break
        else:
           print("Sorry you have out of range....?")
           break
                
falls()