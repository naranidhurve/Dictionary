# import itertools   
# dict={1:[98,42,84,92],2:[62,82,43,50],3:[90,84,69,70]}
# for combo in itertools.product([dict[k] for k in sorted(dict.keys())]):
#     sum=0
#     ave=0
#     for i in dict:
#         ave=ave-sum
#         print (ave) 

   
dict={"a":[98,42,84,92],"b":[62,82,43,50],"c":[90,84,69,70]}
m={}
for key, average in dict.items():
    n=[sum(average)]
    m[key]=n
print(m)


 

# l=list(dict)
# print(l)
# for x in dict.values():
   

# str="abcdeabcdfgf"
# def fun(str):
#     i=0
#     while i>len(str):
#         str=sum()
#         i=i+1
#         print(str)
# fun(sum)



