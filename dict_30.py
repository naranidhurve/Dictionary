# i=65
# while i<=68:
#     j=65
#     while j<=i:
#         print("*",end=" ")
#         j=j+1
#     print()
#     i=i+1
    
# i=0
# while i<=4:
    # space=4-i
    # while space>0:
    #     print(end=" ")
    #     space-=1
    # n=i+1
    # while n>0:
    #     print("*",end=" ")
    #     n-=1
    #     i+=1
    # print()

    

dic={"a":[4,3,1],"b":[6,13,9],"c":[9,2]}
k={}
for key in dic:
    a=dic[key]
    i=0
    c=0
    while i<len(a):
        c=c+a[i]
        i=i+1
    k[key]=[c]
print(k)


