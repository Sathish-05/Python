n=int(input("Enter the No of terms:"))
n1=0
n2=1 
count=0
if n<=0:
    print("Incorrect Input,Please Enter a positive input")
elif n==1:
    print ("The fibonacci sequence of the numbers is:")  
    print(n1)
else:
    print ("The fibonacci sequence of the numbers is:")  
    while count<n:
        print(n1)
        n3=n1+n2
        n1=n2
        n2=n3
        count+=1
