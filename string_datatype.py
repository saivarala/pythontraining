l1 = ["Hello World","say something","red alert"]

for s in l1:
 if s.endswith('alert'):
  print(s)

a = " Today"  
b = "monday"
s = [a,b]
print("+".join(s))
print(b.replace("M","+"))
print(b.title())
print(b.upper())
print(b.rfind('a'))