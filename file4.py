my_file=open("people_exercise.txt","r")
for j in my_file:
    if "delhi" in j:
        s=open("delhi.txt","a")
        s.write(j)
    elif "shimla" in j:
        d=open("shimla.txt","a")
        d.write(j)
    else:
        o=open("other.txt","a")
        o.write(j)