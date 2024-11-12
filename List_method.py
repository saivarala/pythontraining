# l1 = ["apples","bananas","mangoes",5,False,3.99]
# l2 = []
# #print(type(l1))
# t1 = ("apples","mango")
# t2 = ("gold","sliver","copper")

# m1 = [1,2]
# m2 = [3,4]
# l3 = [m1,m2]
# l3.append([1,2,3])
# l3.extend(['1',2,3])
# l3.insert(0,5)
# #print(l3.pop())
# print(l3)
# ### deleting
# #del l3
# # len(l3)
# # l3.remove(5)
# # print(l3)

# ## in 
# if [3,4] in l3 : 
#     print("Yes")

# print(l3.count(3))
# print(l3.reverse())


# print(l4)
# print(sorted(l4))
# print(l4)
# print(l4.sort())
# print(l4)

l4 = [1,2,3,4,5,8,9,10] 
l5 = [4,5,8,9]
l4.extend(l5)
print(l4)
s4 = set(l4)
# List Comp.
res2 = [n for n in l4 if n%2== 0]
print(f"res2 : {res2}")

def find_even(l):
    res = []
    for n in l:
        if n%2 == 0:
            res.append(n)
    return res
print(f"res for function : {find_even(l4)}")



