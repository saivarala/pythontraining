### PEP 8 - 
# linting - flake8
i = 0
fruits = ['apple', 'mango', 'bananas']
fruits.append(5)

def PrintFruit(*detectme) : 
    try : 
        for i in range(len(fruits)):
            print(f"{i} :{fruits[i]}")
    except Exception as e:
        raise e
     
PrintFruit()

while i < len(fruits):
    print(f"{i} :{fruits[i]}")
    i += 1
