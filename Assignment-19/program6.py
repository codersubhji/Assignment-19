#6. Write a python program to create a function that finds a maximum of four numbers.
def funmx(a,b,c,d):
    if a>b and a>c and a>d:
        print(a)
    elif b>a and b>c and b>d:
        print(b)
    elif c>a and c>b and c>d:
        print(c)
    else:
        print(d)            
funmx(200,300,40,100)                    
        
    