# Dictionary:
# It is an unordered collection of data values which store data in a key value pair.

#creation
# d={}
# d={3:'c',4:{1:'a',2:'b'}}
d={3:'c',4:[1,2,3,4]}
# d=dict([(1,'abc'),(2,'bcd')])

#accessing
# print(d[3])
# print(d.get(3))
# for i in d:
#     print(i,d[i])

#Insertion
d[5]='Jaipur' #one element at a time
d[6]=11,22,33 #Set of values
d[5]='India' #Updating existing value
d[8]={1:'a',2:'b'} #adding nested key-value
d[9]={1:'a',2:{'Nested':'Hi'}} #adding nested dict
d[0]='India'

# print(d[9][2]['Nested'])

#Deletion
# del d[9][2]
# d.pop(9)  #pop the given key,value pair
# d.popitem() #deletes last element
# d[8].pop(1) #deletes nested dictorny item
# print(d.values()) #return values 


# Program 1: WAP to sort a dictionary by keys
# Program 2: WAP to sort a dictionary by values
# Program 3: WAP to merge two dictionaries in a sorted form
# Program 4: WAP to create a Grade Calculator
# Program 5: WAP to remove all duplicate words from a given sentence
# Program 6: WAP to count frequency of an element in a list using dictionary
# Program 7: WAP to convert a list of tuples into dictionary

d1={1:'9',2:'8',0:'7'}

#Program 1
a=sorted(d1.items(), key=lambda x: x[0])    
print(a)

#Program 2
a=sorted(d1.items(), key=lambda x: x[1])    
print(a)

#Program 3
d2={1:'9',2:'8',0:'7'}
d3={1:'9',2:'8',0:'7'}
a=sorted(d2.items(), key=lambda x: x[0])  
b=sorted(d3.items(), key=lambda x: x[0])  
a.append(b)
print(a)

#Progran 4
st={'Maths':80,'English':80}
n=st.values()
t=sum(n)/len(n)
if t>=91:
    print("A+")
elif t>=80:
    print("A")
elif t>=70:
    print("B+")

#Program 5


#Program 6
my_list=['a','a','a','b','b']
freq = {} 
for item in my_list: 
    if (item in freq): 
        freq[item] += 1
    else: 
        freq[item] = 1
  
for key, value in freq.items(): 
    print(key, value) 

#Program 7
lst=[(1,'a'),(2,'b')]
dt={}
for i in lst:
    dt[i[0]]=i[1]
print(dt)

