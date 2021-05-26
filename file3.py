my_file3=["kotak","HDFC","RBL","SBI","Bank of Baroda"]
f=open("people3.txt","w")
i=0
while i<len(my_file3):
    f.write(my_file3[i])
    f.write("\n")
    i=i+1