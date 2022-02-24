def most_frequent(string):
   new=sorted(string)
   char=set(new)
   return list(char)
string=list(input()) 
count=0
char=most_frequent(string)
for i in char:
    count=0
    for x in string:
         if i==x:
              count+=1
    print(i,":",count)
    
