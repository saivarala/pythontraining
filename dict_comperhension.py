
list1 = [x for x in range(10) if x%2 == 0]
print(list1)
list2 = ["bmw","tesla", "honda","mazda"]
list3 = [10,20,3,4]
dict1 = {x:y for x,y in zip(list2,list3)}
print(dict1["bmw"])
dict2 = {tuple([1,2,3,4]) : "shooping"}
print(dict2[(1, 2, 3, 4)])

for key, value in dict1.items():
    print(key,value)