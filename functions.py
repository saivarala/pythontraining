# -- open file
# -- read from the file 
# -- write something
# -- close file

# with open(file_name, "r") as f:
#     s = f.readlines()
# s.upper()
# with open(file_name, "w") as f:
#     f.writelines(s)
#      

# class 
# def read_file(file_name):
#     with open(file_name, "r") as f:
#     s = f.readlines()
#     return s

# def write_file(s, file_name):
#     with open(file_name, "r") as f:
#     s = f.readlines()
#     return file_name
# def convert(s):
#     return s.upper()

# if __name__ == '__main__':
#     s = read_file(file_name)
#     write_file(convert(s))

def sum_two(a:int,b:int) -> int:
    """ 
    It sums two number and return sum
    @parameters
    a : int
    b : int
    """
    sum = a + b
    return sum

a = sum_two('5','5')
print(a)