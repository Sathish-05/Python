f= open("sathish.txt","w+")
for i in range(2):
     f.write("Hai,I'm Sathish\n")
f.close()
f=open("sathish.txt", "a+")
for i in range(2):
     f.write("Hai,I'm Sathish\n")
f.close()
f=open("sathish.txt", "r")
if f.mode == 'r':
    con =f.read()
    print(con)
f.close()
