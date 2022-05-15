#3
filename="t.txt"
infile=open(filename,'r')
s=infile.read()
l=s.splitlines()
infile.close()
count=0
for i in l:
    print(i[:-1])
    s=input()
    if s==i[-1]:
        count+=1
username=input("enter your name ")
count=str(count)
sw=username+"       "+count
print(sw)
out=open("ghasaq.txt",'w')
out.write(sw)
out.close()