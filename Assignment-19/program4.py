#4. Write a python program to create a function which expects kwargs arguments.
def fun(*t):
    average=sum(t)/len(t)
    print(average)
fun(20,30,40) 
fun(20,30,40,50,60)    
fun(20,30,40,10,10,10)    
fun(20,30,40,20,30,20,40)    
   
    