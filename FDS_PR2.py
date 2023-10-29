marks=[]
present=[]
absent=[]

nos=int(input("Enter Number of student"))
i = 0
j=0
k=0
while i<nos:
    b=input("enter marks:")
    marks.append(b)
    i=i+1


while j<nos:
    if marks[j]=="abs":
        absent.append(marks[j])
    else:

        present.append(int(marks[j]))
    j=j+1


while (k<len(present)):
    print("present:",present[k])
    k=k+1


def avg():
    total=0
    avg=0
    i=0
    while i<len(present):
        total=total+present[i]
        i=i+1
        avg=total/len(present)
    print("total :",total)
    print('Average:',avg)

def high():
    high=0
    h=0
    while(h<len(present)):
        if high<present[h]:
          high=present[h]
        h=h+1
    print("Highest is :",high)

def low():
    low=999
    l=0
    while(l<len(present)):
       if low>present[l]:
           low=present[l]
       l=l+1
    print("Lowest Marks are :",low)


def abs():
    print("Number Of student Absent:",len(absent))


def frequency():
    hf=0
    for i in range(0,len(present),1):
        fr=1
        
        for j in range(i+1,len(present),1):
           if present[i]==present[j]:
               fr=fr+1
              
               if fr>hf:
                   hf=fr
                   p=present[i]
                   
                   print("Highest Frequency:",hf,"For marks",p)


avg()
high()
low()
abs()
frequency()



