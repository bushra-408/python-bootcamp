#sum of elements using ascii
"""inp="hello 123world"
sum=0
for i in inp:
    if(ord(i)>=48 and ord(i)<=57):
        sum+=int(i)
print(sum)"""
#write a code to print all the capital letters in a given string
"""inp="BuShRa TaBaSuM"
for i in inp:
    if(ord(i)>=68 and ord(i)<=90):
        print(i,end=" ")"""
#remove all the brackets from the given algebraic expression
"""inp=input()
for i in inp:
    if(ord(i)==40 or ord(i)==41 or ord(i)==91 or ord(i)==93 or ord(i)==123 or ord(i)==125):
        pass
    else:
        print(i,end=" ")
print()"""
#i/p=ABC,4
#4=skip
#o/p=EFG
#ex:xyz
"""hint:#x=120+3=123----a=97
#chr(123)=|
#y=121+3=124----b=98
#chr(124)=}
#z=122+3=125----c=99
#char(125)=~"""
#hello--------world-----
#0/p:---------helloworld
"""inp=input()
count=0
ans=""
for i in inp:
    if(i=="-"):
        count+=1
    else:
        ans=ans+i
print("-"*count+ans)"""
#*****
#*****
#*****
#*****
#*****
"""for i in range(5):
    for j in range(5):
        print("*",end="")
    print()"""
# ****
#* ***
#** **
#*** *
#***
"""for i in range(5):
    for j in range(5):
        if(i==j):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()"""


