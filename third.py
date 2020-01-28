# create a list of tuples from given list having number and its cube in each tuple. i/p=[1,2,3] o/p=[(1,1),(2,8),(3,27)]
# sort a list of tuples by second element. i/p=[('ab',100),('xy',50),()] o/p=[(xy,50),(ab,100),()]
# sort the list of tuples by third element using a specific ordering. i/p=[(r,2.2,100),(t,34.3,400)...] order=[400,100..] 
# find mismatch items on same index in two tuples.   
# find the tuples containing given element from the list of tuples.  // [(11,22),(,33,55),(55,77),(77,99),(55,88),(11,44)] o/p= (11,22) (11,44) (55,77) (55,88)

# Program 1
lst=[]
n=int(input("Enter Number of elements of list "))
for i in range(n):
    lst.append(int(input("Enter element ")))
nlst=[]
for i in lst:
    nlst.append((i,pow(i,3)))
print(nlst)

# Program 2
lst=[]
n=int(input("Enter Number of elements of list "))
for i in range(n):
    line=input("Enter Tuple items in line ")
    lst.append(tuple(line.split(" ")))
nlst=sorted(lst,key= lambda lst:lst[1])
print(nlst)

# Program 3

lst=[]
n=int(input("Enter Number of elements of list "))
for i in range(n):
    line=input("Enter Tuple items in line ")
    lst.append(tuple(line.split(" ")))
nlst=[]
print("Enter order of sorting")
for i in range(n):
    nlst.append(int(input()))

s=[]
for a in nlst:
    for i in range(n):
        if a==int(lst[i][2]):
            s.append(lst[i])
print(s)

# Program 4
print("Enter fiirst tuple")
n1=tuple(int(x) for x in input().split(" "))

print("Enter second tuple")
n2=tuple(int(x) for x in input().split(" "))

        
for i in range(len(n1)):
    if n1[i]!=n2[i]:
        print("Mismatch Index: ",i)

# Program 5
lst=[]
n=int(input("Enter Number of elements of list "))
for i in range(n):
    line=input("Enter Tuple items in line ")
    lst.append(tuple(line.split(" ")))

for i in range(n):
    for j in range(n):
        if lst[i][0]==lst[j][0] and i!=j:
            print(lst[i],lst[j])