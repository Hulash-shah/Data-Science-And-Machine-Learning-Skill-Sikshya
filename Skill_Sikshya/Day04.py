
# variable  length arguments in functions


# def print_all(*args):
#     print("positional arguments")
#     print(args)
# print_all("a",2, 2,2,3,4,"b","c")


# def sum_all(*args):
#     return sum(args)


# print(sum_all(1,2,3,4,5))


# #  *kwargs


# def print_all(**kwargs):
#     print("keyword arguments")
#     print(kwargs)
# print(print_all(num1 = 1, num2 = 3 , value = 5, name ="hulash"))



# def calculate_area(shape:str, **kwargs):
#     area = 0
#     if shape == "square":
#         area = kwargs.get("length", 0) ** 2
#     elif shape == "rectangle":
#         area = kwargs.get("length", 0) * kwargs.get("breadth", 0)
#     elif shape == "rhombus":
#         if "length" in kwargs.keys() and "breadth" in kwargs.keys():
#              area = kwargs.get("length", 0) * kwargs.get("breadth", 0)
#     else:
#         print(f"{shape} is not supported")
#     return area

# print(calculate_area("square", length = 4))#  
# print(calculate_area("rectangle", length = 4 , breadth = 5)) 
# print(calculate_area("rhombus", length = 4 , breadth = 5)) 



# def print_args( shape , *args ,**kwargs):
#     print(shape)
#     print(args)
#     print(kwargs)
    
# print(print_args("cylinder", 1, 1, 3, 4, name="Hulash", num= 3345))



def std_dev(*args):
    n = len(args)
    X_bar = sum(args)/ n
    sq = sum(i**2 for i in args)
    
    std = ((sq/n) - (X_bar ** 2)) ** 0.5
    
    return std

print(std_dev(1,2,3,4,5))



def std_dev(*nums):
    n = len(nums)
    mean = sum(nums)/n
    numerator = sum((x - mean) ** 2 for x in nums)
    std = (numerator/n) ** 0.5
    return std

print(std_dev(1,2,3,4,5))

    
# lambda Expression


def power_up( base , power):
    return base ** power
print(power_up ( 2 , 3))



power_up_lambda = lambda base , power : base ** power
print(power_up_lambda(4,2))



area = lambda length , breadth , height : 2 * ( length*breadth + breadth * height + length * height )
print(area ( 4,5, 6))