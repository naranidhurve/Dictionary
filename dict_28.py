# dict1={1:2,2:3,3:4,4:5}
# sum=0
# for i in dict1.values():sum=sum+1
# print(sum)

# c=dict()
# for i in range(1,16):c=i*i
# print(c)

# s={'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56}
# a={'python':20,"gaurav":300,'dev':34,"karan":43}
# c={}
# for i in (s,a):c.update(i)
# print(c)

dic={"A":[4,6],"B":[9,6],"C":[3,5]}
m={}
for key in dic:
    a=dic[key]
    i=0
    c=0
    while i<len(a):
        c=c+a[i]
        i=i+1
    m[key]=[c]
print(m)